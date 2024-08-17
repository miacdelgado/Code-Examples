#include <iostream>
using namespace std;
int main () {
    int culc_num1;
    cin >>culc_num1;
    char opr;
    cin >> opr;
    int culc_num2;
    cin >>culc_num2;
    int culc_adt = culc_num1 + culc_num2;
    int culc_mut = culc_num1 * culc_num2;
    int culc_sub = culc_num1 - culc_num2;       int culc_dev = culc_num1 / culc_num2;
    int culc_rem = culc_num1 % culc_num2;
    switch (opr) {
    case '+':
    cout << culc_adt;
    break;
    case '-' :
    cout << culc_sub;
    break;
    case '*':
    cout << culc_mut;
    break;
    case '/':
    cout << culc_dev;
    break;
    case '%':
    cout << culc_rem;
    break;
    default : { cout <<"error";} ;
    }
}