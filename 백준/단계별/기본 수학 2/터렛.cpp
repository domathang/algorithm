#include<stdio.h>
#define _USE_MATH_DEFINES
#include<math.h>

int main()
{
	int x1,x2,y1,y2,r1,r2,i,t;
	double d;
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		scanf("%d %d %d %d %d %d",&x1,&y1,&r1,&x2,&y2,&r2);
		d=sqrt(pow(x1-x2,2)+pow(y1-y2,2));
		//printf("d : %lf\n",d);
		if( x1==x2 && y1==y2 && r1==r2) printf("-1\n");
		else if( d > r1+r2 || d+r1 < r2 || d+r2 < r1) printf("0\n");
		else if( d == r1+r2 || d+r1 == r2 || d+r2 == r1) printf("1\n");
		else printf("2\n");
	}
	return 0;
}
