#include <iostream>
using namespace std;

int gcd(int a, int b)
{
    while(b != 0)
    {
        int temp = a%b;
        a = b;
        a = temp;
    }
    return a;
}

int main()
{
    cout << gcd(36, 60) << endl;
}