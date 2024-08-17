#include <iostream>
#include <cstdlib>
#include <ctime>
#include <random>
using namespace std;

		class rps_game {
			public:
				int user_input, ai_input;
				
			
void user_choise() {
	cin>>user_input;
}
void user_return() {
	if(user_input==1) {
		cout<< "user choosed rock\n";
	}
	else if(user_input==2) {
		cout<< "user choosed scissor\n";
	}
	else if(user_input==3) {
		cout<< "user choosed paper\n";
	}
	else {
		cout<< "error, try again\n";
	}
}

void ai_choise() {
	srand(time(NULL));

	ai_input = rand()% 3 + 1;
}

void ai_return() {
	if(ai_input==1) {
		cout<< "ai choosed rock\n";
	}
	else if(ai_input==2) {
		cout<< "ai choosed scissor\n";
	}
	else if(ai_input==3) {
		cout<< "ai choosed paper\n";
	}
	else {
		cout<< "error, try again\n";
	}
}

void raund() {
	cout<< "result: ";
	
	if(user_input==1 && ai_input==3) {
		cout<<"ai win"<<endl;
	}
	else if(user_input==2 && ai_input==1) {
		cout<<"ai win"<<endl;
	}
	else if(user_input==3 && ai_input==2) {
		cout<<"ai win"<<endl;
	}
	else if(user_input==3 && ai_input==1) {
		cout<<"You win"<<endl;
	}
	else if(user_input==1 && ai_input==2) {
		cout<<"You win"<<endl;
	}
	else if(user_input==2 && ai_input==3) {
		cout<<"You win"<<endl;
	}
	else {
		cout<<"its draw"<<endl;
	}
	}
	
};

void launch() {
	
	rps_game*a1=new rps_game;
	a1->user_choise();
	a1->user_return();
	a1->ai_choise();
	a1->ai_return();
	a1->raund();
}

int main() {
	
   launch();
   return 0;
}