/*
Book: Algorithms 4th Edition, MIT. 1.1.14
Write a static method lg() that takes an int value N as argument and returns
the largest int not larger than the base-2 logarithm of N . Do not use Math.
*/

package com.alayo;

public class IntLowerThanLog2 {
    public static void compute(int N) {
        int x = 0;
        for (int i = N; i > 0; i /= 2) x++;
        System.out.println(--x);
    }
}
