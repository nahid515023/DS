#include <bits/stdc++.h>
using namespace std;

int linear_search(int arr[], int n, int f)
{
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == f)
        {
            return i;
        }
    }
    return -1;
}

int main()
{
    int arr[] = {2, 3, 4, 10, 40, 50, 1};
    int n = sizeof(arr) / sizeof(arr[0]);
    int f;
    cout << "Which number you search : ";
    cin >> f;
    int x = linear_search(arr, n, f);
    if (x == -1)
    {
        cout <<f<<" is not found.\n";
    }
    else
    {
        cout << f << " is found in index " << x+1 << endl;
    }
}