#include <cstdio>

int main()
{
	long long int i,j,n, sum = 0 , a[10]={0,1,1,1,1,1,1,1,1,1}, b[10]={};
	
	scanf("%lld",&n);
	
	for(i=1; i<n; i++) {
		if(i == 1) {
			for(j=0; j<10; j++) {
				if(j-1 >= 0) {
					b[j-1] = b[j-1] + a[j]%2;
				}
				if(j+1 <= 9) {
					b[j+1] = b[j+1] + a[j]%2;
				}
			}
		}
		else {
			for(j=0; j<10; j++) {
				if(j == 0) {
					b[j+1] = b[j+1] + a[j];
				}
				else if(j == 9) {
					b[j-1] = b[j-1] + a[j];
				}
				else {
					b[j-1] = (b[j-1] + a[j]) % 1000000000;
					b[j+1] = (b[j+1] + a[j]) % 1000000000; 
				}
			}
		}
		
		for(j=0; j<10; j++) {
			a[j] = b[j];
			b[j] = 0;
			//printf("%d %d %d\n",i,j,a[j]);
		}
	}
	for(i=0; i<10; i++) {
		sum += a[i];
	}
	
	printf("%lld", sum % 1000000000);
	return 0;
}
