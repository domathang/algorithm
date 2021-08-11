#include<stdio.h>
int a[1000000];
int main()
{
	int k,i,n,r=0;
	long long int sum=0;
	scanf("%d",&k);
	for(i=0;i<k;i++){
		scanf("%d",&n);
		if(n==0){
			r--;
			a[r]=0;
		}
		else{
			a[r]=n;
			r++;
		}
	}
	for(i=0;i<r;i++){
		sum+=a[i];
	}
	printf("%lld\n",sum);
	return 0;
}