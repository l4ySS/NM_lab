#pragma once
#include "Vector.h"
#include <iomanip>
class Matrix {
	Vector a, b, c, p, q;
	int size;
public:

	Matrix():a(),b(),c(),p(), q(), size(0) {};
	Matrix(Vector _a, Vector _b, Vector _c, Vector _p, Vector _q);
	int getSize();

	Vector getA();
	Vector getB();
	Vector getC();
	Vector getP();
	Vector getQ();

	void setA(Vector _A);
	void setB(Vector _B);
	void setC(Vector _C);
	void setP(Vector _P);
	void setQ(Vector _Q);

	Matrix operator+=(Matrix A);
	Matrix operator -=(Matrix A);
	Matrix operator =(Matrix A);
	
	Vector multiply(Vector& A);

	friend std::ostream& operator<<(std::ostream& out, Matrix& A);
	friend std::istream& operator>>(std::istream& in, Matrix& A);

	void read(std::string filename);
	void write(std::string filename);
	Vector solution(Vector &F, Vector Sol);

	void goodCondition(int lower_bracket, int upper_bracket, int _size);
	void badCondition(int lower_bracket, int upper_bracket, int _size);

	void test(Vector X, Vector r, Vector F);
private:
//	void print(Vector r);
};