//
// Created by Conor on 11/6/2020.
//

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;

    char alpha[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    vector<char> alphabet(alpha, alpha+sizeof(alpha)-1);

    for (int i = 0; i < n; ++i) {
        char c;
        cin >> c;
        c = toupper(c);
        alphabet.erase(remove(alphabet.begin(), alphabet.end(), c), alphabet.end());
    }

    if (alphabet.empty()) {
        cout << "YES";
    } else {
        cout << "NO";
    }
}