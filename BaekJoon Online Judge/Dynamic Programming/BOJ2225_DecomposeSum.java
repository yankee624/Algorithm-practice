import java.io.*;
import java.util.*;

public class BOJ2225_DecomposeSum {
	static long[][] ans;

	
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int K = sc.nextInt();
		int MOD = 1000000000;
		ans = new long[K+1][N+1];
		for(int j=0; j<=N; j++) {
			ans[1][j] = 1;
		}
		
		for(int i=2; i<=K; i++) {
			for(int j=0; j<=N; j++) {
				for(int k=0; k<=j; k++) {
					ans[i][j] += ans[i-1][j-k];
				}
				ans[i][j] %= MOD;
			}
		}
		
		System.out.println(ans[K][N]);
		
		
	}
}
