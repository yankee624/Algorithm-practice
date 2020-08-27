
#include <iostream>

using namespace std;

bool broken[10];

int can_reach(int channel) {
    int press_num = 0;
    if (channel == 0) {
        if (broken[0]) return -1;
        else return 1;
    }
    while(channel > 0) {
        int a = channel % 10;
        if(broken[a]) return -1;
        press_num++;
        channel /= 10;
    }
    return press_num;
}

int main()
{
    int N;
    int M;
    cin >> N >> M;
    for(int i=0; i<M; i++) {
        int x;
        cin >> x;
        broken[x] = true;
    }
    
    int ans = abs(N - 100);
    for(int start=0; start<=1000000; start++) {
        // First, go to "start" channel by pressing numbers (if possible)
        int press_num;
        if(start == 100) {
            press_num = 0;
        } else{
            press_num = can_reach(start);
        }
        
        if(press_num == -1) continue;
        
        // Next, go to "N" channel by pressing + / -
        press_num += abs(start - N);
        if(press_num < ans) ans = press_num;
        
    }
    cout << ans;


    return 0;
}
