package com.alayo;

import java.util.Stack;

public class ValidParenthesisSol2 {
    public static boolean isValid(String s) {
        if (s.length() % 2 != 0)
            return false;
        else if (s.charAt(0) == ')' || s.charAt(0) == ']' || s.charAt(0) == '}') return false;
        else {
            Stack<Character> st = new Stack<>();
            for (int i = 0; i < s.length(); i++) {
                if (s.charAt(i) == '(' || s.charAt(i) == '{' || s.charAt(i) == '[')
                    st.push(s.charAt(i));
                else
                    if (!st.isEmpty()) {
                        if (s.charAt(i) == ')')
                            if(st.peek() != '(') return false;
                            else st.pop();
                        if (s.charAt(i) == ']')
                            if(st.peek() != '[') return false;
                            else st.pop();
                        if (s.charAt(i) == '}')
                            if(st.peek() != '{') return false;
                            else st.pop();
                    }
                    else if (i < s.length()-1)
                        return false;
            }
            return st.isEmpty();
        }
    }
}
