/*
Book: Algorithms 4th Edition, MIT. 1.1.9
Write a code fragment that puts the binary representation of a positive integer N
into a String s.
*/

package com.alayo;

public class IntToBinary1 {
    public static void convert(int N){
        StringBuilder s = new StringBuilder("");
        for (int n = N; n > 0; n /=2)
            s.append((n % 2));
        s.reverse();
        System.out.println(s);
    }
}
