#include <iostream>
#include <vector>
#include <string>
using namespace std;
vector < vector<string> > v(300);

int main()
{
	int N,age;
	string name;
	cin >> N; 
	for(int i=0; i<N; i++)
	{
		cin >> age >> name;
		v[age].push_back(name);
	}
	
	for(int i=1; i<=200; i++)
	{
		for(int j=0; j<v[i].size(); j++)
			cout << i << " " << v[i][j] << '\n';
	}
	
	return 0;
}
