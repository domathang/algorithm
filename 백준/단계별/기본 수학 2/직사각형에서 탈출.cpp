#include<stdio.h>
int main()
{
	int x,y,w,h,d;
	scanf("%d %d %d %d",&x,&y,&w,&h);
	d=x>y?y:x;
	if(d>w-x) d=w-x;
	if(d>h-y) d= h-y;
	printf("%d\n",d); 
	return 0;
}
