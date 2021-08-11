#include<stdio.h>
#include<math.h>
int main()
{
	int x,y,z;
	do{
		scanf("%d %d %d",&x,&y,&z);
		if(pow(x,2)+pow(y,2)==pow(z,2)&&x!=0) printf("right\n");
		else if(pow(z,2)+pow(y,2)==pow(x,2)&&x!=0) printf("right\n");
		else if(pow(x,2)+pow(z,2)==pow(y,2)&&x!=0) printf("right\n");
		else if(x!=0)printf("wrong\n");
	}while(x!=0);
	return 0;
}
