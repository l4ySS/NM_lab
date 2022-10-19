#include "Vector.h"
#include <iostream>


Vector::Vector() {
	size = 0;
	nums = new double;
}

Vector::Vector(int _size) {
	size = _size;
	nums = new double[size+1];
	nums[0] = 0;
	for (int i = 1; i < size + 1; i++) nums[i] = 0;
}

Vector::Vector(double* _nums, int _size) {
	size = _size;
	nums = new double[size + 1];
	nums[0] = 0;
	for (int i = 1; i < _size + 1; i++)
		nums[i] = _nums[i-1];
}
Vector::Vector(int _size, double val) {
	size = _size;
	nums = new double[size + 1];
	nums[0] = 0;
	for (int i = 1; i < size + 1; i++) nums[i] = val;
};


double& Vector::operator[](int i)
{
	return nums[i];
}

double& Vector::operator[](int i) const
{
	return nums[i];
}

Vector::Vector(Vector& A) {
	size = A.getSize();
	nums = new double[size + 1];
	nums[0] = 0;
	for (int i = 1; i < size + 1; i++)
		nums[i] = A[i];

}



int Vector::getSize() {
	return size;
}

int Vector::getSize() const{
	return size;
}

void Vector::setSize(int _size) {
	size = _size;
}



Vector::~Vector() {
//	delete nums;
};


Vector Vector::operator+(Vector A) {
	Vector Temp;
	Temp.setSize(A.getSize());
	for (int i = 1; i < getSize() + 1; i++)
		Temp[i] = this->nums[i] + A[i];
	return Temp;
};


Vector Vector::operator-(Vector A) {
	Vector Temp;
	Temp.setSize(A.getSize());
	for (int i = 1; i < getSize() + 1; i++) 
		Temp[i] = this->nums[i] - A[i];
	return Temp;
}



Vector Vector::operator=(const Vector &A) {
	size = A.getSize();
	for (int i = 1; i < getSize() + 1; i++)
		nums[i] = A[i];
	return *this;
};

Vector Vector::operator+=(Vector A) {
	for (int i = 1; i < getSize() + 1; i++)
		nums[i] += A[i];
	return *this;
};



Vector Vector::operator-=(Vector A) {
	for (int i = 1; i < getSize() + 1; i++)
		nums[i] -= A[i];
	return *this;
}



double Vector::dotProduct(Vector A) {
	if (size != A.getSize()) return 0;
	double res = 0;
	
	for (int i = 1; i < getSize() + 1; i++)
		res += nums[i] * A[i];
	return res;
};

double Vector::norm(){
	double max = nums[1];
	for (int i = 1; i < getSize() + 1; i++)
		if (max < abs(nums[i])) max = abs(nums[i]);
	return max;
}

//double Vector::norm() {
//	double max;
//
//	if(nums[1] > 0) max = nums[1];
//	else max = nums[1]*( - 1);
//
//	for (int i = 1; i < getSize() + 1; i++)
//			if ((nums[i] > 0)&&(max < nums[i])) max = nums[i];
//			else if(max < (-1)*nums[i]) max = nums[i] *( - 1);
//
//	return max;
//}

std::ostream& operator<<(std::ostream& out, Vector& A) {
	int i = 1;
	for (i = 1; i < A.getSize() + 1; i++)
		out << A[i] << "\t";
	return out;
};

std::istream& operator>>(std::istream& in, Vector& A) {
	int i = 1;
	do {
		in >> A[i];
		i++;
	} while (in.get() != '\n');
	A.setSize(i);
	return in;
};


void Vector::read(std::string filename) {
	std::ifstream fin(filename);
	if (!fin.eof()) {
		int i = 0;
		while (fin >> nums[i+1]) i++;
		size = i;
	}
	fin.close();
};

void Vector::write(std::string filename) {
	std::ofstream fout(filename);
	for (int i = 1; i < size+1; i++)
		fout << nums[i];
	fout.close();
}

void Vector::randomFill(int a, int b) {
	for (int i = 1; i < size + 1; i++) {
		nums[i] = a + rand() % (b - a + 1);
	}
}