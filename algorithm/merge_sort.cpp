#include <iostream>
using namespace std;

void merge(int arr[], int f, int m, int l)
{
    int s1 = m - f + 1;
    int s2 = l - m;
    int a1[s1], a2[s2];

    for (int i = 0; i < s1; i++)
        a1[i] = arr[f + i];
    for (int j = 0; j < s2; j++)
        a2[j] = arr[m + j + 1];

    int i, j, k;
    i = 0, j = 0;
    k = f;
    while (i < s1 && j < s2)
    {
        if (a1[i] <= a2[j])
        {
            arr[k] = a1[i];
            i++;
        }
        else
        {
            arr[k] = a2[j];
            j++;
        }
        k++;
    }

    while (i < s1)
    {
        arr[k] = a1[i];
        i++;
        k++;
    }
    while (j < s2)
    {
        arr[k] = a2[j];
        j++;
        k++;
    }
}

void mergeSort(int arr[], int f, int l)
{
    int m = (f + l) / 2;
    if (f < l)
    {
        mergeSort(arr, f, m);
        mergeSort(arr, m + 1, l);
        merge(arr, f, m, l);
    }
}

int main()
{
    int arr[] = {1, 3, 8, 9, 4, 3, 2, 1};
    int n = sizeof(arr) / sizeof(arr[0]);
    mergeSort(arr, 0, n - 1);

    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
}