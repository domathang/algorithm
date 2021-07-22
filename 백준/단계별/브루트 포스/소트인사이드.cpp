#include<stdio.h>
#include<algorithm>
using namespace std;

int main()
{
	int n, i=0, cnt=0, a[11]={};
	scanf("%d",&n);
	
	while(n!=0)
	{
		a[i++] = n%10;
		n /= 10;
		cnt++;
	}
	
	sort(a, a+cnt);
	
	for(i=cnt-1; i>=0; i--)
		printf("%d",a[i]);
	
	return 0;
}
