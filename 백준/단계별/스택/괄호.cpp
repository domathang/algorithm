#include<stdio.h>
#include<string.h>
char a[1000000];
int main()
{
	int i,r=0,t;
	scanf("%d",&t);
	for(i=0;i<t;i++){
		scanf("%s",a);
		r=0;
		for(int j=0;j<strlen(a);j++){
			if( a[j]=='(' ) r++;
			else if( r==0 && a[j]==')'){
				r=-1;
				break;
			}
			else r--;
		}
		if(r==0) printf("YES\n");
		else printf("NO\n");
	}

	return 0;
}