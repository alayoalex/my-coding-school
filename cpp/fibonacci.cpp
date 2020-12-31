#include <bits/stdc++.h>

using namespace std;

int fibonacci(int n);
int dp[1000];

int main() {
    cout << fibonacci(4);
	memset(dp, -1, sizeof dp);
	return 0;
}

int fibonacci(int n) {
	if(dp[n] > 0) return dp[n];
	if (n == 1 || n == 2)
		return 1;
	dp[n] = fibonacci(n - 1) + fibonacci(n - 2);
	return dp[n];
}