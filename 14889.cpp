#include <iostream>
#include <vector>
#include <stdlib.h>
using namespace std;

int n, arr[21][21], minn = 9999;
vector<int> v[2];

void dfs(int k)
{
  int start = 0, link = 0;
  if (v[0].size() == n / 2 && v[1].size() == n / 2)
  {
    for (int i = 0; i < v[0].size(); i++)
    {
      for (int j = 0; j < v[0].size(); j++)
      {
        if (i != j)
        {
          start += arr[v[0][i]][v[0][j]];
          link += arr[v[1][i]][v[1][j]];
        }
      }
    }
    if (minn > abs(start - link))
    {
      minn = abs(start - link);
    }
  }
  if(v[0].size()<n/2)
  {
  	v[0].push_back(k);
 	dfs(k + 1);
 	v[0].pop_back();
  }
 
  if(v[1].size()<n/2)
  {
  	v[1].push_back(k);
 	 dfs(k + 1);
 	 v[1].pop_back();
  }
}

int main()
{
  int k;
  scanf("%d", &n);

  for (int i = 1; i <= n; i++)
    for (int j = 1; j <= n; j++)
      scanf("%d", &arr[i][j]);

  dfs(1);

  printf("%d\n", minn);
  return 0;
}