import java.util.*;
import java.io.*;


// Start with the minimum number, go in increasing order. If found, that's the min value
// Start with the maximum number, go in decreasing order. If found, that's the max value
public class BOJ2529_Inequality2 {
	static long ans_max = 0;
	static long ans_min = 9999999999L;
	static String[] sign;
	static int k;
	static boolean[] used = new boolean[10];
	static boolean found_min, found_max;
	
	static boolean possible(String s, int a, int b) {
		return (s.charAt(0)=='>' && a>b) || (s.charAt(0)=='<' && a<b);
	}
	
	static void find_min(int idx, String num) {
		if(idx == k+1) {
			ans_min = Long.parseLong(num);
			found_min = true;
			return;
		}
		
		for(int i=0; i<10; i++) {
			if(!found_min && !used[i]) {
				if(idx == 0 || possible(sign[idx-1],Character.getNumericValue(num.charAt(idx-1)),i)) {
					used[i] = true;					
					find_min(idx+1, num+i);
					used[i] = false;
				}
			}
		}
	}
	
	static void find_max(int idx, String num) {
		if(idx == k+1) {
			ans_max = Long.parseLong(num);
			found_max = true;
			return;
		}
		
		for(int i=9; i>=0; i--) {
			if(!found_max && !used[i]) {
				if(idx == 0 || possible(sign[idx-1],Character.getNumericValue(num.charAt(idx-1)),i)) {
					used[i] = true;					
					find_max(idx+1, num+i);
					used[i] = false;
				}
			}
		}
	}
	
	
	public static void main(String args[]) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		k = Integer.parseInt(br.readLine());
		sign = br.readLine().split(" ");

		
		find_min(0, "");
		find_max(0, "");
		
		if(String.valueOf(ans_max).length() < k+1) System.out.println("0" + ans_max);
		else System.out.println(ans_max);
		
		if(String.valueOf(ans_min).length() < k+1) System.out.println("0" + ans_min);
		else System.out.println(ans_min);

		
		
	}
}
