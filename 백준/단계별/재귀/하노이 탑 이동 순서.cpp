#include<stdio.h>
#include<math.h>
int cnt;
void hanoi(int n,int a,int b)
{
	cnt++;
	int c;
	
	if(n<=1)
	{
		printf("%d %d\n",a,b);
	}
	else
	{
		c=6-a-b;
		
		hanoi(n-1,a,c);
		printf("%d %d\n",a,b);
		hanoi(n-1,c,b);
	}
}
int main()
{
	int n;
	scanf("%d",&n);
	printf("%.0lf\n",pow(2,n)-1);
	hanoi(n,1,3);
	return 0;
}
