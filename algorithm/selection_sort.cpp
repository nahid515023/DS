#include<iostream>
using namespace std;

void selection_sort(int arr[],int n)
{
    for(int i=0;i<n;i++)
    {
        int key = i;
        for(int j=i+1;j<n;j++)
        {
            if(arr[key]>arr[j])
            {
                key=j;
            }
        }
        int temp=arr[i];
        arr[i]=arr[key];
        arr[key]=temp;
    }
}

int main()
{
    int arr[]={5,3,2,6,8,7,7,1};
    int n = sizeof(arr)/sizeof(arr[0]);
    selection_sort(arr,n);

    for(int i=0;i<n;i++)
    {
        cout<<arr[i]<<" ";
    }
}