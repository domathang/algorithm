#include<stdio.h>
#include<string.h>
int q[2000001];
char a[6];
int main()
{
	int n,t,r=0;
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		scanf("%s",a);
		if( !strcmp(a,"push") ){
			scanf("%d",&n);
			q[r]=n;
			r++;
		}
		else if( !strcmp(a,"pop") ){
			if( r==0 ) printf("-1\n");
			else{
				r--;
				printf("%d\n",q[r]);
			}
		}
		else if( !strcmp(a,"size") ){
			printf("%d\n",r);
		}
		else if( !strcmp(a,"empty") ){
			if( r==0 ) printf("1\n");
			else printf("0\n");
		}
		else if( !strcmp(a,"top") ){
			if( r!=0 ) printf("%d\n",q[r-1]);
			else printf("-1\n");
		}
	}
	return 0;
}