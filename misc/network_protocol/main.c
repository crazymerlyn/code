#include <assert.h>
#include <stdio.h>

#include <libdillimpl.h>

#define cont(ptr, type, member) \
    ((type*)(((char*) ptr) - offsetof(type, member)))

struct quux {
    struct hvfs hvfs;
    struct msock_vfs mvfs;
    int u;
};

static void *quux_hquery(struct hvfs *hvfs, const void *id);
static void quux_hclose(struct hvfs *hvfs);
static int quux_hdone(struct hvfs *hvfs, int64_t deadline);

static int quux_msendl(struct msock_vfs *mvfs,
        struct iolist *first, struct iolist *last, int64_t deadline);
static ssize_t quux_mrecvl(struct msock_vfs *mvfs,
        struct iolist *first, struct iolist *last, int64_t deadline);

static int quux_type_placeholder = 0;
static const void* quux_type = &quux_type_placeholder;

static void quux_hclose(struct hvfs *hvfs) {
    struct quux* self = (struct quux*)hvfs;
    free(self);
}

static void *quux_hquery(struct hvfs *hvfs, const void *type) {
    struct quux* self = (struct quux*) hvfs;
    if (type == msock_type) return &self->mvfs;
    if (type == quux_type) return self;
    errno = ENOTSUP;
    return NULL;
}

static int quux_hdone(struct hvfs* hvfs, int64_t deadline) {
    errno = ENOTSUP;
    return -1;
}

static int quux_msendl(struct msock_vfs *mvfs,
        struct iolist *first, struct iolist *last, int64_t deadline) {
    struct quux *self = cont(mvfs, struct quux, mvfs);
    size_t sz = 0;
    for (struct iolist *it = first; it; it = it->iol_next) {
        sz += it->iol_len;
    }
    if (sz > 254) {
        errno = EMSGSIZE; return -1;
    }

    uint8_t c = (uint8_t) sz;
    struct iolist hdr = {&c, 1, first, 0};
    int rc = bsendl(self->u, &hdr, last, deadline);
    if (rc < 0) return -1;
    return 0;
}

static ssize_t quux_mrecvl(struct msock_vfs *mvfs,
        struct iolist *first, struct iolist *last, int64_t deadline) {
    struct quux *self = cont(mvfs, struct quux, mvfs);
    uint8_t sz;
    int rc = brecv(self->u, &sz, 1, deadline);
    if (rc < 0) return -1;
    if (!first) {
        rc = brecv(self->u, NULL, sz, deadline);
        if (rc < 0) return -1;
        return sz;
    }
    size_t bufsz = 0;
    for (struct iolist *it = first; it; it = it->iol_next) {
        bufsz += it->iol_len;
    }
    if (bufsz < sz) { errno = EMSGSIZE; return -1; }

    size_t rmn = sz;
    for (struct iolist *it = first; it; it->iol_next) {
        size_t torecv = rmn < it->iol_len ? rmn : it->iol_len;
        rc = brecv(self->u, it->iol_base, torecv, deadline);
        if (rc < 0) return -1;
        rmn -= torecv;
        if (rmn == 0) break;
    }
    return sz;
}

int quux_detach(int h) {
    struct quux* self = hquery(h, quux_type);
    if (!self) return -1;
    int u = self->u;
    free(self);
    return u;
}

int quux_attach(int u) {
    int err;
    struct quux *self = malloc(sizeof(struct quux));
    if (!self) { err = ENOMEM; goto error1; }
    self->hvfs.query = quux_hquery;
    self->hvfs.close = quux_hclose;
    self->hvfs.done = quux_hdone;
    self->mvfs.msendl = quux_msendl;
    self->mvfs.mrecvl = quux_mrecvl;
    self->u = u;
    int h = hmake(&self->hvfs);
    if (h < 0) { int err = errno; goto error2; }
    return h;
error2:
    free(self);
error1:
    errno = err;
    return -1;
}

coroutine void client(int s) {
    int q = quux_attach(s);
    assert(q >= 0);
    int rc = msend(q, "Hello, World!", 13, -1);
    assert(rc == 0);
    s = quux_detach(q);
    assert(s >= 0);
    rc = hclose(s);
    assert(rc == 0);
}

int main() {
    int ss[2];
    int rc = ipc_pair(ss);
    assert(rc == 0);
    go(client(ss[0]));
    int q = quux_attach(ss[1]);
    assert(q >= 0);
    char buf[256];
    ssize_t sz = mrecv(q, buf, sizeof(buf), -1);
    assert(sz >= 0);
    printf("%.*s\n", (int)sz, buf);
    int s = quux_detach(q);
    assert(s >= 0);
    rc = hclose(s);
    assert(rc == 0);
    return 0;
}
