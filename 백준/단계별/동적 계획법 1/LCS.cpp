#include <iostream>
#include <cstring>

using namespace std;

int a[1001][1001];
int cnt[1001][1001];
char seq1[1001];
char seq2[1001];

int main()
{
	cin >> seq1;
	cin >> seq2;
	
	int len1 = strlen(seq1), len2 = strlen(seq2);

	for(int i=1; i<=len1; i++) {
		for(int j=1; j<=len2; j++) {
			if (seq1[i-1] == seq2[j-1]) {
				a[i][j] = a[i-1][j-1] + 1;
			} else {
				a[i][j] = a[i-1][j]>a[i][j-1]?a[i-1][j]:a[i][j-1];
			}
		}
	}
	cout << a[len1][len2];
}
