#include <iostream>

using namespace std;

int main()
{
	int n, m, cntw=0, cntb=0, min=9999;
	char board[51][51];
	
	cin >> n >> m;
	
	for(int i=0; i<n; i++)
		cin >> board[i];
	
	for(int i=0; i<n-7; i++) {
		for(int j=0; j<m-7; j++) {
			
			cntw = cntb = 0;
			for(int k=i; k<i+8; k++) {
				for(int l=j; l<j+8; l++) {
					if((k+l) % 2 == 0) {
						if(board[k][l] == 'B')
							cntw++;
						else 
							cntb++;
					} else {
						if(board[k][l] == 'W') 
							cntw++;
						else 
							cntb++;
					}
				}
			}
			if(min > cntw) min = cntw;
			if(min > cntb) min = cntb;
		}
	} 
	cout << min;
	
	return 0;	
}
