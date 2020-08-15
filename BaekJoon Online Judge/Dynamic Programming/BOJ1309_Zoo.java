import java.io.*;
import java.util.*;

public class BOJ1309_Zoo {
	static long[][] A;

	
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		A = new long[N+1][2];
		A[1][0] = 1;
		A[1][1] = 2;
		
		for(int i=2; i<=N; i++) {
			A[i][0] = (A[i-1][0] + A[i-1][1]) % 9901;
			A[i][1] = (2 * A[i-1][0] + A[i-1][1]) % 9901;
		}
		
		System.out.println((A[N][0] + A[N][1])%9901);
		
		sc.close();
	}
}
