//
// Created by Conor on 5/29/2020.
//

#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, val;
    cin >> n;

    vector<int> result;
    result.reserve(n);
    for (int j = 0; j < n; ++j) {
        result.push_back(0);
    }

    for (int i = 0; i < n; ++i) {
        cin >> val;
        result[val-1] = i+1;
    }

    for (int v : result) {
        cout << v << " ";
    }

    cout << endl;
}