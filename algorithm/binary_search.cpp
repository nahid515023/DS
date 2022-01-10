#include <iostream>
using namespace std;

int binary_search(int arr[], int n, int x)
{
    int l = 0, h = n, m = 0;
    while (l <= h)
    {
        m = (int)(l + h) / 2;
        if (arr[m] == x)
        {
            return m;
        }
        if (arr[m] > x)
        {
            h = m - 1;
        }
        else
        {
            l = m + 1;
        }
    }
    return -1;
}

int main()
{
    int arr[] = {2, 3, 4, 10, 40};
    int n = sizeof(arr) / sizeof(arr[0]);
    int x;
    cout << "Enter the value : ";
    cin >> x;
    int r = binary_search(arr, n, x);
    if (r == -1)
    {
        cout << x << " is not found.\n";
    }
    else
    {
        cout << x << " is found in index " << r + 1 << endl;
    }
}