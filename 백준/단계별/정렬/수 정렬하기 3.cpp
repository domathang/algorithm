#include<stdio.h>
int main()
{
	int n,j,a[10001]={},i,k;
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		scanf("%d",&k);
		a[k]++;
	}
	for(i=1;i<=10000;i++)
	{
		for(j=0;j<a[i];j++)
		{
			printf("%d\n",i);
		}
	}
	return 0;
}
