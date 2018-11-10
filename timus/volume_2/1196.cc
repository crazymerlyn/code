#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n; cin >> n;
    set<int> s;
    for (int i = 0; i < n; ++i) {
        int k; cin >> k; s.insert(k);
    }
    int m; cin >> m;
    int res = 0;
    for (int i = 0; i < m; ++i) {
        int k; cin >> k;
        if (s.find(k) != s.end()) res += 1;
    }
    cout << res << endl;
    return 0;
}

