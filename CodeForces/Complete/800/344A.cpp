//
// Created by Conor on 5/29/2020.
//

#include <iostream>

using namespace std;

int main() {
    int n, val, current;
    int groups = 1;

    cin >> n;
    cin >> current;
    for (int i = 0; i < n-1; ++i) {
        cin >> val;
        if (val != current) {
            groups++;
            current = val;
        }
    }

    cout << groups;
}