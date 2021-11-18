//
// Created by Conor on 6/5/2020.
//

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n, val;
    cin >> n;

    vector<int> columns;

    for (int j = 0; j < n; ++j) {
        cin >> val;

        columns.push_back(val);
    }

    sort(columns.begin(), columns.end());

    for (int c : columns) {
        cout << c << " ";
    }
}