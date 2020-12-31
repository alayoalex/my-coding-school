//============================================================================
// Name        : hm.cpp
// Author      : Alexei
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <bits/stdc++.h>

using namespace std;

//typedef pair<int, int> pii;
//const double pi = 2 * acos(0);
//#define FOR(i,a,n) for(int i = a; i < n; i++)
const int MAX = 1e9 + 7;

int fibonacci(int n);
int dp[1000];

int main() {
//	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
//	vector<int> v;
//	for(int i = 0; i < 10; i++) {
//		int n = rand();
//		cout << n << " ";
//		v.push_back(n);
//	}
//	cout << endl;
//	sort(v.begin(), v.end());
//	for(int i = 0; i < 10; i++) {
//		cout << v[i] << " ";
//	}
//	vector<int>::iterator it = lower_bound(v.begin(), v.end(), 28000);
//	cout << endl << *it << " " << (it - v.begin());

//
//	int arr[] = { 1, 2, 3, 4, 5 };
//	do {
//		for(int i = 0; i < 5; i++)
//			cout << arr[i] << " ";
//		cout << endl;
//	} while(next_permutation(arr, arr + 5));
//
//	cout << atan2(2, 0) * 180 / pi << "\n";
	/*for(int i = 2; i < MAXN; i++) if(!mk[i])
	{
		for(int j = i * i; j < MAXN; j += i) mk[j] = true;
		primos.push_back(i);
	}
	pii p;

//	for(int i = 0; i < primos.size(); i++) cout << bin(primos[i]) << endl;
*/
//	FOR(i,50,100) cout << i << endl;
	cout << fibonacci(4);
	memset(dp, -1, sizeof dp);
	return 0;
}

int fibonacci(int n) {
	if(dp[n] != -1) return dp[n];
	if (n == 1 || n == 2)
		return 1;
	dp[n] = fibonacci(n - 1) + fibonacci(n - 2);
	return dp[n];
}
