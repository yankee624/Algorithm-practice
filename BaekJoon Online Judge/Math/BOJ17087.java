import java.io.*;

public class BOJ17087 {
	static int gcd(int a, int b) {
		if(b == 0) return a;
		return gcd(b, a%b);
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		String[] inputs = br.readLine().split(" ");
		int N = Integer.parseInt(inputs[0]);
		int S = Integer.parseInt(inputs[1]);
		String[] pos = br.readLine().split(" ");
		
		int[] diff = new int[pos.length];
		for(int i=0; i<pos.length; i++) {
			diff[i] = Math.abs(S - Integer.parseInt(pos[i]));
		}
		
		int ans = diff[0];
		for(int i=1; i<diff.length; i++) {
			ans = gcd(ans, diff[i]);
		}
		
		System.out.println(ans);
		
		
	}
}
