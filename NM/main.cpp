#include "Vector.h"
#include "Matrix.h"

double relError(Vector A, Vector B, Vector C, Vector P, Vector Q, Vector X_corr);


void main(){
	//std::cout << "" << "";
	//std::cout << "" << "";
	//std::cout << "" << "";
	//std::cout << "" << "";
	//std::cout << "" << "";


	//int command;
	//std::cin >> command;
	//while(command != 0)
	//switch (command) {
	//case 1: 
	//	break;
	//case 2:
	//	break;
	//case 3:
	//	break;
	//default:
//	std::cout << abs(-2.3) << "\nWrong command!\n";
	
	double nums1[] = { 4, -1, -1, -1, -1 };
	double nums2[] = { -1, -1, -1, -1 };
	double nums3[] = { 4, 4, 4, 4, 4 };
	double nums4[] = { -1, -1, -1, -1 };
	double nums5[] = { -1, -1, -1, -1, 4 };

	double nums6[] = { 2, 3, 5, 8, 4 };
	double nums7[] = { 2, 3, 5, 8, 4 };
	Vector A(nums2, 5);

	Vector B(nums3, 5);
	Vector C(nums4, 5);
	Vector P(nums1, 5);
	Vector Q(nums5, 5);

	Vector F(nums6, 5);
	Vector X(nums6, 5);
	Vector X_star(nums7, 5);
	Vector L(nums6, 5);
	Matrix M(A, B, C, P, Q);
	std::cout << M << "\n\n";
	std::cout <<"Correct answer  = " << X << "\n\n";
	F = M.multiply(X);
	std::cout << "F = " << F << "\n\n";
	X = M.solution(F);
	std::cout << "Answer = " << X << "\n\n";
	std::cout  << "Error = "  << relError(A, B, C, P, Q, L);
}



double relError(Vector A, Vector B, Vector C, Vector P, Vector Q, Vector X_corr) {
	Matrix M(A, B, C, P, Q);
	Vector F(X_corr);
	Vector X(X_corr);
	Vector X_star(X_corr);
	F = M.multiply(X_corr);
	X = M.solution(F);
	X -= X_corr;
	return X.norm();
}