//
// Created by Conor on 11/6/2020.
//

#include <iostream>
#include <map>

using namespace std;

int main() {
    map<string, int> faces;
    faces.insert({
         {"Tetrahedron", 4},
         {"Cube", 6},
         {"Octahedron", 8},
         {"Dodecahedron", 12},
         {"Icosahedron", 20}
    });

    int n;
    cin >> n;

    int total = 0;

    for (int i = 0; i < n; ++i) {
        string shape;
        cin >> shape;

        total += faces[shape];
    }

    cout << total;
}