import java.util.*;
import java.io.*;

public class BOJ13398_ContinuousSum2 {
	
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] nums = new int[N];
		for(int i=0; i<N; i++) nums[i] = sc.nextInt();
		
		int[] until = new int[N]; // until[i]: using until i-th number
		int[] from = new int[N]; // from[i]: using from i-th number
		
		until[0] = nums[0];
		for(int i=1; i<N; i++) {
			until[i] = Math.max(nums[i], until[i-1]+nums[i]);
		}
		from[N-1] = nums[N-1];
		for(int i=N-2; i>=0; i--) {
			from[i] = Math.max(nums[i], from[i+1]+nums[i]);
		}
		
		int ans = nums[0];
		// Same as usual continuous sum
		for(int i=0; i<N; i++) {
			if(until[i] > ans) ans = until[i];
		}
		// If you remove i-th number,
		// largest sum = (largest sum using until i-1 th num) + (largest sum using until i+1 th num)
		for(int i=1; i<N-1; i++) {
			if(until[i-1]+from[i+1] > ans) ans = until[i-1]+from[i+1];
		}
	
		System.out.println(ans);
		
		sc.close();
	}

}
