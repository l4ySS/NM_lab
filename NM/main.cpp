#include "Vector.h"
#include "Matrix.h"

void main(){
	/*double nums1[] = { 1, 5, 3, 4, 5};
	double nums2[] = { 1, 2, 3, 2 };
	double nums3[] = { 1, 3, 4, 6, 7 };
	double nums4[] = { 5, 1, 1, 1 };
	double nums5[] = { 3, 3, 3, 2, 7 };
	double nums6[] = { 4, 2, 5, 2, 3 };*/
	double nums1[] = { 1, 5, 3, 4, 5 };
	double nums2[] = { 1, 2, 3, 2 };
	double nums3[] = { 1, 3, 4, 6, 7 };
	double nums4[] = { 5, 1, 1, 1 };
	double nums5[] = { 3, 3, 3, 2, 7 };
	double nums6[] = { 4, 2, 3, 5, 6 };

	Vector A(nums2, 5);
	Vector B(nums3, 5);
	Vector C(nums4, 5);
	Vector P(nums1, 5);
	Vector Q(nums5, 5);

	Vector F(nums6, 5);
	Vector K(nums6, 5);
	Vector L(nums6, 5);

	A.randomFill(1, 5);
	B.randomFill(1, 5);
	C.randomFill(1, 5);
	P.randomFill(1, 5);
	Q.randomFill(1, 5);
	Q[4] = A[5];
	P[2] = C[1];


	Matrix M(A, B, C, P, Q, F);
	Matrix M2(A, B, C, P, Q, F);
	std::cout << M;
//	std::cout << "kek3\n";
	//A[0] = 4;
	//std::cout << A << "\n";
	//A.setSize(20);
	//std::cout << A << "\n";
//	L = M.multiply(K);
	//std::cout << "kek4\n";
//	std::cout << F << "\n";
//	std::cout << "kek5\n";
//	std::cout << L << "\n";
	
//	M.read("input.txt");
//	M.write("output.txt");
	L = M.solution();
	std::cout << "\n" << "\n";

	std::cout << L << "\n\n\n";
	std::cout << M << "\n";
	std::cout << "kek" << "\n";
	K = M2.multiply(L);
	std::cout << K << "\n";


	//std::cout << "kek6\n";
//	std::cout << A.dotProduct(B);
}