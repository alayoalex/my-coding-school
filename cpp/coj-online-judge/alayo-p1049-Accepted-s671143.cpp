#include <stdio.h>

int main() {

	int a;

	scanf("%d", &a);

	int sum = 0;

	if (a > 0){
		for	(int i = 1; i <= a; i++){
			sum += i;
		}
		printf("%d\n", sum);
	}
	else if (a < 0){
		a = a*-1;
		for	(int i = 1; i <= a; i++){
			sum += i;
		}
		printf("%d\n", (sum*-1) + 1);
	}
	else printf("%d\n", 0);
}