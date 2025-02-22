class Solution {
    public int countPrimes(int n) {
        boolean[] arr = new boolean[n];
        Arrays.fill(arr,true);

        int p=2;
        while(p*p<=n){
            if(arr[p]==true){
                for(int i=p*p;i<n;i+=p){
                    arr[i]=false;
                }
            }
            p+=1;
        }
        int c=0;
        for(int i=2;i<n;i++){
            if(arr[i]==true){
                c+=1;
            }
        }
        return c;
    }
}