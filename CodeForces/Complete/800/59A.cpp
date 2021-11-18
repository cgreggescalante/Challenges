//
// Created by Conor on 5/28/2020.
//

#include <iostream>

using namespace std;

int main() {
    string word;

    cin >> word;
    int high = 0;
    int low = 0;

    for (char c : word) {
        if (islower(c)) {
            low++;
        } else {
            high++;
        }
    }

    if (high > low) {
        for (char & c : word) {
            c = toupper(c);
        }
    } else {
        for (char & c : word) {
            c = tolower(c);
        }
    }

    cout << word;
}