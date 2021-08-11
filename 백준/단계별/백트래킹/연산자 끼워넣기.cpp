#include<iostream>
using namespace std;

int n,a[11];
int maxx=-1000000001,minn=1000000001;

void dfs(int x,int num,int pl,int mi,int me,int di)
{
	if(num==n-1) {
		if(maxx < x) maxx=x;
		if(minn > x) minn=x;
		return;
	}
	if( pl>0 ) {
		dfs(x+a[num+1],num+1,pl-1,mi,me,di);
	}
	if( mi>0 ) {
		dfs(x-a[num+1],num+1,pl,mi-1,me,di);
	}
	if( me>0 ) {
		dfs(x*a[num+1],num+1,pl,mi,me-1,di);
	}
	if( di>0 ) {
		dfs(x/a[num+1],num+1,pl,mi,me,di-1);
	}
}

int main()
{
	int pl,mi,me,di;
	scanf("%d",&n);
	for( int i=0;i<n;i++)
		scanf("%d",&a[i]);
	
	scanf("%d %d %d %d",&pl,&mi,&me,&di);
	
	dfs(a[0],0,pl,mi,me,di);
	
	printf("%d\n%d",maxx,minn);
	return 0;
}
