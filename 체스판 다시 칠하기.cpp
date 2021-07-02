#include <iostream>

int main()
{
	int n,m;
	std::cin >> n >> m;
	char board[51][51];
	
	for(int i=0; i<n; i++) {
		std::cin >> board[i];
	}
	
	int bw=0, wb=0, min=9999;
	for(int i=0; i<n-7; i++) {
		for(int j=0; j<m-7; j++) {
			bw = wb = 0;
			for(int k=i; k<i+8; k++) {
				for(int l=j; l<j+8; l++) {
					if(k%2==i%2) {
						if(l%2==j%2) {
							if(board[k][l] == 'B') {
								bw++;
							} else {
								wb++;
							}
						} else {
							if(board[k][l] == 'W') {
								bw++;
							} else {
								wb++;
							}
						}
					} else {
						if(l%2==j%2) {
							if(board[k][l] == 'W') {
								bw++;
							} else {
								wb++;
							}
						} else {
							if(board[k][l] == 'B') {
								bw++;
							} else {
								wb++;
							}
						}
					}
				}
			}
			if(min > wb) 
				min = wb;
			if(min > bw)
				min = bw;
		}
	} 
	std::cout << min;
	return 0;	
}
