#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
vector < vector<string> > v(50);

int main()
{
	int i,N;
	string word;
	scanf("%d",&N);
	for(i=0; i<N; i++)
	{
		cin >> word;
		v[word.length()-1].push_back(word);
	}
	
	for(i=0; i<50; i++)
	{
		sort(v[i].begin(),v[i].end());
		v[i].erase(unique(v[i].begin(),v[i].end()),v[i].end()); // unique �Լ��� erase �Լ��� �̿��� ������ �ߺ� ���� ���� 
		for(int j=0; j<v[i].size(); j++)
			cout << v[i][j] << endl;
	}
	
	return 0;
}


