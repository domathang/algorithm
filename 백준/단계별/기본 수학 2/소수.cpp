#include<stdio.h>
int main()
{
	int i,j,n,m,ch,cnt=0,sum=0,min=1000000;
	scanf("%d %d",&n,&m);
	for(i=n;i<=m;i++)
	{
		ch=0;
		for(j=1;j<=i/2;j++)
		{
			if(i%j==0)
				ch++;
		}
		if(ch==1){
			sum+=i;
			if(min>i) min=i;
			cnt++;	
		} 
	}
	if(cnt!=0) printf("%d\n%d",sum,min);
	else
	printf("%d\n",-1);
	return 0;
}
