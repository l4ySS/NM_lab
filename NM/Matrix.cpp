#pragma once
#include "Matrix.h"

Matrix::Matrix(Vector _a, Vector _b, Vector _c, Vector _p, Vector _q) : a(_a), b(_b), c(_c), p(_p), q(_q), size(b.getSize()) {

	a.setSize(size);
	a[1] = 0;
	for (int i = 2; i < size + 1; i++)
		a[i] = _a[i - 1];
};


Vector Matrix::getA() {
	return a;
}

Vector Matrix::getB() {
	return b;
}

Vector Matrix::getC() {
	return c;
}

Vector Matrix::getP() {
	return p;
}

Vector Matrix::getQ() {
	return q;
}


void Matrix::setA(Vector _A) {
	a.setSize(_A.getSize());
	a[1] = 0;
	for (int i = 2; i < size + 1; i++)
		a[i] = _A[i - 1];
}

void Matrix::setB(Vector _B) {
	b = _B;
}
void Matrix::setC(Vector _C) {
	c = _C;
}

void Matrix::setP(Vector _P) {
	p = _P;
}

void Matrix::setQ(Vector _Q) {
	q = _Q;
}




int Matrix::getSize() {
	return size;
}

void Matrix::goodCondition(int lower_bracket, int upper_bracket, int _size) {
	Vector A(_size);
	Vector B(_size);
	Vector C(_size);
	Vector P(_size);
	Vector Q(_size);

	A.random(lower_bracket, upper_bracket - lower_bracket);
	B.random(upper_bracket - lower_bracket, upper_bracket);
	C.random(lower_bracket, upper_bracket - lower_bracket);
	P.random(lower_bracket, upper_bracket - lower_bracket);
	Q.random(lower_bracket, upper_bracket - lower_bracket);


	P[1] = B[1];
	C[1] = P[2];
	A[_size - 1] = Q[_size - 1];
	Q[_size] = B[_size];


	Matrix M(A, B, C, P, Q);
	*this = M;
};

void  Matrix::badCondition(int lower_bracket, int upper_bracket, int _size) {
	Vector A(_size);
	Vector B(_size);
	Vector C(_size);
	Vector P(_size);
	Vector Q(_size);

	A.random(lower_bracket, upper_bracket - lower_bracket);
	B.random(upper_bracket - lower_bracket, upper_bracket);
	C.random(lower_bracket, upper_bracket - lower_bracket);
	P.random(lower_bracket, upper_bracket - lower_bracket);
	Q.random(lower_bracket, upper_bracket - lower_bracket);


	P[1] = B[1];
	C[1] = P[2];
	A[_size - 1] = Q[_size - 1];
	Q[_size] = B[_size];


	Matrix M(A, B, C, P, Q);
	*this = M;
};

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
	size = A.size;
	return *this;
}

Vector Matrix::multiply(Vector &A) {

	Vector temp(getSize());

	temp[1] = p.dotProduct(A);

	for (int i = 2; i < getSize(); i++)
	{
		temp[i] = a[i] * A[i - 1] + b[i] * A[i] + c[i] * A[i+1];
	}
	
	temp[getSize()] = q.dotProduct(A);

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

//void Matrix::print(Vector r) {
//	
//	std::cout << p << "\n";
//	for (int i = 2; i < getSize(); i++)
//	{
//		std::cout << r[i] << "\t";
//		for (int j = 1; j < i - 2; j++) std::cout << "0\t";
//		std::cout << a[i] << "\t" << b[i] << "\t" << c[i] << "\t";
//		for (int j = getSize(); j > i + 1; j--) std::cout << "0\t";
//		std::cout << "\n";
//	}
//
//	std::cout << q;
//}

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

Vector Matrix::solution(Vector &F, Vector Sol) {
	if ((p[1] == 0) || (q[size] == 0)) {
		std::cout << "Wrong matrix!\n";
		return F;
	};
	double R;
	Vector r(size + 1);
	r[2] = a[2];

	for (int i = 2; i < size; i++) {
		if (b[i] == 0) {
			std::cout << "Wrong matrix!\n";
			return F;
		}
	//	std::cout << "\n\n############\n I = " << i << "\n############\n\n";
		R = 1 / b[i];

		b[i] = 1;
		r[i] *= R;
		c[i] *= R;
		F[i] *= R;
		if ( i == 2) a[2] = r[2];


		R = a[i + 1];
		a[i + 1] = 0;
		r[i + 1] = -R * r[i];
		b[i + 1] -= R * c[i];	

		

		F[i + 1] -= R * F[i];
	


		if (i == size - 1) {
			q[1] += r[i + 1];
			q[size] = b[i + 1];
			q[size - 1] = 0;
			}

		

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



		if (i == size - 2) {
			a[size] = q[size - 1];
		}

	
	}



	c[1] = p[2];

	R = 1 / p[1];
	p[1] = 1;
	p[size] *= R;
	F[1] *= R;


	R = q[1];
	q[1] = 0;
	q[size] -= R * p[size];
	F[size] -= R * F[1];
	r[size] = 0;


	R = 1 / q[size];
	q[size] = 1;
	b[size] = 1;
	F[size] *= R;

	R = p[size];
	p[size] = 0;
	F[1] -= F[size] * R;


	for (int i = 2; i < size; i++) {
		R = r[i];
		r[i] = 0;
		F[i] -= R * F[1];
	}
	a[2] = r[2];

	

	Vector x(size);
	x[size] = F[size];
	for (int i = size - 1; i >= 1; i--) {
		x[i] = F[i] - c[i] * x[i + 1];
	}

	
return x;
};


void Matrix::test(Vector X, Vector r, Vector F) {
	Vector temp(X.getSize());
	Vector t;
	temp[1] = p.dotProduct(X);
	a[2] = r[2];


	for (int i = 2; i < getSize(); i++)
	{
		temp[i] = a[i] * X[i - 1] + b[i] * X[i] + c[i] * X[i + 1];
	}

	
	for (int i = 3; i < getSize(); i++) temp[i] += r[i] * X[1];

	temp[size] = q.dotProduct(X);
//	std::cout << "Theor = " << temp << "\n\nFact  = " << F << " \n\n";
	t = F - temp;
	std::cout << "Error(f) = " << t.norm() << "\n\n\n\n";

};

//
// 	std::cout << std::setprecision(3) << *this << "\n\n";
		//	std::cout << "r = " << r << "\n\n";
//test(Sol, r, F);
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