#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
	int n,m,i,j,sum=0,a[101]={};
	scanf("%d %d",&n,&m);
	for(i=0;i<n;i++)
		scanf("%d",&a[i]);
	
	for(i=0;i<n;i++)
	{
		for(j=i+1;j<n;j++)
		{
			for(int l=i+2;l<n;l++)
			{
				if(i!=j && j!=l && l!=i && sum<a[i]+a[j]+a[l] && a[i]+a[j]+a[l]<=m)
				{
					sum=a[i]+a[j]+a[l];
				}
			}
		}
	}
	printf("%d\n",sum);
	return 0;
}
