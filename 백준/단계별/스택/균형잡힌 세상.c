#include<stdio.h>
#include<string.h>
int main()
{
	char a[101],ch[101];
	int r=0,i,check=0;
	while(1){
		check=0;
		r=0;
		gets(a);
		if( !strcmp(a,".") ) break;
		for(i=0;i<strlen(a);i++){
			if( a[i]=='(' || a[i]=='[' ){
				ch[r]=a[i];
				r++;
			}
			else if( a[i]==')' ){
				if( ch[r-1]=='(' ){
					r--;
				}
				else check=1;
			}
			else if( a[i]==']' ){
				if( ch[r-1]=='[' ){
					r--;
				}
				else check=1;
			}
		}
		if( check==0 && r==0 ) printf("yes\n");
	else printf("no\n");
	}

	return 0;
}