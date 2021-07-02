#include <iostream>
#include <stack>

using namespace std;

int a[1000000], nge[1000000];
int main() 
{
	int size;
	stack<int>s;
	
	cin >> size;
	for(int i=0; i<size; i++) {
		cin >> a[i];
	}
	
	for(int i=size-1; i>=0; i--) {
		if(s.empty()) {
			nge[i] = -1;
			s.push(a[i]);	
		}
		else {
			if(a[i] < s.top()) {
				nge[i] = s.top();
				s.push(a[i]);
			}
			else if(a[i] >= s.top()) {
				while(!s.empty() && a[i] >= s.top()) {
					s.pop();
				}
				if(s.empty()) 
					nge[i] = -1;
				else 
					nge[i] = s.top();
				s.push(a[i]);
			}
		}
	}
	
	for(int i=0; i<size; i++) {
		cout << nge[i] << " ";
	}
	return 0;
}
