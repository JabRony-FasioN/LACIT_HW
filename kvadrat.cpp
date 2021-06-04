#include<iostream>
#include<cmath>
using namespace std;


class CSquare {
public:
	double a;
	double D;
	double P;
	double S;
	
	CSquare() {
		 a = D = P = S = 0;
	}
public:
	void get() {
		cout << "Введите сторону квадрата" << endl;
		cin >> a;
	}

	void dia() {
		D = sqrt(pow(a, 2) + pow(a, 2));
	}

	double s() {
	return	S = a * a;
	}

	void p() {
		P = 4 * a;
	}

	void show_dia() {
		cout << "Длина диагонали == " << D << endl;
	}

	void show_s() {
		cout << "площадь == " << S << endl;
	}

	void show_p() {
		cout << "Периметр == " << P << endl;
	}

	
};

class Pyramid : public CSquare {
public :
	double h;
	double H;
	double center;
	double V;
	double PYR_S;
	double side;
	Pyramid() {
		side=PYR_S = h = H = center = V = 0;
	}
	//Pyramid();
	//Pyramid(double a, double D, double S, double P);

	void geth() {
		cout << "введите h" << endl;
		cin >> h;
	}

	double getCenter() {
		return center = sqrt(pow(D / 2, 2) - pow(a / 2, 2));
	}
	
	double getH() {
		return H = sqrt(pow(h, 2) - pow(center, 2));
	}

	double exV() {
		return V =  (S * H)/3;
	}
	
	void showV() {
		cout << "обьем пирамиды  " << V << endl;
	}

	double get_side() {
		return side = sqrt(pow(H, 2) + pow(D / 2,2));
	}

	double getPYR_S(){
		return PYR_S = pow(a, 2) + 2 * a * sqrt(pow(side, 2) - pow(a / 2, 2));
	}
};

int main() {
	setlocale(0, "");
	/*CSquare first;
	first.get();
	first.dia();
	first.show_dia();
	first.s();
	first.show_s();
	first.p();
	first.show_p();
	*/

	
	Pyramid second;
	second.get();
	second.dia();
	second.show_dia();
	second.s();
	second.show_s();
	second.p();
	second.show_p();
	second.geth();
	second.getCenter();
	second.getH();
	second.exV();
	second.showV();

	cout << "/////////////////////////////////////////" << endl;
	
	//a)
	const int n_kvadrat = 5;
	double eq=0;
	//cout << "количество кубов" << endl;
	//cin >> n_kvadrat;
	CSquare kvad_arr[n_kvadrat];
	for (int i = 0; i < n_kvadrat; i++)
	{
		kvad_arr[i].get();
		eq = eq + kvad_arr[i].s();
		kvad_arr[i].show_s();
	}
	cout << "среднее значение:  " << eq / n_kvadrat << endl;

	//b)
	const int m_PYR = 3;
	Pyramid PYR_arr[m_PYR];
	double M = -INFINITY;
	double Max_index = -1;
	for (int i = 0; i < m_PYR; i++)
	{
		PYR_arr[i].get();
		PYR_arr[i].get_side();
		//PYR_arr[i].getPYR_S();
		if (PYR_arr[i].getPYR_S() > M)
		{
			M = PYR_arr[i].getPYR_S();
			Max_index = i;
		}
	}
	cout << "max element:  " << endl;
	
	system("pause");
	return 0;
}