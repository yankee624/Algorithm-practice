import java.io.*;

public class BOJ9095_add123 {
	static int[] results = new int[11+1];
	
	static int count_ways(int n) {
		if(n == 0) return 1;
		if(results[n] > 0) return results[n];
		
		int count = 0;
		for(int i=1; i<=3; i++) {
			if(n-i >= 0) count += count_ways(n-i);
		}
		results[n] = count;
		return count;
	}

	
	public static void main(String[] args) throws Exception {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		results[0] = 1;
		for(int i=0; i<T; i++) {
			int n = Integer.parseInt(br.readLine());
			System.out.println(count_ways(n));
		}
		
		
	}
}
