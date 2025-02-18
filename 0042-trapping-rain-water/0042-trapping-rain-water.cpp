class Solution {
public:
    int trap(vector<int>& height) {
        int n=height.size();
        vector<int>lt;
        vector<int>rt;
        int max=0;
        for(int i=0;i<n;i++){
            if(max<=height[i])  max=height[i];
            lt.push_back(max);
        }
        max=0;
        for(int i=n-1;i>=0;i--){
            if(max<height[i])  max=height[i];
            rt.push_back(max);
        }
        reverse(rt.begin(),rt.end());
        long long ans=0;
        for(int i=0;i<n;i++){
            if(lt[i]<rt[i]){
                ans=ans+abs(lt[i]-height[i]);
            }
            else{
                ans=ans+abs(rt[i]-height[i]);
            }
        }
        return ans;
    }
};