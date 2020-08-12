import java.io.*;

public class BOJ1463_MakeOne {
	static int[] results;
	
	static int make_one(int n) {
		if(n == 1) return 0;
		if(results[n] > 0) return results[n];
		
		int min = make_one(n-1) + 1;
		if(n % 3 == 0) min = Math.min(min, make_one(n/3) + 1);
		if(n % 2 == 0) min = Math.min(min, make_one(n/2) + 1);
		results[n] = min;
		return min;
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		results = new int[n+1];
				
		System.out.println(make_one(n));
		
		
	}
}
