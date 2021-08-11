#include<iostream>
using namespace std;

int n,m;
int arr[9],visit[9];

void dfs(int x,int count)
{
	visit[x]=1;
	arr[count]=x;
	
	if( count==1 ) {
		for( int i=m ; i>0 ; i-- )
			printf("%d ",arr[i]);
		printf("\n");
		return;
	}
	
	for( int i=1 ; i<=n ; i++ ) {
		if( visit[i]!=1 ) {
			dfs(i,count-1);
			visit[i]=0;
		}
	}
}

int main()
{
	cin >> n >> m;
	for(int i=1;i<=n;i++) {
		for( int j=1;j<=n;j++ ) 
			visit[j]=0;            //visit ÃÊ±âÈ­ 
		dfs(i,m);
	}
	
	return 0;
}
