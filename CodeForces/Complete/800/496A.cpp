//
// Created by Conor on 6/1/2020.
//

#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, p, q;
    cin >> n >> p;

    vector<int> levels;
    levels.reserve(n);
    for (int k = 0; k < n; ++k) {
        levels.push_back(0);
    }

    int val;

    for (int i = 0; i < p; ++i) {
        cin >> val;

        levels[val - 1] = 1;
    }

    cin >> q;
    for (int j = 0; j < q; ++j) {
        cin >> val;

        levels[val - 1] = 1;
    }

    for (int x : levels) {
        if (x == 0) {
            cout << "Oh, my keyboard!";
            return 0;
        }
    }

    cout << "I become the guy.";
}