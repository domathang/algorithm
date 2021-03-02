#include <iostream>
using namespace std;

int a[501][501] = {},b[501][501] = {};
int n, sum = 0, max_sum = 0;

void find(int i,int j)
{
    if (i == n+1)
    {
        if (sum > max_sum)
        {
            max_sum = sum;
        }
        return;
    }
    
    sum += a[i+1][j];
    if(b[i+1][j] < sum) {
    	b[i+1][j] = sum;
    	find(i + 1,j);
	} 
	sum -= a[i+1][j];
	
	sum += a[i+1][j+1];
	if(b[i+1][j+1] <= sum) {
		b[i+1][j+1] = sum;
		find(i + 1,j+1);
	}
	sum -= a[i+1][j+1];
}
int main()
{
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            cin >> a[i][j];
        }
    }
    find(1,1);
    cout << max_sum + a[1][1] << endl;
    return 0;
}
