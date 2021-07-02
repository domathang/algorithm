#include <iostream>
#include <stack>

int a[100001]; 
char o[100001]={};

int main()
{
	int n, cnt=0, cnt2=1;
	std::stack<int> s;
	std::cin >> n;
	for(int i=1; i<=n; i++) {
		std::cin >> a[i]; 
	}
	
	for(int i=1; i<=n; i++) {
		s.push(i);
		o[cnt++] = '+';
		while(s.top() == a[cnt2]) {
			cnt2++;
			s.pop();
			o[cnt++] = '-';
			if(s.empty()) break;
		}
	}
	if(!s.empty()) {
		std::cout << "NO" << std::endl;			
	} else {
		for(int i=0; i<cnt; i++) {
			std::cout << o[i] << '\n';
		}	
	}
}
