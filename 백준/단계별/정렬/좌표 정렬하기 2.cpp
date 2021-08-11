#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;

vector < pair<int,int> > v;

int main()
{
	int i,N,a,b;
	scanf("%d",&N);
	for(i=0; i<N; i++)
	{
		scanf("%d %d", &a, &b);
		v.push_back(pair <int, int>(b,a))	;
	}
	
	sort(v.begin(),v.end());
	
	for(i=0; i<N; i++)
	{
		printf("%d %d\n",v[i].second,v[i].first);
	}
	
	return 0;
}

