#include <iostream>
#include <cstdlib>
using namespace std;


void gameSystem()
{
        srand(time(0));
        int x,y=rand()%11;
        cin>>x;
        if(x>10 || x<0)
        {
            cout<<"Max limit is 0-10.\n";
        }
        else if(x>y)
        {
            cout<<"Too high, Try again You can do it!\n";
            cout<<"Random Number was "<<y<<"\tbetter luck next time!\n";
        }
        else if(x<y)
        {
            cout<<"Too low, Try again You can do it!\n";
            cout<<"Random Number was "<<y<<"\tbetter luck next time!\n";
        }   
        else
        {
            cout<<"You did it!! Great job\nthere was 1/11 possibility of user inputing the correct number and you did it.\n";
        }
}

int main() 
{
    gameSystem();
    return 0;
}
