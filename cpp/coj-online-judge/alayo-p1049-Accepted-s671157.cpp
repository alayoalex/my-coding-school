/*
 * Ejercicio1000.c
 *
 *  Created on: sep 22, 2014
 *      Author: Alexei
 */

#include <stdio.h>

int main() {

	int a;

	scanf("%d", &a);

	if (a > 0) printf("%d", a*(a + 1)/2);
	else if (a < 0) printf("%d", (a*(a - 1)/2 - 1)*-1);
	else printf("%d", 0);
}
