import java.io.*;
import java.util.Arrays;

public class BOJ10844_StairNum {
	
	public static void main(String[] args) throws Exception {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int mod = 1000000000;
		// ans[i][j]: number of stairNums that are length i, ends with digit j
		// use long instead of int (overflow possible)
		long[][] ans = new long[N+1][10];
		for(int j=1; j<=9; j++) ans[1][j] = 1; // exclude 0
		
		for(int i=2; i<=N; i++) {
			for(int j=0; j<=9; j++) {
				if(j >= 1) ans[i][j] += ans[i-1][j-1];
				if(j <= 8) ans[i][j] += ans[i-1][j+1];
				ans[i][j] %= mod;
			}
		}
		
		long num = 0;
		for(int j=0; j<=9; j++) num += ans[N][j];
		System.out.println(num % mod);
		
	}
}
