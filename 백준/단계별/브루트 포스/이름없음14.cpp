#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool compare(pair<int, int>a, pair<int, int>b) {
	if (a.first == b.first) {
		return a.second < b.second;
	}
	else {
		return a.first < b.first;
	}
}

void init(vector< pair<int, int> > &v){
	v.push_back({3, 4});
	v.push_back({1, 1});
	v.push_back({1, -1});
	v.push_back({2, 2});
	v.push_back({3, 3});
}

int main(){
	vector< pair<int, int> >v;
	init(v);
	sort(v.begin(), v.end(), compare);
	for(auto i : v){
		cout<<i.first<<" "<<i.second<<endl;
	}
}
