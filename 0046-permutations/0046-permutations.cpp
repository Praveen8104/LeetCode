class Solution {
public:
    vector<vector<int>>v;
    void solve(vector<int>s,int start,int end){
        if(start>=end){
            v.push_back(s);
            return;
        }
        for(int i=start;i<=end;i++){
            swap(s[start],s[i]);
            solve(s,start+1,end);
            swap(s[start],s[i]);
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        solve(nums,0,nums.size()-1);
        return v;
    }
};