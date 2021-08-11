#include<stdio.h>
int a[501][501];
int main()
{
	int n,max=0;
	scanf("%d",&n);
	scanf("%d",&a[1][1]);
	for(int i=2;i<=n;i++)
	{
		for(int j=1;j<=i;j++)
		{
			scanf("%d",&a[i][j]);
			a[i][j] += a[i-1][j] > a[i-1][j-1] ? a[i-1][j] : a[i-1][j-1];
		}
	}
	for(int i=1;i<=n;i++){
		if(max<a[n][i]) {
			max=a[n][i];
		}
	}
	printf("%d",max);
	return 0;
}
