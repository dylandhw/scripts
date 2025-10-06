#include <iostream>
using namespace std;

long long power(long long a, long long b)
{
    long long res = 1;
    while(b > 0)
    {
        if (b%2 == 1) res *= a;
        a *= a;
        b /= 2;
    }
    return res;
}

int main()
{
    cout << power(2, 10) << endl;
}