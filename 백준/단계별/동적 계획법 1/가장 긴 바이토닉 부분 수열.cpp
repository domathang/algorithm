#include <iostream>
using namespace std;

int main()
{
	int N, a[1000][3]={}, i, j, max = 1;
	
	cin >> N;
	
	a[0][1] = 1;
	a[N][2] = 1;
	
	for(i=0; i<N; i++)
		cin >> a[i][0];
	
	for(i=1; i<N; i++)
	{
		for(j=i-1; j>=0; j--)
		{
			if(a[i][0] > a[j][0] && a[i][1] < a[j][1]) 
			{
				a[i][1] = a[j][1];
			}
		}
		a[i][1]++;
	}
	
	for(i=N-1; i>=0; i--)
	{
		for(j=i+1; j<N; j++)
		{
			if(a[i][0] > a[j][0] && a[i][2] < a[j][2]) 
			{
				a[i][2] = a[j][2];
			}
		}
		a[i][2]++;
		
		if(a[i][1] + a[i][2] > max) max = a[i][1] + a[i][2];
	}
	
	cout << max - 1;
	
	return 0;
}

