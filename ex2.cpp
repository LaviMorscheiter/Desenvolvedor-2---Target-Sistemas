#include <iostream>

using namespace std;

int fibonacci(int n) {
    if (n <= 1)
        return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}
bool pertenceFibonacci(int num) {
    int a = 0, b = 1, c = 0;
    while (c < num) {
        c = a + b;
        a = b;
        b = c;
    }
    return c == num || num == 0;
}

int main() {
    int n=5, num=10;
    cout << "Sequência de Fibonacci: ";
    for (int i = 0; i < n; i++) {
        cout << fibonacci(i) << " ";
    }
    if (pertenceFibonacci(num)) {
        cout << "\nO número " << num << " pertence à sequência de Fibonacci." <<endl;
    } else {
        cout << "\nO número " << num << " não pertence à sequência de Fibonacci." <<endl;
    }

    return 0;
}