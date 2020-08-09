import java.io.*;

public class BOJ2004 {
	public static void main(String[] args) throws Exception {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		String[] inputs = br.readLine().split(" ");
		int a = Integer.parseInt(inputs[0]);
		int b = Integer.parseInt(inputs[1]);
		
		long two = 0;
		long five = 0;
		for(int i=a/2; i>0; i/=2) {
			two += i;
		}
		for(int i=a/5; i>0; i/=5) {
			five += i;
		}
		
		for(int i=b/2; i>0; i/=2) {
			two -= i;
		}
		for(int i=b/5; i>0; i/=5) {
			five -= i;
		}
		for(int i=(a-b)/2; i>0; i/=2) {
			two -= i;
		}
		for(int i=(a-b)/5; i>0; i/=5) {
			five -= i;
		}
		
		System.out.println(Math.min(two, five));
		
		
	}
}
