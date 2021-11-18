//
// Created by Conor on 11/6/2020.
//

#include <iostream>
#include <vector>

using namespace std;

int main() {
    int t;
    cin >> t;

    for (int i = 0; i < t; ++i) {
        int n, x;
        cin >> n >> x;

        vector<int> a, b;

        for (int j = 0; j < n; ++j) {
            int c;
            cin >> c;
            a.push_back(c);
        }

        for (int j = 0; j < n; ++j) {
            int c;
            cin >> c;
            b.push_back(c);
        }

        bool valid = true;

        for (int j = 0; j < n; ++j) {
            if (a[j] + b[n - j - 1] > x) {
                cout << "No\n";
                valid = false;
                break;
            }
        }

        if (valid) {
            cout << "Yes\n";
        }
    }
}