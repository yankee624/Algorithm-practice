import java.util.*;
import java.io.*;


public class BOJ1929 {
	
	public static void main(String[] args) throws Exception {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		String[] inputs = br.readLine().split(" ");
		int a = Integer.parseInt(inputs[0]);
		int b = Integer.parseInt(inputs[1]);
		
		boolean[] check = new boolean[b+1];
		check[0] = true;
		check[1] = true;
		for(int i=2; i*i <= b; i++) {
			if(!check[i]) {
				for(int j=i*i; j <= b; j += i) {
					check[j] = true;
				}
			}
		}
		for(int i=a; i<=b; i++) {
			if(!check[i]) {
				System.out.println(i);
			}
		}
	}
}
