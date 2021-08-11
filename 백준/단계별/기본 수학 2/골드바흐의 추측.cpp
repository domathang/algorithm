#include<stdio.h>
#include<math.h>

int main()
{
	int i,j,n,ch,t,l;
	scanf("%d",&t);
	for(l=0;l<t;l++)
	{
		scanf("%d",&n);
	
		for(i=n/2;i>=2;i--)
		{
			ch=0;
			for(j=2;j<=sqrt(i);j++)
			{
				if( j!=1 && i%j==0 && i!=2) 
				{
					ch=1; 
					break;
				}
			}
			if(ch==0 && (i%2!=0 || i==2))
			{
				ch=0;
				for(j=2;j<=sqrt(n-i);j++)
				{
					if((n-i)%j==0 && n-i!=2) 
					{
						ch=1; 
						break;
					}
				}
				if(ch==0 && n-i%2!=0){
					printf("%d %d\n",i,n-i);
					break;
				}
						
			} 
		}
	}

	return 0;
}
