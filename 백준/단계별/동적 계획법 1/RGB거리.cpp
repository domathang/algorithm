#include <iostream>
using namespace std;

int main()
{
	int n,a[3][1001]={};
	cin >> n;
	cin >> a[0][1] >> a[1][1] >> a[2][1];
	for(int i=2;i<=n;i++) {
		cin >> a[0][i] >> a[1][i] >> a[2][i];

		a[0][i] += a[1][i-1] > a[2][i-1] ? a[2][i-1]:a[1][i-1];
		a[1][i] += a[0][i-1] > a[2][i-1] ? a[2][i-1]:a[0][i-1];
		a[2][i] += a[0][i-1] > a[1][i-1] ? a[1][i-1]:a[0][i-1];
	}
	if(a[1][n] >= a[0][n] && a[2][n] >= a[0][n]) {
		cout << a[0][n] << endl;
	}
	else if(a[0][n] >= a[1][n] && a[2][n] >= a[1][n]) {
		cout << a[1][n] << endl;
	}
	else cout << a[2][n] << endl;
	return 0;
}
