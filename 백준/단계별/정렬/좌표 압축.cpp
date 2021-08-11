#include <iostream>
#include <algorithm>
#include <vector> 

using namespace std;

vector< pair<int, int> > v;

int xi[1000000];

int main()
{
	int N, x, cnt=0;
	cin >> N;
	for(int i=0; i<N; i++) {
		cin >> x;
		v.push_back({x, i});
	};
	sort(v.begin(), v.end());
	
	xi[v[0].second] = cnt; // ù���� ������ 0 
	
	for(int i=1; i<N; i++) {
		if(v[i].first > v[i-1].first ) {
			xi[v[i].second] = ++cnt; // ���� Ŀ������ +1 
		} else {
			xi[v[i].second] = cnt; // ���� ������ �״�� 
		}
	}
	
	for(int i=0; i<N; i++) {
		cout << xi[i] << " ";	
	}
}
