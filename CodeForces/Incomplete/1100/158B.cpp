//
// Created by Conor on 5/28/2020.
//

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> groups;

    int val;
    for (int i = 0; i < n; ++i) {
        cin >> val;
        groups.push_back(val);
    }

    sort(groups.begin(), groups.end(), greater<int>());

    for (int j = 0; j < groups.size(); ++j) {
        int diff = 4 - groups[j];
        for (int k = diff; k > 0; k--) {
            const vector<int>::iterator &p = std::find(groups.begin(), groups.end(), k);
            if (p != groups.end()) {
                if (groups[j] + k <= 4) {
                    groups[j] += k;
                    groups[*p] = 100;
                }
            }
            if (groups[j] == 4) {
                break;
            }
        }
//        const vector<int>::iterator &p = std::find(groups.begin(), groups.end(), 4 - groups[j]);
//        if (p != groups.end()) {
//            for (int i = j + 1; i < groups.size(); ++i) {
//                if (groups[j] + groups[i] <= 4) {
//                    groups[j] += groups[i];
//                    groups.erase(groups.begin() + i);
//                    i--;
//                } else if (groups[j] == 4) {
//                    break;
//                }
//            }
//        }
    }

    for (int g : groups) {
        cout << g << " ";
    }
    cout << endl;

    cout << groups.size();
}