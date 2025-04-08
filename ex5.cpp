#include <iostream>
#include <string>
using namespace std;

void inverterString(string& str) {
    int tamanho = str.length();
    for (int i = 0; i < tamanho / 2; i++) {
        swap(str[i], str[tamanho - i - 1]);
    }
}

int main() {
    string minhaString = "Bom dia!";
    cout << "String original: " << minhaString << endl;

    inverterString(minhaString);

    cout << "String invertida: " << minhaString << endl;

    return 0;
}