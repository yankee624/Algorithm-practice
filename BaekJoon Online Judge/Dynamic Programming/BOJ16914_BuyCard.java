import java.io.*;
import java.util.Arrays;

public class BOJ16914_BuyCard {
	
	public static void main(String[] args) throws Exception {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		String[] s = br.readLine().split(" ");
		
		int[] ans = new int[N+1];
		int[] prices = new int[N+1];
		for(int i=1; i<=N; i++) {
			prices[i] = Integer.parseInt(s[i-1]);
			ans[i] = prices[i];
		}
		
		for(int i=1; i<=N; i++) {
			for(int j=1; j<=i; j++) {
				ans[i] = Math.min(ans[i], prices[j] + ans[i-j]);
			}
		}
		
		System.out.println(ans[N]);
		
	}
}
