//
// Created by Conor on 11/13/2020.
//

#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int n, l;
    cin >> n >> l;

    int lanterns[n+2];

    lanterns[n] = 0;
    lanterns[n+1] = l;

    for (int i = 0; i < n; ++i) {
        cin >> lanterns[i];
    }

    sort(lanterns, lanterns + n + 2);
    int max_gap = 0;
    for (int i = 0; i < n + 1; ++i) {
        cout << lanterns[i] << endl;
        if (lanterns[i+1] - lanterns[i] > max_gap) {
            max_gap = lanterns[i+1] - lanterns[i];
        }
    }
    cout << max_gap / 2.;
}