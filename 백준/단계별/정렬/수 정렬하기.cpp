#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
	int i,n,a[1001];
	scanf("%d",&n);
	for(i=0;i<n;i++)
		scanf("%d",&a[i]);
	sort(a,a+n);
	for(i=0;i<n;i++)
		printf("%d\n",a[i]);
	return 0;
}
