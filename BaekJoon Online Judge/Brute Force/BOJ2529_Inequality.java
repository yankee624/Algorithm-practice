import java.util.*;
import java.io.*;


public class BOJ2529_Inequality {
	static long ans_max = 0;
	static long ans_min = 9999999999L;
	static String[] sign;
	static int k;
	static boolean[] used = new boolean[10];
	
	static boolean possible(String s, int a, int b) {
		return (s.charAt(0)=='>' && a>b) || (s.charAt(0)=='<' && a<b);
	}
	
	static void go(int idx, String num) {
		if(idx == k+1) {
			long ans = Long.parseLong(num);
			if(ans > ans_max) ans_max = ans;
			if(ans < ans_min) ans_min = ans;
			return;
		}
		
		for(int i=0; i<10; i++) {
			if(!used[i]) {
				if(idx == 0 || possible(sign[idx-1],Character.getNumericValue(num.charAt(idx-1)),i)) {
					used[i] = true;					
					go(idx+1, num+i);
					used[i] = false;
				}
			}
		}
	}
	
	
	public static void main(String args[]) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		k = Integer.parseInt(br.readLine());
		sign = br.readLine().split(" ");

		
		go(0, "");
		if(String.valueOf(ans_max).length() < k+1) System.out.println("0" + ans_max);
		else System.out.println(ans_max);
		
		if(String.valueOf(ans_min).length() < k+1) System.out.println("0" + ans_min);
		else System.out.println(ans_min);

		
		
	}
}
