#include<stdio.h>
int main()
{
	int i,j,n,m,ch=0,cnt=0;
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		scanf("%d",&m);
		ch=0;
		if(m==1) ch=1;
		
		else if(m==3||m==5) ch=0;
		
		else
		for(j=2;j<=m/2;j++)
		{
			if(m%j==0){
				ch=1;
				break;
			}
		}
		if(ch==0) cnt++;
	}
	printf("%d\n",cnt);
	return 0;
}
