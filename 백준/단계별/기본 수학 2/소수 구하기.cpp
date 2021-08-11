#include<stdio.h>
#include<math.h>

int main()
{
	int i,j,n,m,ch;
	scanf("%d %d",&n,&m);
	for(i=n;i<=m;i++)
	{
		ch=0;
		for(j=2;j<=sqrt(i);j++)
		{
			if( j!=1 && i%j==0) {
				ch=1; 
				break;
			}
		}
		if(i!=1 && ch==0 && i%2!=0 || i==2){
			printf("%d\n",i);	
		} 
	}
	return 0;
}
