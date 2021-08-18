#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int s1Pat[5] = {1, 2, 3, 4, 5};
int s2Pat[8] = {2, 1, 2, 3, 2, 4, 2, 5};
int s3Pat[10] = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    vector<int> v;

    int s1=0, s2=0, s3=0;
    for(int i=0; i<answers.size(); i++) {
        if ( s1Pat[i%5] == answers[i] ) { s1++; }
        if ( s2Pat[i%8] == answers[i] ) { s2++; }
        if ( s3Pat[i%10] == answers[i] ) { s3++; }
    }
    v.push_back(s1);
    v.push_back(s2);
    v.push_back(s3);

    int max_value = *max_element(v.begin(), v.end());

    for(int i=0; i<3; i++) {
        if( v[i] == max_value ) {
            answer.push_back(i+1);
        }
    }

    return answer;
}