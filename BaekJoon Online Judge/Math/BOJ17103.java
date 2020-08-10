import java.io.*;
import java.util.*;

public class BOJ17103 {

	
	public static void main(String[] args) throws Exception {

		final int MAX = 1000000;
		ArrayList<Integer> primes = new ArrayList<>();
		
		boolean[] check = new boolean[MAX+1];
        for(int i=2; i <= MAX; i++) {
        	if(!check[i]) {
        		primes.add(i);
        		for(int j=i+i; j<=MAX; j+=i) { // why not i*i: possibility of overflow...
        			check[j] = true;
        		}
        	}
        }
        
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		for(int i=0; i<N; i++) {
			int num = Integer.parseInt(br.readLine());
			int count = 0;
			for(int first: primes) {
				if(first <= num/2 && !check[num - first]) {
					count += 1;
				}
			}
			System.out.println(count);
		}
		
		
	}
}
