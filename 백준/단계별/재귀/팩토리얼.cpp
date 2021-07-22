#include<stdio.h>
long long int f(int n)
{
	if(n==1) return 1;
	return n*f(n-1);
}
int main()
{
	int n;
	scanf("%d",&n);
	
	if(n!=0) printf("%lld",f(n));
	
	else printf("1");
	return 0;
}
