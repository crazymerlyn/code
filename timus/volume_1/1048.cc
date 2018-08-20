#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    ios_base::sync_with_stdio(false);
    cin >> n;
    vector<int> res(n);
    for (int i = 0; i < n; ++i) {
        int a, b;
        cin >> a >> b;
        res[i] = a + b;
    }
    int c = 0;
    for (int i = n-1; i >= 0; --i) {
        res[i] += c;
        c = res[i] / 10;
        res[i] %= 10;
    }
    if (c) cout << c;
    for (auto val : res) cout << val;
    cout << endl;
    return 0;
}
