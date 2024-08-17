#include<iostream>
#include<string>
using namespace std;

void UNO_reverse()
{
    string x;
    getline(cin,x);
    int y=size(x),z=sizeof(x)-1;
    char c[z];
    cout<<"Total length:"<<y;
    cout<<endl;
    cout<<"Orignal: "<<x;
    cout<<endl;
    cout<<"Modified: ";
    for(int i=0;i<=y;i++)
    {
        c[i]=x[y-i];
        cout<<c[i];
    }
}

int main()
{
    UNO_reverse();
}
