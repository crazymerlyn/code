#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;


int main() {
    int n = 1e6-1;
    vector<int> mdrs(n+1);
    for (int i = 1; i <= n; ++i) mdrs[i] = (i-1)%9 + 1;

    for (int i = 2; i * i <= n; ++i) {
        for (int j = 2; i*j <= n; ++j) {
            mdrs[i*j] = max(mdrs[i*j], mdrs[i] + mdrs[j]);
        }
    }

    cout << accumulate(mdrs.begin()+2, mdrs.end(), 0) << endl;
}


