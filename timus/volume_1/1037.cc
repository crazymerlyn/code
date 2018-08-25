#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N = 1 << 15;

int arr[1 << 15];
int tree[(1 << 16) - 1];

void _replace(int start, int end, int index, int val, int sindex) {
    if (index < start || index > end) return;
    if (start != end) {
        int mid = start + (end - start) / 2;
        _replace(start, mid, index, val, sindex * 2 + 1);
        _replace(mid+1, end, index, val, sindex * 2 + 2);
        tree[sindex] = min(tree[sindex * 2 + 1], tree[sindex * 2 + 2]);
    } else {
        tree[sindex] = val;
    }
}

void replace(int i, int time) {
    arr[i] = time;
    _replace(0, N-1, i, time, 0);
}

char get(int time, int i) {
    if (time - arr[i] < 600) {
        replace(i, time);
        return '+';
    }
    return '-';
}

int search(int start, int end, int time, int sindex) {
    while (start != end) {
        int mid = start + (end - start) / 2;
        if (tree[sindex * 2 + 1] <= time - 600) {
            end = mid;
            sindex = sindex * 2 + 1;
        } else {
            start = mid + 1;
            sindex  = sindex * 2 + 2;
        }
    }
    return start;
}

int add(int time) {
    int i = search(0, N-1, time, 0);
    replace(i, time);
    return i;
}

int main() {
    ios_base::sync_with_stdio(false);
    for (int i = 0; i < N; ++i) arr[i] = -1000;
    for (int i = 0; i < 2 * N - 1; ++i) {
        tree[i] = -1000;
    }
    while(! cin.eof()) {
        int time;
        char query;
        cin >> time >> query;
        if (cin.eof()) break;
        if (query == '+') {
            cout << add(time) + 1 << endl;
        } else {
            int i;
            cin >> i;
            cout << get(time, i - 1) << endl;
        }
    }
    return 0;
}

