//
// Created by Conor on 5/28/2020.
//

#include <iostream>

using namespace std;

int main() {
    int n, val, taxis;
    taxis = 0;
    cin >> n;

    int counts[3];
    for (int & count : counts) {
        count = 0;
    }

    for (int i = 0; i < n; ++i) {
        cin >> val;
        if (val == 4) {
            taxis++;
        } else {
            counts[val - 1]++;
        }
    }

    int three_one;

    if (counts[2] > counts[0]) {
        three_one = counts[0];
    } else {
        three_one = counts[2];
    }

    taxis += three_one;

    counts[2] -= three_one;
    counts[0] -= three_one;

    taxis += counts[2];

    taxis += counts[1] / 2;

    counts[1] -= (counts[1] / 2) * 2;

    if (counts[1] == 1) {
        if (counts[0] >= 2) {
            counts[0] -= 2;
        } else {
            counts[0] = 0;
        }
        taxis++;
    }

    if (counts[0] > 4) {
        taxis += counts[0] / 4;
        counts[0] -= (counts[0] / 4) * 4;
    }

    if (counts[0] > 0) {
        taxis++;
    }

    cout << taxis;
}