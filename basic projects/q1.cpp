#include<bits/stdc++.h>
using namespace std;
class nQueens{
    vector<vector<int>> matrix;
    vector<string> out;
    int size;
    bool check(vector<vector<int>>& matrix,int i,int j,int n){
        for(int k=0;k<n;k++){
            if(matrix[k][j]==1){
                return 0;
            }
        }
        for(int k=0;k<n;k++){
            if(matrix[i][k]==1){
                return 0;
            }
        }
        int checkI=i,checkJ=j;
        while(checkI && checkJ){
            if(matrix[checkI][checkJ]){
                return 0;
            }
            checkI--;
            checkJ--;
        }
        return 1;
    }
    bool recursion(int i,vector<vector<int>>& matrix,int n,string& curr){
        if(i==size){out.push_back(curr);return 0;}
        int canBe =0;
        for(int j=0;j<size;j++){
            if(check(matrix,i,j,n)){
                matrix[i][j]=1;string temp ="q";
                    temp+=to_string(i);
                    temp+=to_string('-');
                    temp+=to_string(j);
                    curr+=temp;
                if(recursion(i+1,matrix,n,curr)){
                    canBe=1;
                }else{
                    curr.pop_back();
                }
                matrix[i][j]=0;
            }
        }
        return canBe;
    }
    public:
    nQueens(int n){
        matrix.resize(n);
        size=n;
    }
    vector<string> solve(){
        int isPossible=0;
        for(int i=0;i<size;i++){
            matrix[0][i]=1;
            string cur;
            if(recursion(i,matrix,size,cur)){
                isPossible=1;
            }
            matrix[0][i]=0;
        }
        if(isPossible==0){
            return {};
        }
        return out;
    }
};
int main(){
    int n;
    cin>>n;
    nQueens queens(n);
    vector<string> final = queens.solve();
    for(auto e:final){
        cout<<e<<endl;
    }
}