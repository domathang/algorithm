#include <iostream>
#include <algorithm>

using namespace std;

int a[1000000];

int main()
{
	int n;
	cin >> n;
	
	for(int i=0; i<n; i++)
		cin >> a[i];
	
	sort(&a[0], &a[n]);
	
	for(int i=0; i<n; i++)
		cout << a[i] << '\n';	
} 
