import java.util.*;
import java.io.*;

public class BOJ9465_Sticker {
	
	public static void main(String[] args) throws Exception{

		Scanner sc = new Scanner(System.in);
		int T= sc.nextInt();
		for(int t=0 ;t<T; t++) {
			int N = sc.nextInt();
			int[][] scores = new int[N+1][3];
			for(int i=1; i<=2; i++) {
				for(int j=1; j<=N; j++) {
					scores[j][i] = sc.nextInt();
				}
			}
			
			// A[N][0]: Max score with N columns, with 0 sticker at N-th row
			// A[N][1]: Max score with N columns, with first sticker at N-th row
			// A[N][2]: Max score with N columns, with second sticker at N-th row
			int[][] A = new int[N+1][3];
			for(int i=1; i<N+1; i++) {
				A[i][0] = Math.max(A[i-1][1], A[i-1][2]);
				A[i][1] = Math.max(A[i-1][0], A[i-1][2]) + scores[i][1];
				A[i][2] = Math.max(A[i-1][0], A[i-1][1]) + scores[i][2];
			}
			System.out.println(Math.max(A[N][1], A[N][2]));
		}
		
		
		sc.close();
	}

}
