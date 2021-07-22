#include<stdio.h>

int a[7000][7000];

void f(int s,int e,int s1,int e1)
{
	int i,j,cnt;

	cnt=0;
	
	if(e-s==3) {
		for(i=s; i<e; i++)
		{
			for(j=s1; j<e1; j++)
			{
				cnt++;
				if(cnt!=5) a[i][j]=1;
			}
		}
	}
	else {
		for(i=s; i<e; i+=(e-s)/3)
		{
			for(j=s1; j<e1; j+=(e1-s1)/3)
			{
				cnt++;
				if(cnt!=5) f(i, i+(e-s)/3, j, j+(e1-s1)/3);
			}
		}
	}
	
}

int main()
{
	int n,i,j;
	scanf("%d",&n);
	
	f(0,n,0,n);
	
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			if(a[i][j] == 1) printf("*");
			else printf(" ");
		}
		printf("\n");
	}
	return 0;
}
