import java.util.*;
import java.io.*;

public class BOJ11054_LongestBitonicSequence {
	
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] nums = new int[N+1];
		for(int i=1; i<=N; i++) nums[i] = sc.nextInt();
		
		// inc[N]: longest sequence with N nums, with N-th number used in increasing part
		// dec[N]: longest sequence with N nums, with N-th number used in decreasing part
		int[] inc = new int[N+1];
		int[] dec = new int[N+1];
		
		for(int i=1; i<=N; i++) {
			int _inc = 0;
			int _dec = 0;
			for(int j=0; j<i; j++) {
				if(nums[j] < nums[i] && inc[j]+1 > _inc) _inc = inc[j]+1;
				if(nums[j] > nums[i]) {
					// Case where it starts to decrease from the i-th number
					if(inc[j]+1 > _dec) _dec = inc[j]+1;
					// Case where it Keeps decreasing
					if(dec[j]+1 > _dec) _dec = dec[j]+1;
				}
			}
			inc[i] = _inc;
			dec[i] = _dec;
		}
		
		int ans = 0;
		for(int i=1; i<=N; i++) {
			if(inc[i] > ans) ans = inc[i];
			if(dec[i] > ans) ans = dec[i];
		}
		System.out.println(ans);
		
		sc.close();
	}

}
