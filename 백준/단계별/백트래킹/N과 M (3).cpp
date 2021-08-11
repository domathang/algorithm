#include<iostream>

int n,m;
int arr[9];

void dfs(int x,int count)
{
	arr[count]=x;
	
	if( count==1 ) {
		for( int i=m ; i>0 ; i-- )
			printf("%d ",arr[i]);
		printf("\n");
		return;
	}
	
	for( int i=1 ; i<=n ; i++ ) {
			dfs(i,count-1);
		}
}


int main()
{
	std::cin >> n >> m;
	for(int i=1;i<=n;i++) {
		dfs(i,m);
	}
	
	return 0;
}
