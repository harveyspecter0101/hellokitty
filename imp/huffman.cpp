// #include<bits/stdc++.h>
// using namespace std;
// struct Node{
//     char ch;
//     int freq;
//     Node*left;
//     Node*right;
//     Node(char c,int f){
//         ch = c;
//         freq = f;
//         left = right = NULL;
//     }
// };
// struct Compare{
//     bool operator()(Node*a,Node*b){
//         return a->freq > b->freq;
//     }
// };
// void print(Node*root,string code){
//     if(!root) return;
//     if(!root->left && !root->right){
//         cout<<root->ch<<" : "<<code<<endl;
//         return;
//     }
//     print(root->left,code + "0");
//     print(root->right,code + "1");
// }
// void huffman(vector<char>&data,vector<int>&freq){
//     int n = data.size();
//     priority_queue<Node*,vector<Node*>,Compare>pq;
//     for(int i=0;i<n;i++){
//         pq.push(new Node(data[i],freq[i]));
//     }
//     while(pq.size() > 1){
//         Node *left = pq.top();
//         pq.pop();
//         Node*right = pq.top();
//         pq.pop();
//         Node*node = new Node('$',left->freq + right->freq);
//         node->left = left;
//         node->right = right;
//         pq.push(node);
//     }
//     print(pq.top(),"");
// }
// int main(){
//     vector<char>data = {'a', 'b', 'c', 'd', 'e', 'f'};
//     vector<int>freq = {5, 9, 12, 13, 16, 45};
//     huffman(data,freq);
//     return 0;
// }

// GPT code ahh -----------------------


#include <iostream>
#include <queue>
using namespace std;

struct Node {
    char ch;
    int freq;
    Node *left, *right;

    Node(char c, int f) {
        ch = c;
        freq = f;
        left = right = NULL;
    }
};

// Compare frequencies for min heap
struct Compare {
    bool operator()(Node* a, Node* b) {
        return a->freq > b->freq;
    }
};

// Print Huffman codes
void printCodes(Node* root, string code) {
    if (root == NULL)
        return;

    if (root->left == NULL && root->right == NULL) {
        cout << root->ch << " : " << code << endl;
    }

    printCodes(root->left, code + "0");
    printCodes(root->right, code + "1");
}

int main() {
    int n;
    cout << "Enter number of characters: ";
    cin >> n;

    priority_queue<Node*, vector<Node*>, Compare> pq;

    char ch;
    int freq;

    cout << "Enter character and frequency:\n";

    for (int i = 0; i < n; i++) {
        cin >> ch >> freq;
        pq.push(new Node(ch, freq));
    }

    // Build Huffman Tree
    while (pq.size() > 1) {
        Node* left = pq.top();
        pq.pop();

        Node* right = pq.top();
        pq.pop();

        Node* parent = new Node('$', left->freq + right->freq);

        parent->left = left;
        parent->right = right;

        pq.push(parent);
    }

    // Generate Huffman codes
    cout << "\nHuffman Codes:\n";
    printCodes(pq.top(), "");

    return 0;
}
