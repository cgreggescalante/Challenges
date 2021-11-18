//
// Created by Conor on 11/6/2020.
//

#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;

    for (int i = 0; i < t; ++i) {
        int l, r;
        cin >> l >> r;
        bool works = true;

        for (int a = 2; a <= l * 2; ++a) {
            works = true;
            for (int x = l; x <= r; ++x) {
                if (x % a < a / 2.0) {
                    works = false;
                    break;
                }
            }
            if (works) {
                break;
            }
        }

        if (works) {
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
    }
}