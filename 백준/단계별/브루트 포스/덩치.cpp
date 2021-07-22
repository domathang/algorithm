#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
	int a[51]={},b[51]={};
	int i,j,t,k;
	scanf("%d",&t);
	for(i=0;i<t;i++)
		scanf("%d %d",&a[i],&b[i]);
	for(i=0;i<t;i++)
	{
		k=0;
		for(j=0;j<t;j++)
		{
			if( i!=j && a[i]<a[j] && b[i]<b[j])
			k++;
		}
		printf("%d ",k+1);
	}
	
	return 0;
}
