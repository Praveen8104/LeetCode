class Solution {
public:
vector<vector<int>>py;
void feb(vector<int>Nums, int index, vector<int>ans, int target, int size, int mysum,int k){
    if(index >= size and mysum!=target){
        return;
    }
    else if(mysum  == target){
        if(ans.size()==k){
        py.push_back(ans);}
        return;
    }   
    else if(mysum > target){
        return;
    }
    ans.push_back(Nums[index]);
    feb(Nums,index+1,ans,target,size,mysum+Nums[index],k);
    while(index+1 < size && Nums[index] == Nums[index+1]) index++;
    ans.pop_back();
    feb(Nums,index+1,ans,target,size,mysum,k);
}
    vector<vector<int>> combinationSum3(int k, int target) {
        vector<int>Nums={1,2,3,4,5,6,7,8,9};
        int n = Nums.size();
        feb(Nums,0,{},target,n,0,k);
        py.erase(unique(py.begin(),py.end()),py.end());
        return py;
    }
};