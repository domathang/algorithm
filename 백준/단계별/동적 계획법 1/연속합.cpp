#include <iostream>
#include <algorithm>

using namespace std;

int a[100000], dp[100000];

int main()
{
	int n;
	cin >> n;
	
	for(int i=0; i<n; i++) {
		cin >> a[i];
	}
	
	int ans = dp[0] = a[0];
	for(int i=1; i<n; i++) {
		dp[i] = max(a[i], dp[i-1] + a[i]);
		if(ans < dp[i]) ans = dp[i];
	}
	
	cout << ans;
}
