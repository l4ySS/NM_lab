# Лабораторная 1 
## Метод прогонки решения разреженных матриц специального вида
Матрица, где x обозначает произвольные ненулевые элементы, а 0 — нули

x x x x x x x x x x x x x
x x x 0 0 0 0 0 0 0 0 0 0
0 x x x 0 0 0 0 0 0 0 0 0
0 0 x x x 0 0 0 0 0 0 0 0
0 0 0 x x x 0 0 0 0 0 0 0
0 0 0 0 x x x 0 0 0 0 0 0
0 0 0 0 0 x x x 0 0 0 0 0
0 0 0 0 0 0 x x x 0 0 0 0
0 0 0 0 0 0 0 x x x 0 0 0
0 0 0 0 0 0 0 0 x x x 0 0
0 0 0 0 0 0 0 0 0 x x x 0
0 0 0 0 0 0 0 0 0 0 x x x
x x x x x x x x x x x x x

# Лабораторная 2
## LU-разложение симметричных матриц ленточного вида

Вид матрицы:
x x 0 0 0 0 0 0 0 0 0 0 0
x x x 0 0 0 0 0 0 0 0 0 0
0 x x x 0 0 0 0 0 0 0 0 0
0 0 x x x 0 0 0 0 0 0 0 0
0 0 0 x x x 0 0 0 0 0 0 0
0 0 0 0 x x x 0 0 0 0 0 0
0 0 0 0 0 x x x 0 0 0 0 0
0 0 0 0 0 0 x x x 0 0 0 0
0 0 0 0 0 0 0 x x x 0 0 0
0 0 0 0 0 0 0 0 x x x 0 0
0 0 0 0 0 0 0 0 0 x x x 0
0 0 0 0 0 0 0 0 0 0 x x x
0 0 0 0 0 0 0 0 0 0 0 x x

При этом размерность ленты может быть произвольная.
В памяти хранится только диагональ и элементы выше диагонали. Т.е. при задаче с матрицей размерности NxN и длиной ленты L для вычислений используется матрица размерности Nx(L mod 2 + 1)

# Лабораторная 3 
## Метод вращений Якоби определения всех собственных значений

# Лабораторная 4

# Лабораторная 5 

# Лабораторная 6
