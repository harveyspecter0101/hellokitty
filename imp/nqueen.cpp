#include<bits/stdc++.h>
using namespace std;

int cnt = 0;

bool isSafe(int r, int c, int &m, int &n, vector<vector<int>>&board){
    for(int i=0; i<m; i++){
        for(int j=0; j<n; j++){
            if(board[i][j] == 1){
                // Same column
                if(j == c) return false;
                // Same diagonal
                if(abs(i-r) == abs(j-c))
                    return false;
            }
        }
    }
    return true;
}

void print(vector<vector<int>>&board, int &m, int &n){
    for(int i=0; i<m; i++){
        for(int j=0; j<n; j++){
            if(board[i][j]) cout<<"Q ";
            else cout<<"_ ";
        }
        cout<<endl;
    }
}

void solve(int row, int &m, int &n, vector<vector<int>>&board){
    if(row == m){
        cnt++;
        cout<<"Solution : "<<cnt<<endl;
        print(board,m,n);
        return;
    }

    for(int col=0; col<n; col++){
        if(board[row][col]){
            solve(row+1,m,n,board);
            return;
        }
    }

    for(int col=0; col<n; col++){
        if(isSafe(row,col,m,n,board)){
            board[row][col] = 1;
            solve(row+1,m,n,board);
            board[row][col] = 0;
        }
    }
}

int main() {
    int n;
    cout << "Enter N: ";
    cin >> n;

    vector<vector<int>> board(n, vector<int>(n, 0));
    int r, c;
    cout << "Enter position of first Queen (row and column): ";
    cin >> r >> c;

    // Validate position
    if(r < 0 || r >= n || c < 0 || c >= n) {
        cout << "Invalid position!" << endl;
        return 0;
    }

    // Place first Queen
    board[r][c] = 1;
    cout << "\nInitial Board:\n";
    print(board, n, n);

    // Backtracking to place remaining Queens
    solve(0, n, n, board);
    cout << "Total solutions: " << cnt << endl;
    return 0;
}