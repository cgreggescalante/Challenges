//
// Created by Conor on 11/15/2020.
//

#include <iostream>
#include <map>

using namespace std;

int main() {
    int n;
    cin >> n;

    map<string, int> names;
    string name;

    for (int i = 0; i < n; ++i) {
        cin >> name;
        if (names.find(name) == names.end()) {
            names[name] = 1;
            cout << "OK" << endl;
        } else {
            cout << name + to_string(names[name]) << endl;
            names[name]++;
        }
    }
}