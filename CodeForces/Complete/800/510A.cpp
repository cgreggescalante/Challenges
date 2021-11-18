//
// Created by Conor on 11/9/2020.
//

#include <iostream>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    bool side = false;

    for (int i = 0; i < n; ++i) {
        if (i % 2 == 0) {
            for (int j = 0; j < m; ++j) {
                cout << "#";
            }
        } else {
            if (side) {
                cout << "#";
            }
            for (int j = 0; j < m - 1; ++j) {
                cout << ".";
            }
            if (!side) {
                cout << "#";
            }
            side = !side;
        }
        cout << endl;
    }
}