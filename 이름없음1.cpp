#include <bits/stdc++.h>

using namespace std;

int weight[101], value[101], dp[101][100001];

int main()
{
	int n, k;
	
	cin >> n >> k;
	
	for(int i=1; i<=n; i++) {
		cin >> weight[i] >> value[i];
	}
	
	for(int i=1; i<=n; i++) {
		for(int j=1; j<=k; j++) {
			if( j - weight[i] >= 0 ) {
				dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + value[i]);
			} else {
				dp[i][j] = dp[i-1][j];
			}
		}
	}
	for(int i=1; i<=n; i++) {
		for(int j=1; j<=k; j++) {
			cout << dp[i][j] << " " ;
		}
		cout << '\n';
	}
	
	cout << dp[n][k];
}
