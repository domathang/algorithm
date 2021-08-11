#include<iostream>
using namespace std;

int main()
{
	int t, n, a[2][41] = { {1,0},{0,1} };
	cin >> t;
	for (int i = 0;i < t;i++)
	{
		cin >> n;
		for (int j = 2;j <= n;j++)
		{
			a[0][j] = a[0][j - 1] + a[0][j - 2];
			a[1][j] = a[1][j - 1] + a[1][j - 2];
		}
		printf("%d %d\n", a[0][n], a[1][n]);
	}
	return 0;
}
