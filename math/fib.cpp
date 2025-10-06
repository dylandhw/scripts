#include <iostream>
using namespace std;

void fibonacci(int n)
{
    long long a = 0, b = 1;
    cout << a << " " << b << " ";
    
    for (int i = 2; i < n; i++)
    {
        long long c = a + b;
        cout << c << " ";
        a = b;
        b = c;
    }
}

int main()
{
    fibonacci(10);
}