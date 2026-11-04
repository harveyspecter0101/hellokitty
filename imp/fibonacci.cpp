// #include<bits/stdc++.h>
// using namespace std;
// // Recursive Function
// int fib(int n){
//     if(n <= 0) return 0;
//     if(n == 1) return 1;
//     return fib(n-1) + fib(n-2);
// }
// int main(){
//     int n;
//     cin >> n;
//     // Recursive
//     cout<<fib(n)<<endl;
//     // Iterative
//     vector<int>fib(n+1,0);
//     fib[0] = 0;
//     fib[1] = 1;
//     for(int i=2;i<=n;i++) fib[i] = fib[i-1] + fib[i-2];
//     cout<<fib[n]<<endl;
//     // Further optimization
//     int prev = 1;
//     int prev_prev = 0;
//     int curr = 0;
//     for(int i=2;i<=n;i++){
//         curr = prev + prev_prev;
//         prev_prev = prev;
//         prev = curr;
//     }
//     cout<<curr<<endl;
// }

// gpt code ahh -----------------------

#include <iostream>
using namespace std;

// Recursive function
int fibonacci(int n) {
    if (n == 0)
        return 0;
    if (n == 1)
        return 1;

    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    int n, a = 0, b = 1, c;
    cout << "Enter number of terms: ";
    cin >> n;

    cout << "\nFibonacci Series using Recursion: ";
    for (int i = 0; i < n; i++) {
        cout << fibonacci(i) << " ";
    }

    cout << "\nFibonacci Series using Iteration: ";
    for (int i = 0; i < n; i++) {
        cout << a << " ";

        c = a + b;
        a = b;
        b = c;
    }
    return 0;
}