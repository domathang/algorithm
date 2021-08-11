#include <iostream>
using namespace std;

int main()
{
	int N, a[1000][2]={}, i, j, max1 = 1;
	
	cin >> N;
	
	a[0][1] = 1;
	
	for(i=0; i<N; i++)
		cin >> a[i][0];
	
	for(i=1; i<N; i++)
	{
		for(j=i-1; j>=0; j--)
		{
			if(a[i][0] > a[j][0] && a[i][1] < a[j][1]) 
				a[i][1] = a[j][1];
		}
		a[i][1]++;
		if(max1 < a[i][1]) {
			max1 = a[i][1];
		}
	}
	
	cout << max1;
	
	return 0;
}
