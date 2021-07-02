#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector< pair<int, int> > v;

int main()
{
	int N, startT, endT, cnt=1;
	cin >> N;
	for(int i=0; i<N; i++) {
		cin >> startT >> endT;
		v.push_back({endT, startT});
	}
	sort(v.begin(), v.end());
	
	int x;
	x = v[0].first;

	for(int i=1; i<N; i++) {
		if(x <= v[i].second) {
			cnt++;
			x = v[i].first;
		}
	}
	
	cout << cnt;
}
