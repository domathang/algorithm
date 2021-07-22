#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
	int cnt=0,n,sum=0,sumsum=0;
	scanf("%d",&n);
	 
	while(sum!=n)
	{
		cnt++;
		sum=sumsum=cnt;
		while(sumsum!=0)
		{
			sum+=sumsum%10;
			sumsum/=10;
		}	
		if(cnt>=n) {
			cnt=0;
			break;
		}
	}
	printf("%d\n",cnt);
	return 0;
}
