#include <iostream>
using namespace std;

int main() 
{
	long N, ctry[100000], road[100000], min, sum=0;
	cin >> N;
	for(int i=0; i<N-1; i++) {
		cin >> road[i];
	}
	for(int i=0; i<N; i++) {
		cin >> ctry[i];
	}
	min = ctry[0];
	for(int i=0; i<N-1; i++) {
		if( min>ctry[i] ) min = ctry[i];
		sum += min * road[i];
	}
	cout << sum;
	return 0;
}
