#include <iostream>
using namespace std;
int main() {
    const double gRt[] = {0.38, 0.91, 0.38, 2.34, 1.06, 0.92, 1.19, 0.06};
    const string cBd[] = {"Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"};
    double eWeight;
    cin >> eWeight;
    if(eWeight <1){
        for (int i = 0; i < 999; i++) {
        cout <<cBd[8];
    }
        return 1;
    }
    cout << "Your weight on different celestial bodies would be:\n\n";
    for (int i = 0; i < 8; i++) {
        double weightOn = eWeight * gRt[i];
        cout <<cBd[i] << " :  " << weightOn << " kg\n\n";
    }

    return 0;
}