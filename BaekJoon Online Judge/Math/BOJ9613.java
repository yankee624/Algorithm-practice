import java.io.*;

public class BOJ9613 {
	static int gcd(int a, int b) {
		if(b == 0) return a;
		return gcd(b, a%b);
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		for(int i=0; i<N; i++) {
			String[] testCase = br.readLine().split(" ");
			long sum = 0; // int: overflow possible
			int n = Integer.parseInt(testCase[0]);
			int[] nums = new int[n];
			for(int j=0; j<n; j++) {
				nums[j] = Integer.parseInt(testCase[j+1]);
			}
			
			for(int j=0; j<n; j++) {
				for(int k=j+1; k<n; k++) {
					sum += gcd(nums[j], nums[k]);
				}
			}
			System.out.println(sum);
		}
		
		
		
	}
}
