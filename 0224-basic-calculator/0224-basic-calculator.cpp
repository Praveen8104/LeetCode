class Solution {
public:
    int pre(char op) {
        if (op == '+' || op == '-')
            return 2;
        return 0;
    }
    int ope(int a, int b, char op) {
        if (op == '+') {
            return a + b;
        } else if (op == '-') {
            return a - b;
        } else {
            return a * b;
        }
    }
    int calculate(string s) {
        string s1;
        for (auto i:s) if (i!=' ') s1 += i;
        int i;
        stack<int> nums;
        stack<char> ops;
        if(s1[0]=='-')
            {
                nums.push(0);
            }
        for (i = 0; i < s1.length(); i++) {
            
            if (isspace(s1[i])) {
                continue;
            } else if (s1[i] == '(') {
                if(!isdigit(s1[i+1])){
                    nums.push(0);
                }
                ops.push(s1[i]);
            } else if (isdigit(s1[i])) {
                int n = 0;
                while (isdigit(s1[i])) {
                    n = (n * 10) + (s1[i] - '0');
                    i++;
                }
                nums.push(n);
                i--;
            } else if (s1[i] == ')') {
                while (!ops.empty() && ops.top() != '(') {
                    int v2 = nums.top();
                    nums.pop();

                    int v1 = nums.top();
                    nums.pop();

                    char op = ops.top();
                    ops.pop();

                    nums.push(ope(v1, v2, op));
                }
                if(!ops.empty())
                ops.pop();
            } else {
                while (!ops.empty() && pre(s1[i]) <= pre(ops.top())) {
                    int v2 = nums.top();
                    nums.pop();

                    int v1 = nums.top();
                    nums.pop();

                    char op = ops.top();
                    ops.pop();

                    nums.push(ope(v1, v2, op));
                }
                ops.push(s1[i]);
            }
        }

        while (!ops.empty()) {
            int v2 = nums.top();
            nums.pop();

            int v1 = nums.top();
            nums.pop();

            char op = ops.top();
            ops.pop();

            nums.push(ope(v1, v2, op));
        }
        return (nums.top());
    }
};