#include<iostream>
#include<stdlib.h>
using namespace std;

int sudoku[10][10],wide[10],dep[10],squ[10],check1[10];

void dfs(int x,int y,int cnt)
{
	int i,j,check[10]={};

	if( cnt==82 ) {
	
		for( i=1;i<=9;i++ )
		{
			for( j=1;j<=9;j++ )
			{
				printf("%d ",sudoku[i][j]);
			}printf("\n");
		}
		exit(0);
	}
	else {
		
	if( sudoku[x][y]!=0 ) {
		if( y==9 ) dfs(x+1,1,cnt+1);
		else dfs(x,y+1,cnt+1);
	}
	else if( sudoku[x][y]==0 ) {
		 
		for( i=1 ; i<=9 ; i++ ){
		
			check[sudoku[x][i]] ++;
			
			check[sudoku[i][y]] ++;

		}

		for( i = (x-1)/3*3+1 ; i <= (x-1)/3*3+3 ; i++ ) {
			for( j = (y-1)/3*3+1 ; j <= (y-1)/3*3+3 ; j++ ) {
				check[sudoku[i][j]] ++;
	
			}
		}
		
		
		for( i=1 ; i<=9 ; i++ )	{

			if( check[i]==0 ) {
		
				sudoku[x][y] = i;
			
				if( y==9 ) dfs(x+1,1,cnt+1);
				else dfs(x,y+1,cnt+1);	
				sudoku[x][y] = 0;	
			}
		}
	}
	}
}

int main()
{
	int i,j;
	
	for(i=1;i<=9;i++)
		for(j=1;j<=9;j++)
			scanf("%d",&sudoku[i][j]);

	dfs(1,1,1);
	
	return 0;
}
