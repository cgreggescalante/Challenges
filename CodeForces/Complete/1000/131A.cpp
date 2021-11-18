//
// Created by Conor on 6/6/2020.
//

#include <iostream>
#include <string>

using namespace std;

int main() {
    string word;
    cin >> word;

    bool caps = true;
    for (int i = 1; i < word.length(); ++i) {
        if (islower(word[i])) {
            caps = false;
            break;
        }
    }

    if (caps) {
        if (isupper(word[0])) {
            word[0] = tolower(word[0]);
        } else {
            word[0] = toupper(word[0]);
        }
        for (int j = 1; j < word.length(); j++) {
            word[j] = tolower(word[j]);
        }
    }

    cout << word;
}