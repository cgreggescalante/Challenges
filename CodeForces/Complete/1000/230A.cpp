//
// Created by Conor on 6/6/2020.
//

#include <iostream>
#include <vector>

using namespace std;

int main() {
    int s, n, x, y, min, min_index;
    cin >> s >> n;

    vector<int> strengths;
    vector<int> bonuses;

    for (int i = 0; i < n; ++i) {
        cin >> x >> y;
        bonuses.push_back(y);
        strengths.push_back(x);
    }

    while (!strengths.empty()) {
        min = 100000;
        min_index = -1;
        for (int i = 0; i < strengths.size(); ++i) {
            if (strengths[i] < min) {
                min = strengths[i];
                min_index = i;
            }
        }

        if (min >= s) {
            cout << "NO";
            return 0;
        }

        s += bonuses[min_index];

        bonuses.erase(bonuses.begin() + min_index);
        strengths.erase(strengths.begin() + min_index);
    }

    cout << "YES";
}