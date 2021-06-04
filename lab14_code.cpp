//#include "Header.h"
#include<iostream>
#include<math.h>
#include <conio.h>

using namespace std;

class  Straight {
	public:
		double x1, y1, x2, y2;
	public:		
		Straight(double x1, double y1, double x2, double y2) : x1(x1), y1(y1), x2(x2), y2(y2) {
			X();
			Y();
		};

	public:

	double k() {
		return  (y2 - y1) / (x2 - x1);
	}
	
	double index1() {
		return x2 - x1;
	}
	double index2() {
		return y2 - y1;
	}

	bool operator || (Straight& straight2) {
		double pres = 0.000000000001;
		return abs(abs(k()) - abs(straight2.k())) < pres;
	}

	bool operator != (Straight& straight2) {
		//return  k() == straight2.k();
		return (index1() * straight2.index1()) + (index2() * straight2.index2()) == 0 ;
	}
	
	void X() {
		cout << "по Y:  " << y1 - (x1*(y2-y1))/(x2-x1) << endl;
	}

	void Y() {
		cout << "по X:  " << (x1 - ((x2 - x1) * y1) / (y2 - y1)) << endl;
	}
};

int main() {
	setlocale(0, "");
	Straight straight1(1, 1, 1, 3);
	Straight straight2(0, 2, 1, 2);

	if (straight1 || straight2)
		cout << "are parallel" << endl;
	else
		cout << "are not parralel" << endl;

	if (straight1 != straight2)
		cout << "are perpendicular" << endl;
	else
		cout << "are not perpendicular" <<  straight1.k() << endl;

	system("pause");
	return 0;
}

