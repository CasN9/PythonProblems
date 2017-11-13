#include <iostream>
#include <vector>
#include <string>
#include <fstream>
using namespace std;

int main() {

	cout << "Hello world!" << endl;

	const double PI = 3.1415926535;

	char myGrade = 'A';

	bool isHappy = true;

	int myAge = 19;

	float favNum = 3.141592;

	double otherFavNum = 1.6180339887;

	cout << "Favourite Number: " << favNum << endl;

	//sizeof returns size of a data type in bytes
	cout << "Size of int " << sizeof(myAge) << endl;

	int five = 5;
	five += 6; //the same as: five = five + 6;

	// ++ and -- are increments/decrements respectively
	cout << "5++ = " << five++ << endl;	//returns 5
	cout << "++5 = " << ++five << endl;	//returns 7
	cout << "5-- = " << five-- << endl;	//returns 7
	cout << "--5 = " << --five << endl;	//returns 5

	cout << "4 / 5 = " << (float) 4/5 << endl; // known as casting - changing data types




	return 0;

}
