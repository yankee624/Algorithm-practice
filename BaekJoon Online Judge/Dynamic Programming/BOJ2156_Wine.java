import java.util.*;
import java.io.*;

public class BOJ2156_Wine {
	
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] amounts = new int[N+1];
		for(int i=1; i<=N; i++) {
			amounts[i] = sc.nextInt();
		}
		
		// A[N][0]: Maximum amount using N wines, choosing N-th wine
		// A[N][1]: Maximum amount using N wines, not choosing N-th wine
		int[][] A = new int[N+1][2];
		A[1][1] = amounts[1];
		for(int i=2; i<=N; i++) {
			A[i][0] = Math.max(A[i-1][0], A[i-1][1]);
			A[i][1] = Math.max(A[i-1][0], A[i-2][0]+amounts[i-1]) + amounts[i];
		}
		System.out.println(Math.max(A[N][0], A[N][1]));
		
		sc.close();
	}

}
