#include<iostream> 
#include<stdlib.h>
using namespace std;

int n,check[17],check1[17];

int dfs(int x,int y)
{
	for(int i=1;i<x ;i++)
	{
		if( check[i]==x ) return 0;
		if( check1[i]==y ) return 0;
		if( abs( x-check[i] ) == abs( y-check1[i]) ) return 0;
	} 
	if(x==n) return 1;
	
	check[x]=x;
	check1[x]=y;
	
	int r=0;
	for( int i=1 ; i<=n ; i++ )
		r += dfs(x+1,i);	
	return r;
}

int main()
{
	scanf("%d",&n);
	int r=0;
	for(int i=1;i<=n;i++){
		r += dfs(1,i);	
	} 
	 
	printf("%d\n",r);

	return 0;
}
