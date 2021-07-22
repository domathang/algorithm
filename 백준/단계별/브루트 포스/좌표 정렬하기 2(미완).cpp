#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

vector< pair<int, int> > v;

bool compare(pair<int, int>a, pair<int, int>b) {
	if(a.first == b.first) {
		return a.second > b.second;
	} else {
		cout << "?";
		return a.first > b.first;
	}
} 

int main()
{
	int n, x, y;
	cin >> n;
		
		
	for(int i=0; i<n; i++) {
		cin >> x >> y;
		v.push_back({x, y});
	}	
	
	sort(v.begin(), v.end(), compare);
	
	for(int i=0; i<n; i++)
		cout << v[i].first << " " << v[i].second << '\n';
} 
