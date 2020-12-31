/*
 * ejercicio1003.c
 *
 *  Created on: sep 16, 2014
 *      Author: Alexei
 */

#include <stdio.h>

int matrix[105][10];

int main() {

	int N;
	scanf ("%d", &N);

	for(int i = 0; i < N; i++) {
		int c, f;
		scanf ("%d %d", &c, &f);

		for(int j = 0; j < f; j++)
			for (int k = 0; k < c; k++)
				scanf ("%d", &matrix[j][k]);

		int maxima = 0, ganador = 0;
		for(int k = 0; k < c; k++) {
			int suma = 0;
			for(int j = 0; j < f; j++) {
				suma = suma + matrix[j][k];
			}

			if (suma > maxima) {
				maxima = suma;
				ganador = k;
			}
		}
		printf ("%d\n", ganador + 1);
	}

	return 0;
}
