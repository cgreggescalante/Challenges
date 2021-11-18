//
// Created by Conor on 6/5/2020.
//

#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    string song, result;
    unsigned int loc;
    cin >> song;

    vector<string> words;
    loc = song.find("WUB");
    while (loc != string::npos) {
        words.push_back(song.substr(0, loc));
        song = song.substr(loc+3);
        loc = song.find("WUB");
    }

    words.push_back(song);

    for (const string& w : words) {
        if (!w.empty()) {
            cout << w << " ";
        }
    }
}