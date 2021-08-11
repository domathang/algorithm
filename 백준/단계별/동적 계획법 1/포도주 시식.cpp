#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	int n,arr[10000]={},dp[10000][2]={},i;
	cin >> n;
	for(i=0; i<n; i++){
		cin >> arr[i];
	}
	// dp[][0] : ÃÖ´ñ°ª 	dp[][1] :  µÎ Ä­ ¶³¾îÁø ¾Ö¶û ´õÇÑ °ª
	dp[0][0] = arr[0];
	dp[1][0] = arr[0] + arr[1];
	dp[2][0] = arr[2] + max(arr[0], arr[1]);
	dp[2][1] = arr[2];

	for(i=3; i<n; i++) {
		dp[i][0] = arr[i] + max(dp[i-1][1], max(dp[i-2][0], dp[i-3][0] + arr[i-1]));
		dp[i][1] = arr[i] + dp[i-3][0];
	}
	
	cout << max(dp[n-1][0], dp[n-2][0]);
	return 0;
}
