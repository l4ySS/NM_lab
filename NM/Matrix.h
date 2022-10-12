#pragma once
#include "Vector.h"
class Matrix {
	Vector a, b, c, p, q, f;
	int size;
public:
	Matrix():a(),b(),c(),p(), q(), f(), size(0) {};
	Matrix(Vector _a, Vector _b, Vector _c, Vector _p, Vector _q, Vector _f);
	int getSize();
	void setSize(int _size);

	
	Matrix operator+=(Matrix A);
	Matrix operator -=(Matrix A);
	Matrix operator =(Matrix A);
	
	Vector multiply(Vector& A);

	friend std::ostream& operator<<(std::ostream& out, Matrix& A);
	friend std::istream& operator>>(std::istream& in, Matrix& A);

	void read(std::string filename);
	void write(std::string filename);
	Vector solution();
	
};