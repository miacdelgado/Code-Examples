#include <iostream>
using namespace std;

int main() {
	int layers = 0;
	cout << "Enter the height of your card pyramid: ";
	cin >> layers;
    cout << layers;
	cout << endl << endl;
	for (int i = 0; i < layers*2; i+=2) {
		for (int j = 0; (layers-i/2)-1 > j; j++) {
			cout << " ";
		}
		for (int k = 0; k < i+2; k++) {
			if (k % 2 == 0) {
				cout << "/";
			}
			else {
				cout << "\\";
			}
		}
		cout << endl;
	}
	cout << endl;
	return 0;
}