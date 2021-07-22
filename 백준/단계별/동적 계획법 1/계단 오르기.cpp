#include <stdio.h>

int n,a[301],check[301]={0},s[301]={0},sum=0,max=0;

void search(int k) {
	
	if (k == n) {
		if ( s[n]<sum ) s[n] = sum;
		return;
	}

	if ( k <= 1 ||  (!check[k] || !check[k-1]) ) {	// 1칸 오르는 경우 
		sum += a[k+1];
		check[k+1] = 1;
		search(k+1);
		sum -= a[k+1];	
		check[k+1] = 0;
	}
	
	if( s[k] < sum || s[k] == 0) 
		s[k] = sum;
	else 
		return;
	
	if ( k+2 <= n ) {	// 2칸 오르는 경 우 
		sum += a[k+2];
		check[k+2] = 1;
		search(k+2);
		sum -= a[k+2];
		check[k+2] = 0;
	}
}

int main() 
{
	int i;
	scanf("%d",&n);
	for(i=1; i<=n; i++)
	{
		scanf("%d",&a[i]);
	}
	search(0);
	printf("%d",s[n]);
}
