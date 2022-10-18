#pragma once
#include <iostream>
#include <fstream>
#include <ctime>
#include <math.h>

class Vector {
	int size;
	double* nums;
public:
	Vector();
	Vector(int _size);
	Vector(double* _nums, int _size); // 
	Vector(int _size, double val); // create Vector with _size and fill it with val
	double& operator[](int i);
	double& operator[](int i) const;
	
	Vector(Vector &A);
	int getSize();
	int getSize() const;
	void setSize(int _size);
	~Vector();
	

	Vector operator +(Vector A);
	Vector operator -(Vector A);
	Vector operator +(double A);
	Vector operator -(double A);
	Vector operator=(const Vector &A);
	Vector operator +=(Vector A);
	Vector operator +=(double A);
	Vector operator -=(Vector A);
	Vector operator -=(double A);
    double dotProduct(Vector A);
	double norm();

	friend std::ostream& operator<<(std::ostream& out, Vector& A);
	friend std::istream& operator>>(std::istream& in, Vector& A);

	void read(std::string filename);
	void write(std::string filename);

	void randomFill(int a, int b);
};