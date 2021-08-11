#include <iostream>
using namespace std;

int main()
{
	int i,j,N,a[501]={},dp[501]={},tmp,max_len = 0;
	cin >> N;
	for(i=0; i<N; i++)
	{
		cin >> tmp;
		cin >> a[tmp];
	}
		
	for(i=1; i<501; i++)
	{
		if(a[i] == 0) continue;
		for(j=i-1; j>0; j--)
		{
			if(a[j] != 0 && a[i] > a[j] && dp[i] < dp[j])
			{
				dp[i] = dp[j];
			}
		}

		dp[i]++;
		if(max_len < dp[i]) max_len = dp[i];
	}
	if(max_len == 1) max_len=0;
	cout << N - max_len;
	return 0;
}
