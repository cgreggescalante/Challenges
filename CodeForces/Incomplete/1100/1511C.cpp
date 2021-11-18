//
// Created by Conor on 4/24/2021.
//

#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

int main() {
    int n, q, a, t;
    cin >> n;
    cin >> q;

    int last[50];
    for (int & i : last) {
        i = -1;
    }
    vector<int> cards;

    for (int i = 0; i < n; ++i) {
        cin >> a;
        cards.push_back(a);
    }

    for (int i = 0; i < q; ++i) {
        cin >> t;
        int start = last[t - 1];
        if (start == -1) {
            start = 0;
        }
        for (int j = start; j < n; ++j) {
            if (cards[j] == t) {
                cout << j + 1 << " ";
                cards.erase(cards.begin()+j);
                cards.insert(cards.begin(), t);
                last[t - 1] = 0;
                break;
            } else if (j < last[t - 1] && last[t - 1] != -1) {
                last[t - 1] = j;
            }
        }
    }
}