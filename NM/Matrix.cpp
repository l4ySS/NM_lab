#pragma once
#include "Matrix.h"

Matrix::Matrix(Vector _a, Vector _b, Vector _c, Vector _p, Vector _q) : a(_a), b(_b), c(_c), p(_p), q(_q), size(b.getSize()) {

	a.setSize(size);
	a[1] = 0;
	for (int i = 2; i < size + 1; i++)
		a[i] = _a[i - 1];
};


int Matrix::getSize() {
	return size;
}


void Matrix::setSize(int _size) {
	size = _size;
}



Matrix Matrix::operator+=(Matrix A) {
	a += A.a;
	b += A.b;
	c += A.c;
	p += A.p;
	q += A.q;
	return *this;
}


Matrix Matrix::operator-=(Matrix A) {
	a -= A.a;
	b -= A.b;
	c -= A.c;
	p -= A.p;
	q -= A.q;
	return *this;
}


Matrix Matrix::operator =(Matrix A) {
	a = A.a;
	b = A.b;
	c = A.c;
	p = A.p;
	q = A.q;
	return *this;
}

Vector Matrix::multiply(Vector &A) {

	Vector temp(getSize());

	temp[1] = p.dotProduct(A);

	for (int i = 2; i < getSize(); i++)
	{
		temp[i] = a[i] * A[i - 1] + b[i] * A[i] + c[i] * A[i+1];
	}
	
	temp[5] = q.dotProduct(A);

	return temp;
}

std::ostream& operator<<(std::ostream& out, Matrix& M) {
	out << M.p << "\n";
	for (int i = 2; i < M.getSize(); i++)
	{
		for (int j = 0; j < i - 2; j++) out << "0\t";
		out << M.a[i] << "\t" << M.b[i] << "\t" << M.c[i] << "\t";
		for (int j = M.getSize(); j > i + 1; j--) out << "0\t";
		out << "\n";
	}

	out << M.q;
	return out;
};



std::istream& operator>>(std::istream& in, Matrix& M) {
	in >> M.size;
	//double** temp = new double*[M.size + 1];
	//for (int i = 0; i < M.size; i++)
	//	temp[i] = new double[M.size + 1];

	//for (int i = 0; i < M.size; i++)
	//	temp[i] = new double[M.size + 1];


	//for (int i = 1; i < M.size + 1; i++)
	//	M.p[i] = temp[0][i - 1];

	//for (int i = 2; i < M.size + 1; i++)
	//	M.a[i] = temp[i][i - 1];
	//
	//for (int i = 1; i < M.size + 1; i++)
	//	M.b[i] = temp[i][i];

	//for (int i = 1; i < M.size; i++)
	//	M.c[i] = temp[i][i+1];

	//for (int i = 1; i < M.size + 1; i++)
	//	M.q[i] = temp[M.size][i - 1];


	for (int i = 1; i < M.size + 1; i++)
		in >> M.p[i];
	
	M.b[1] = M.p[1];
	M.c[1] = M.p[2];

	for (int i = 2; i < M.size; i++)
	{
		in >> M.a[i] >> M.b[i] >> M.c[i];
	}

	for (int i = 1; i < M.size + 1; i++)
		in >> M.q[i];

	M.a[M.size] = M.q[M.size - 1];
	M.b[M.size] = M.q[M.size];

	return in;
};


void Matrix::read(std::string filename) {
	std::ifstream fin(filename);
	if (!fin.eof()) {
		fin >> *this;
	}
	fin.close();
};

void Matrix::write(std::string filename) {
	std::ofstream fout(filename);
	fout << *this;
	fout.close();
}



Vector Matrix::solution(Vector F) {
	double R;
	Vector r(size+1);
	r[2] = a[2];
	for (int i = 2; i < size; i++) {
		if (b[i] == 0) {
			std::cout << "Wrong matrix!\n";
			return F;
		}
		R = 1 / b[i];

		b[i] = 1;
		r[i] *= R;
		c[i] *= R;
		F[i] *= R;

	


		R = a[i + 1];
		a[i + 1] = 0;
		r[i + 1] = -R * r[i];
		b[i + 1] -= R * c[i];
		F[i + 1] -= R * F[i];


		R = p[i];
		p[i] = 0;
		p[1] -= R * r[i];
		p[i + 1] -= R * c[i];
		F[1] -= R * F[i];
	
		R = q[i];
		q[i] = 0;
		q[1] -= R * r[i];
		q[i + 1] -= R * c[i];
		F[size] -= R * F[i];
	}
		c[1] = p[2];		
		if (p[1] == 0) {
			std::cout << "Wrong matrix!\n";
			return F;
		};
		R = 1 / p[1];

		p[1] = 1;
		p[size] *= R;
		F[1] *= R;
	
		R = q[1];
		q[1] = 0;
		q[size] -= R * p[size]; 
		F[size] -= R * F[1];
	
		if (q[size] == 0) {
			std::cout << "Wrong matrix!\n";
			return F;
		};
		
		R = 1/q[size];
		q[size] = 1;
		b[size] = 1;
		F[size] *= R;
	
		R = p[size];
		p[size] = 0;
		F[1] -= q[size] * R;

		for (int i = 2; i < size; i++)	{
			R = r[i];
			r[i] = 0;
			F[i] -= R * F[size];
		}
		
		Vector x(size);
		x[size] = F[size];
		for (int i = size - 1; i >= 2; i--) {
			x[i] = F[i] - c[i] * x[i + 1];
		}
		x[1] = F[1] - p[size] * x[size];

		
	return x;
};




//
//Vector Matrix::algh(Vector F, Vector& X_star) {
//	double R;
//	Vector r(size + 1);
//	Vector F_star(size + 1, 1);
//	r[2] = a[2];
//	for (int i = 2; i < size; i++) {
//		if (b[i] == 0) {
//			std::cout << "Error";
//			return F;
//		}
//		R = 1 / b[i];
//
//		b[i] = 1;
//		r[i] *= R;
//		c[i] *= R;
//		F[i] *= R;
//		F_star[i] *= R;
//		//	std::cout.precision(3);
//		//	std::cout << *this << "\n\n" << F << "F * " << R << " \n\n\n";
//
//		R = a[i + 1];
//		a[i + 1] = 0;
//		r[i + 1] = -R * r[i];
//		b[i + 1] -= R * c[i];
//		F[i + 1] -= R * F[i];
//		F_star[i + 1] -= R * F_star[i];
//
//		R = p[i];
//		p[i] = 0;
//		p[1] -= R * r[i];
//		p[i + 1] -= R * c[i];
//		F[1] -= R * F[i];
//		F_star[1] -= R * F_star[i];
//
//		R = q[i];
//		q[i] = 0;
//		q[1] -= R * r[i];
//		q[i + 1] -= R * c[i];
//		F[size] -= R * F[i];
//		F_star[size] -= R * F_star[i];
//	}
//	c[1] = p[2];
//	if (p[1] == 0) {
//		std::cout << "Error";
//		return F;
//	};
//	R = 1 / p[1];
//
//	p[1] = 1;
//	p[size] *= R;
//	F[1] *= R;
//	F_star[1] *= R;
//
//	R = q[1];
//	q[1] = 0;
//	q[size] -= R * p[size];
//	F[size] -= R * F[1];
//	F_star[size] -= R * F[1];
//
//	R = 1 / q[size];
//	q[size] = 1;
//	b[size] = 1;
//	F[size] *= R;
//	F_star[size] *= R;
//
//	R = p[size];
//	p[size] = 0;
//	F[1] -= q[size] * R;
//	F_star[1] -= q[size] * R;
//
//	for (int i = 2; i < size; i++) {
//		R = r[i];
//		r[i] = 0;
//		F[i] -= R * F[size];
//		F_star[i] -= R * F_star[size];
//	}
//
//	Vector x(size);
//	x[size] = F[size];
//	for (int i = size - 1; i >= 2; i--) {
//		x[i] = F[i] - c[i] * x[i + 1];
//	}
//	x[1] = F[1] - p[size] * x[size];
//
//	X_star[size] = F_star[size];
//	for (int i = size - 1; i >= 2; i--) {
//		X_star[i] = F_star[i] - c[i] * X_star[i + 1];
//	}
//	X_star[1] = F_star[1] - p[size] * X_star[size];
//	Vector One(size + 1, 1);
//	X_star -= One;
//	std::cout << "\nEstim = " << X_star.norm() << "\n";
//	return x;
//};






//for (int i = 1; i < size; i++) {
//	//		if (b[i] == 0) return f;
//	R = 1 / b[i];
//	b[i] = 1;
//	p[i] = 1;
//	c[i] *= R;
//	f[i] *= R;
//	//		std::cout << "\ni =" << i << " b[i] = " << b << "\n\n";
//	//		std::cout << "\ni =" << i << " c[i] = " << c << "\n\n";
//	//		std::cout << "\ni =" << i << " f[i] = " << f << "\n\n";
//	R = a[i + 1];
//	a[i + 1] = 0;
//	b[i + 1] -= (R * c[i]);
//	f[i + 1] -= (R * f[i]);
//	//		std::cout << "\ni =" << i << " a[i] = " << a << "\n\n";
//	//		std::cout << "\ni =" << i << " b[i] = " << b << "\n\n";
//	//		std::cout << "\ni =" << i << " f[i] = " << f << "\n\n";
//	R = q[i];
//	q[i] = 0;
//	q[i + 1] -= (R * c[i]);
//	f[size] -= (R * f[i]);
//	//		std::cout << "\ni =" << i << " q[i] = " << q << "\n\n";
//	//		std::cout << "\ni =" << i << " f[i] = " << f << "\n\n";