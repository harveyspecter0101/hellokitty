#include<bits/stdc++.h>
using namespace std;

int solve(int i,int &n,vector<int>&weight,vector<int>val,int wt,vector<vector<int>>&dp){
    if(i == n) return 0;
    if(dp[i][wt] != -1) return dp[i][wt];
    int take = 0;
    if(weight[i] <= wt) take = val[i] + solve(i+1,n,weight,val,wt-weight[i],dp);
    int not_take = solve(i+1,n,weight,val,wt,dp);
    return dp[i][wt] = max(take,not_take);
}

// Branch and Bound

struct Node{
    int wt;
    int val;
    double ratio;

    Node(int w,int v){
        wt = w;
        val = v;
        ratio = (double)v/(double)w;
    }
};


int best = -1; // global best variable

double bound(int i,int &n,int &W,int curr_value,int curr_wt,vector<Node>&items){
    if(curr_wt >= W) return curr_value;
    int weight = curr_wt;
    double profit_bound = curr_value;
    while(i < n && weight + items[i].wt <= W){
        weight += items[i].wt;
        profit_bound += items[i].val;
        i++;
    }
    if(i < n && weight < W){
        profit_bound +=  (W - weight)*items[i].ratio;
    }
    return profit_bound;
}

// branch and bound solve

void solve2(int i,int &n,int &W,vector<Node>&items,int curr_value,int curr_wt){
    best = max(best,curr_value);
    if(i == n) return;
    if(bound(i,n,W,curr_value,curr_wt,items) <= best) return; // pruning
    // condition to take
    if(curr_wt + items[i].wt <= W) solve2(i+1,n,W,items,curr_value + items[i].val,curr_wt + items[i].wt);
    // condition to not_take
    solve2(i+1,n,W,items,curr_value,curr_wt);
}


int main(){
    vector<int>weight = {1,3,4,5};
    vector<int>val = {10,40,50,70};
    int wt = 7;
    int n = 4;
    vector<vector<int>>dp(5,vector<int>(8,-1));  // {n+1,wt+1}
    int ans = solve(0,n,weight,val,wt,dp);
    cout<<"Max Val : "<<ans<<endl;
    vector<Node>items;

    for(int i=0;i<n;i++){
        items.push_back({weight[i],val[i]});
    }

    sort(begin(items),end(items),[](const Node &a,const Node &b){
        return a.ratio > b.ratio;
    });

    solve2(0,n,wt,items,0,0);
    cout<<"Best : "<<best<<endl;
}

// gpt code ahh -----------------------


#include <iostream>
using namespace std;

int main() {
    int n, W;

    cout << "Enter number of items: ";
    cin >> n;

    int wt[n], val[n];

    cout << "Enter weights of items:\n";
    for (int i = 0; i < n; i++) {
        cin >> wt[i];
    }

    cout << "Enter values of items:\n";
    for (int i = 0; i < n; i++) {
        cin >> val[i];
    }

    cout << "Enter knapsack capacity: ";
    cin >> W;

    int dp[n + 1][W + 1];

    // Initialize first row and column
    for (int i = 0; i <= n; i++) {
        for (int w = 0; w <= W; w++) {
            if (i == 0 || w == 0) {
                dp[i][w] = 0;
            }
            else if (wt[i - 1] <= w) {
                dp[i][w] = max(
                    val[i - 1] + dp[i - 1][w - wt[i - 1]],
                    dp[i - 1][w]
                );
            }
            else {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }

    cout << "Maximum value = " << dp[n][W];

    return 0;
}
