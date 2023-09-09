#include<bits/stdc++.h>
using namespace std;
class ParentClass{
    int value=0;
    public:
    ParentClass(){}
    ParentClass(int intialisation_value){
        value=intialisation_value;
    }
    void setValue(int initialisation_value){
        value=initialisation_value;
    }
    int function_name(){
        return 0;
    }
    int function_name(int param_1){
        return param_1;
    }
    int function_name(int param_1 , int param_2){
        return (param_1 + param_2);
    }
    int operator + (int param_1){
        return (param_1 + value);
    }
};
class ChildClass : public ParentClass{
    public:
    int function_name(){
        return 2;
    }
};
int main(){
    ParentClass firstObj;
    cout<<firstObj.function_name()<<endl;
    cout<<firstObj.function_name(1)<<endl;
    cout<<firstObj.function_name(2,3)<<endl;

    firstObj.setValue(2);
    cout<<(firstObj+5)<<endl;

    ParentClass* c = new ChildClass;
    cout<<c->function_name()<<endl;
    ChildClass* c2 = new ChildClass;
    cout<<c2->function_name()<<endl; 

    vector<int> v(1);
    cout<<v[2]<<endl;
    // cout<<e<<endl;
}