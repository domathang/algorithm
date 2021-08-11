#include<iostream>
using namespace std;
long long int a[1000001] = { 1,1,1,2,2, };

int main()
{
	int t, n;
	cin >> t;
	for (int i = 0;i < t;i++)
	{
		cin >> n;
		if (a[n - 1] == 0)
		{
			for (int j = 5;j < n;j++)
			{
				a[j] = a[j - 5] + a[j - 1];
			}
		}	
		cout << a[n - 1] << endl;
	}
	return 0;
}
