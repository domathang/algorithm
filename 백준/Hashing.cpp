#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	int L;
	cin >> L;
	char a[51];
	cin >> a;
	long long answer = 0, pow31;
	for(int i=0; i<L; i++) {
		pow31 = 1;
		for(int j=0; j<i; j++) {
			pow31 = (pow31 * 31) % 1234567891;
		}
		answer = (answer + ((a[i] - 'a' + 1) * pow31)) % 1234567891;
	}
	cout << answer;
}
