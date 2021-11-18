//
// Created by Conor on 6/3/2020.
//

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    vector<int> puzzles;
    int val;
    for (int i = 0; i < m; ++i) {
        cin >> val;
        puzzles.push_back(val);
    }

    sort(puzzles.begin(), puzzles.end());

    int min_gap = 10000;
    int gap;
    for (int j = 0; j < puzzles.size() - n + 1; ++j) {
        gap = puzzles[j + n - 1] - puzzles[j];
        if (gap < min_gap) {
            min_gap = gap;
        }
    }

    cout << min_gap;
}