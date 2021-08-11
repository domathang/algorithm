#include<stdio.h>
int main()
{
	int x,y,w,h,j,d,z,k;
	scanf("%d %d %d %d %d %d",&x,&y,&z,&k,&w,&h);
	
	if(x==z) d=w;
	else if(z==w) d=x;
	else d=z;
	
	if(y==k) j=h;
	else if(k==h) j=y;
	else j=k;
	printf("%d %d\n",d,j); 
	return 0;
}
