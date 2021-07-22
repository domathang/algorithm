#include <bits/stdc++.h>

using namespace std;

vector< pair<int, int> > v;

int main()
{
	int n, x, y;
	cin >> n;
	
	for(int i=0; i<n; i++) {
		cin >> x >> y;
		v.push_back({x, y});
	}	
	
	sort(v.begin(), v.end());
	
	for(int i=0; i<n; i++)
		cout << v[i].first << " " << v[i].second << '\n';
} 
