#include <iostream>
#include <vector>
#include <algorithm> 

std::vector< std::pair<int, int> > v(1000000);
int x[1000000];

int main()
{
	int N, k;
	std::cin >> N;
	for(int i=0; i<N; i++) {
		std::cin >> k;
		v.push_back(pair<int, int>(k, i));
	}
	std::cout << "OK" << std::endl;
	sort(v.begin(), v.end());
	std::cout << "OK" << std::endl;
	for(int i=0; i<N; i++) {
		if(i!=0 && v[i][1] == x[i-1]) x[v[i][1]] = x[i-1];
		else x[v[i][1]] = i;
	}
	std::cout << "OK" << std::endl;
	for(int i=0; i<N; i++) {
		std::cout << x[i] << " ";
	}
	return 0;
}
