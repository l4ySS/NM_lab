#include "Vector.h"
#include "Matrix.h"

double relError(Vector A, Vector B, Vector C, Vector P, Vector Q, Vector X_corr);



void main() {
	srand(time(nullptr));

	//double nums1[] = { 5.2, 1.31, 1.3, 1.2, 1.6 };
	//double nums2[] = { 1.31, 1.2, 1.4, 1.6};
	//double nums3[] = { 5.2, 5.94, 5.64, 5.89, 5.99 };
	//double nums4[] = { 1.32, 1.12, 1.213, 1.212, 1.421 };
	//double nums5[] = { 1.9, 1.123, 1.111, 1.421, 5.99 };

	//double nums6[] = { 2.3, 3.1, 5.521, 8.532, 4.132 };

	int size = 3125;
	//Vector A(size);
	//Vector B(size);
	//Vector C(size);
	//Vector P(size);
	//Vector Q(size);
	//Vector L(size);


	Matrix M;
	
	M.goodCondition(-10, 10, size);

//	std::cout << M << "\n\n";
	Vector X_corr(size);
	X_corr.random(1, 5);
	Vector F(size);
	F = M.multiply(X_corr);
	Vector X(size);
	X = M.solution(F, X_corr);
	X -= X_corr;
	std::cout  << "Error(X) = "  << X.norm() << "\n";


	//std::cout << "Error(X) = " << relError(A, B, C, P, Q, L) << "\n";
	/*	A.random(1, 5);
		B.random(1, 5);
		C.random(1, 5);
		P.random(1, 5);
		Q.random(1, 5);*/

	//	B[1] = P[1];
	//	C[1] = P[2];
	//	A[size-1] = Q[size - 1];
	//	B[size] = Q[size];
	//
	//	//std::cout << A << "\n" << B << "\n" << C << "\n" << P << "\n" << Q << "\n\n";
		
	//	Vector F_theor(size);
	
	//	Vector X_corr(size);
	//	Vector L(size);
	//	Vector Y(size);
	//
	//
	//	X.random(1, 5);
	//	F.random(1, 5);
	//	F_theor.random(1, 5);
	//	L.random(1, 5);
		
	//	X_corr = X;
	//	std::cout << M << "\n\n";
	//
	////	std::cout <<"Correct answer  = " << X << "\n\n";
	//	F = M.multiply(X);
	//	F_theor = F;
	////	std::cout << "F = " << F << "\n\n";
	//	Y = M.solution(F, X);
	//	X = Y - X_corr;
	//	std::cout  << "Error(X) = "  << X.norm() << "\n";
	//	F_theor = M.multiply(Y);
	////	std::cout << std::setprecision(40) <<"Theor = " << F_theor << "\n\nFact  = " << F << " \n\n\n";
	//	F -= F_theor;
	//	std::cout << "Error(F) = " << F.norm() << " \n\n\n";
	////	std::cout << "Answer = " << X << "\n\n";
	////	relError(A, B, C, P, Q, L);
}


double relError(Vector A, Vector B, Vector C, Vector P, Vector Q, Vector X_corr) {
	Matrix M(A, B, C, P, Q);
	std::cout << M << "\n\n";
	std::cout << "Correct answer  = " << X_corr << "\n\n";
	Vector F(X_corr);
	Vector X(X_corr);
	Vector X_star(X_corr);
	F = M.multiply(X_corr);
	std::cout << "F = " << F << "\n\n";
	X = M.solution(F, X);
	X -= X_corr;
	return X.norm();
}


//double nums1[] = { 5, 1, 1, 1, 1 };
	//double nums2[] = { 1, 1, 1, 1 };
	//double nums3[] = { 5, 5, 2, 5, 5 };
	//double nums4[] = { 1, 1, 1, 1 };
	//double nums5[] = { 1, 1, 1, 1, 5 };
	//double* nums1 = new double[5];
	//double* nums2 = new double[5];
	//double* nums3 = new double[5];
	//double* nums4 = new double[5];
	//double* nums5 = new double[5];
	//	double nums6[] = { 2, 3, 5, 8, 4 };