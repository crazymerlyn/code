#include <bits/stdc++.h>

using namespace std;
typedef vector<vector<int>> Mat;

void print_mat(Mat &mat) {
    /* int n = mat.size(); */
    /* for (int i = 0; i < n; ++i) { */
    /*     for (int j = 0; j < n; ++j) { */
    /*         cout << mat[i][j] << " "; */
    /*     } */
    /*     cout << endl; */
    /* } */
    /* cout << endl; */
}

int gauss(Mat &mat, Mat &inv) {
    int n = mat.size();
    for (int i = 0; i < n; ++i) {
        if (mat[i][i] == 0) {
            int ans = -1;
            for (int j = i + 1; j < n; ++j) {
                if (mat[j][i] == 1) {
                    ans = j; break;
                }
            }
            if (ans == -1) return -1;
            for (int j = 0; j < n; ++j) {
                mat[i][j] ^= mat[ans][j];
                inv[i][j] ^= inv[ans][j];
            }
        }

        for (int loopi = i + 1; loopi < n; ++loopi) {
            if (!mat[loopi][i]) continue;
            for (int j = 0; j < n; ++j) {
                mat[loopi][j] ^= mat[i][j];
                inv[loopi][j] ^= inv[i][j];
            }
        }
        print_mat(mat);
        print_mat(inv);
    }
    for (int i = n - 1; i >= 0; --i) {
        for (int loopi = i - 1; loopi >= 0; --loopi) {
            if (!mat[loopi][i]) continue;
            mat[loopi][i] ^= mat[i][i];
            for (int j = 0; j < n; ++j) {
                inv[loopi][j] ^= inv[i][j];
            }
        }
    }
    return 0;
}

int main() {
    int n; cin >> n;
    vector<vector<int>> mat(n, vector<int>(n));
    vector<int> ts(n);
    for (int i = 0; i < n; ++i) {
        int val; cin >> val;
        while (val != -1) {
            mat[val-1][i] = 1;
            cin >> val;
        }
    }

    vector<vector<int>> eye(n, vector<int>(n));
    for (int i = 0; i < n; ++i) eye[i][i] = 1;

    print_mat(mat);
    print_mat(eye);
    int res = gauss(mat, eye);
    print_mat(mat);
    print_mat(eye);

    if (res == -1) {
        cout << "No solution" << endl;
        return 0;
    }

    for (int i = 0; i < n; ++i) {
        int res = 0;
        for (int j = 0; j < n; ++j) {
            res += eye[i][j];
        }
        if (res % 2 == 1) cout << i + 1 << " ";
    }
    cout << endl;
    return 0;
}


