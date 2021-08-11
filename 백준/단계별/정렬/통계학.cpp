#include<stdio.h>
#include<algorithm>
using namespace std;

int a[500001];

int main()
{
	int n, i,k,sum=0,cnt=-1,check=0,min=4001,max=-4001;
	int b[4001]={},c[4001]={},d[8001]={};
	
	scanf("%d",&n);
	
	for(i=0;i<n;i++){
		
		scanf("%d",&a[i]);
		sum+=a[i];
		
		if(min>a[i]) min=a[i];
		if(max<a[i]) max=a[i];
		
		if(a[i]>=0)
			b[a[i]]++;
		else if(a[i]<0)
			c[-a[i]]++;
	}
	
	sort(a,a+n);
	
	printf("%.0lf\n",(double)sum/n);
	
	printf("%d\n",a[n/2]);
	
	for(i=4000;i>0;i--){
		
		if(cnt<c[i]){
			k=0;
			d[k]=-i;
			cnt=c[i];
			check=0;
		}
		else if(cnt==c[i]){
			d[++k]=-i;
			check=1;
		}
	}
	for(i=0;i<4001;i++){
		
		if(cnt<b[i]){
			k=0;
			d[k]=i;
			cnt=b[i];
			check=0;
		}
		else if(cnt==b[i]){
			d[++k]=i;	
			check=1;
		}
			
	}
	
	if(check==1) printf("%d\n",d[1]);
	else if(check==0) printf("%d\n",d[0]);
	
	printf("%d\n",max-min);
	
	return 0;
}
