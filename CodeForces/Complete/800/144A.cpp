//
// Created by Conor on 6/1/2020.
//

#include <iostream>
#include <vector>

using namespace std;

int main() {
    int max, max_pos, min, min_pos, n, val;
    cin >> n;

    vector<int> soldiers;

    max = 0;
    min = 1000;

    for (int i = 0; i < n; ++i) {
        cin >> val;
        soldiers.push_back(val);
    }

    for (int j = 0; j < n; ++j) {
        if (soldiers[j] <= min) {
            min = soldiers[j];
            min_pos = j;
        }
        if (soldiers[j] > max) {
            max = soldiers[j];
            max_pos = j;
        }
    }

    int total = soldiers.size() - min_pos - 1;

    soldiers.erase(soldiers.begin() + min_pos);
    soldiers.push_back(min);

    if (min_pos < max_pos) {
        max_pos--;
    }

    total += max_pos;

    cout << total;
}