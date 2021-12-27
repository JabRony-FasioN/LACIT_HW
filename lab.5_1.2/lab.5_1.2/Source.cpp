#include <iostream>
#include<string>
#include <memory>
#include<cmath>
using namespace std;
/*
class Learner
{
public:
    virtual const char* name() const noexcept = 0;
};

class Schooler : public Learner
{
public:
     const char* name() const noexcept override final { return "Школьник"; };
};

class Student : public Learner
{
public:
     const char* name() const noexcept override final { return "Студент"; };
};

int main()
{
    setlocale(LC_ALL, "rus");
    const unique_ptr<Learner> arr[] = {
        make_unique<Schooler>(),
        make_unique<Student>(),
        make_unique<Schooler>(),
        make_unique<Student>()
    };
    for (const auto& p : arr)
        cout << p->name() << endl;
}

*/
//////////////////////////////////////////////////////

/*
class Animal
{
protected:
	string name;
public:
	Animal(string name) : name(name){}

	virtual void Say() = 0;
	virtual void Nick() = 0;
};

class Dog : public Animal
{
public:
	Dog(string name) : Animal(name){}

	void Say()
	{
		cout << name << " speak gav-gav" << endl;
	}
	void Nick()
	{
		cout << name << " name Dog_1" << endl;
	}
};

class Cat : public Animal
{
public:
	Cat(string name) : Animal(name){}

	void Say()
	{
		cout << name << " speak may-may" << endl;
	}
	void Nick() 
	{
		cout << name << " name Cat_1" << endl;
	}
};

class Bird : public Animal
{
public:
	Bird(string name) : Animal(name){}

	void Say() override
	{
		cout << name << " speak kray-kray" << endl;
	}
	void Nick() override
	{
		cout << name << " name Bird_1" << endl;
	}
};


int main()
{
	
	Dog dog("Dog");
	Cat cat("Cat");
	Bird bird("Bird");

	reference_wrapper<Animal> animals[3] = {
	  dog,
	  cat,
	  bird
	};


	for (int i = 0; i < 3; ++i)
	{
		((Animal&)(animals[i])).Say();
		((Animal&)(animals[i])).Nick();
		
	}

	system("pause");
	return 0;
}
*/
//////////////////////////////////////////////////////
/*
class Polygon {
public:
	double x1, y1, x2, y2, x3, y3;
public:
	void show(double aim1, double aim2) {
		cout << "(" << aim1 << "," << aim2 << ")" << endl;
	}
	//virtual void get_P(){}
	//virtual void get_S(){}

};

class Triangle : public Polygon {
public:
	Triangle(double q1, double q2, double q3, double q4, double q5, double q6) {
		x1 = q1; x2 = q3; x3 = q5;
		y1 = q2; y2 = q4; y3 = q6;
	}
	

	void dot_cross() {
		double aim_x = (x1 + x2 + x3) / 3;
		double aim_y = (y1 + y2 + y3) / 3;
		show(aim_x, aim_y);
	}
	void med_lenght() {
		int point;
		cout << "1-A,2-B,3-C" << endl;
		cin >> point;
		if (point == 1)
		{
			double x = (x2 + x3) / 2;
			double y = (y2 + y3) / 2;
			double aim = pow(x1 - x, 2) + pow(y1 - y,2);
			cout << sqrt(aim) << endl;
		} 
		else if (point == 2) {
			double x = (x1 + x3) / 2;
			double y = (y1 + y3) / 2;
			double aim = pow(x2 - x, 2)+ pow(y2 - y, 2);
			cout << sqrt(aim) << endl;
		}
		else if (point == 3) {
			double x = (x1 + x2) / 2;
			double y = (y1 + y2) / 2;
			double aim = pow(x3 - x, 2) + pow(y3 - y, 2);
			cout << sqrt(aim) << endl;
		}
		else {exit(0);}
	}
	void biss_lenght() {
		int point;
		cout << "1-A,2-B,3-C" << endl;
		cin >> point;
		double a = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
		double b = sqrt(pow(x3 - x1, 2) + pow(y3 - y1, 2));
		double c = sqrt(pow(x3 - x2, 2) + pow(y3 - y2, 2));
		if (point ==1)
		{
			cout << sqrt((b * c) * (a + b + c) * (b + c - a)) / b + c << endl;
		}
		else if (point == 2) {
			cout << sqrt((a * c) * (a + b + c) * (b - c + a)) / a + c << endl;
		}
		else if (point == 3) {
			cout << sqrt((b * a) * (a + b + c) * (a + c - b)) / b + a << endl;
		}
		else { exit(0);}
	}
	void biss_dot() {
		double a = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
		double b = sqrt(pow(x3 - x1, 2) + pow(y3 - y1, 2));
		double c = sqrt(pow(x3 - x2, 2) + pow(y3 - y2, 2));
		
		double x = (x1 + x2 + x3) / (a + b + c);
		double y = (y1 + y2 + y3) / (a + b + c);
		show(x, y);
	}
};


void main() {
	//setlocale(LC_ALL, "rus");
	Triangle obj(10,20,310,4.6,5.1,6.5);
	obj.biss_lenght();

}
*/