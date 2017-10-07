#include <iostream>
#include <algorithm>
#include <set>

using namespace std;

struct Fraction {
    long num;
    long denom;

    Fraction(long a, long b) {long gcd = __gcd(a, b); this->num = a / gcd; this->denom = b / gcd; }

    Fraction operator+(const Fraction b) const {return Fraction (this->num * b.denom + this->denom * b.num, this->denom * b.denom);};
    Fraction operator*(const Fraction b) const {return Fraction (this->num * b.num, this->denom * b.denom);};
    Fraction operator/(const Fraction b) const {return Fraction (this->num * b.denom, this->denom * b.num);};

    bool operator<(const Fraction b) const {return this->num * b.denom < this->denom * b.num;}
    bool operator==(const Fraction b) const {return this->num * b.denom == this->denom * b.num;}
    void operator=(const Fraction b) {this->num = b.num; this->denom = b.denom;};
};

using namespace std;

int main() {
    set<Fraction> dp[20];
    dp[1] = {Fraction(1,1)};
    set<Fraction> ans;
    int limit = 18;

    for (int count = 1; count <= limit; count++) {
        for (int i = 1; i < count; ++i) {
            for (auto l: dp[i]) {
                for (auto r: dp[count-i]) {
                    dp[count].insert(l + r);
                    dp[count].insert(l * r / (l + r));
                }
            }
        }
        set_union(dp[count].begin(), dp[count].end(), ans.begin(), ans.end(), inserter(ans, ans.begin()));
    }

    cout << ans.size() << endl;
}


