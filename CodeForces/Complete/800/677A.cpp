//
// Created by Conor on 5/29/2020.
//

#include <iostream>

using namespace std;

int main() {
    int n, h, val;
    cin >> n >> h;

    int total = 0;
    for (int i = 0; i < n; ++i) {
        cin >> val;
        if (val > h) {
            total += 1;
        }
        total += 1;
    }

    cout << total;
}