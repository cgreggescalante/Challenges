//
// Created by Conor on 5/27/2020.
//

#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

int main() {
    vector <int> tokens;

    stringstream check;
    string input;
    cin >> input;
    check << input;

    string intermediate;

    while(getline(check, intermediate, '+')) {
        tokens.push_back(stoi(intermediate));
    }

    sort(tokens.begin(), tokens.end());

    for (int i = 0; i < tokens.size() - 1; ++i) {
        cout << tokens.at(i) << '+';
    }
    cout << tokens.at(tokens.size() - 1);
}