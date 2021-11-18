//
// Created by Conor on 11/6/2020.
//

#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> home;
    vector<int> guest;

    for (int i = 0; i < n; ++i) {
        int h, g;
        cin >> h >> g;
        home.push_back(h);
        guest.push_back(g);
    }

    int count = 0;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (i != j) {
                if (home[i] == guest[j]) {
                    count++;
                }
            }
        }
    }

    cout << count;
}