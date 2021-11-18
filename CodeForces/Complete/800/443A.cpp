//
// Created by Conor on 11/13/2020.
//

#include <iostream>
#include <vector>
using namespace std;

int main() {
    string line;
    getline(cin, line);

    if (line.length() == 2) {
        cout << 0;
        return 0;
    }

    line.erase(0, 1).erase(line.size()-1);

    string characters;

    size_t pos = 0;
    char token;
    while ((pos = line.find(", ")) != string::npos) {
        token = line[0];
        if (characters.find(token) == string::npos) {
            characters.push_back(token);
        }
        line.erase(0, pos + 2);
    }

    token = line[0];
    if (characters.find(token) == string::npos) {
        characters.push_back(token);
    }

    cout << characters.length();
}