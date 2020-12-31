#include <stdio.h>

int main(){
	double a = 0.0, suma = 0.0;

	while (scanf("%lf", &a) != EOF){

		suma += a;
	}

	printf("$%.2lf\n", suma/12);
}
