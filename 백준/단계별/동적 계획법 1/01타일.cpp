#include<iostream>
using namespace std;
int a[1000001] = { 1,2, };

int main()
{
	int n;
	cin >> n;
	for (int i = 2;i < n;i++)
	{
		a[i] = a[i - 1] + a[i - 2];
		a[i] %= 15746;
	}
	cout << a[n - 1] << endl;
	return 0;
}
