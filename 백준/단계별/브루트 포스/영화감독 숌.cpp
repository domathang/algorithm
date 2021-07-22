#include<stdio.h>
int main()
{
	int n, cnt=1, six, k=666, x;
	scanf("%d",&n);
	while(cnt!=n)
	{
		k++;
		x=k;
		six=0;
		while(x!=0)
		{
			if(x%10==6)
			{
				six++;
				if(six==3){
					cnt++;
					break;
				}
			}
			else {
				six=0;
			}
			x/=10;
		}

	}
	printf("%d",k);
	return 0;
}
