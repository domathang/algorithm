#include<stdio.h>
#include<math.h>

int main()
{
	int n,ch,cnt;
	scanf("%d",&n);
	
	while(n!=0)
	{
		cnt=0;
		for(int i=n+1;i<=n*2;i++)
		{
			ch=0;
			for(int j=2;j<=sqrt(i);j++)
			{
				if(i%j==0) {
					ch=1; 
					break;
				}
			}
			if(ch==0  && (i%2==1 || i==2)){
				cnt++;	
			} 
		}
		printf("%d\n",cnt);
		scanf("%d",&n);
	}

	return 0;
}
