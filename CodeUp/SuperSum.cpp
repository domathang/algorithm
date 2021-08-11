#include <stdio.h>
int dp[15][15];

int supersum(int k, int n)
{
	int sum=0;
	
	if( k == 0 )
		return n;
		
	for(int i=1; i<=n; i++)
	{
		if(dp[k][i] == 0)  {
			dp[k][i] = supersum(k-1, i);
		}
			
		sum += dp[k][i];
	}
	return sum;
}

int main()
{
	int k,n;
	while( scanf("%d %d", &k, &n) != EOF )
		printf("%d\n", supersum(k, n));
	return 0;
}
