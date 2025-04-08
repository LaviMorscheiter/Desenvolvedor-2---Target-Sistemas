#include <iostream>
#include <math.h>

using namespace std;

int main() {
    int i, k, Soma;
    i = 13;
    Soma = 0;
    k = 0;

    while (k < i){
        k = k + 1;
        Soma = Soma + k;
        cout << "Soma = " << Soma << endl;
    }

    return 0;
}
