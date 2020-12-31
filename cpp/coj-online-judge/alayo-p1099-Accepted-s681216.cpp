
#include <stdio.h>

int main(){

	int a;
	while(scanf("%d", &a), a != 0){
		int b,c;
		scanf("%d %d", &b, &c);

		if ((a*a + b*b) == c*c)
			printf("right\n");
		else if ((a*a + c*c) == b*b)
			printf("right\n");
		else if ((b*b + c*c) == a*a)
			printf("right\n");
		else printf("wrong\n");
	}
}
