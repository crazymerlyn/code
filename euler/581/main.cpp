#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <set>

using namespace std;

int main() {
    long limit = 1109496723126l;
    vector<long> primes = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47};
    set<long> heap(primes.begin(), primes.end());
    long last = 1;
    long res = 0;

    while (heap.size()) {
        long n = *heap.begin();
        if (n == last + 1) {
            res += last;
        }
        heap.erase(heap.begin());

        for (auto p: primes) {
            if (n * p > limit) break;
            if (heap.find(n * p) == heap.end()) {
                heap.insert(n * p);
            }
        }
        last = n;
    }
    cout << res << endl;
}


