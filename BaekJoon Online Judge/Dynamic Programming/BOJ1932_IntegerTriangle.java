import java.util.*;
import java.io.*;

public class BOJ1932_IntegerTriangle {
	
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[][] triangle = new int[N][N];
		int[][] A = new int[N][N];
		
		for(int i=0; i<N; i++) {
			for(int j=0; j<=i; j++) {
				triangle[i][j] = sc.nextInt();
			}
		}
		
		A[0][0] = triangle[0][0];
		for(int i=1; i<N; i++) {
			for(int j=0; j<=i; j++) {
				if(j==0) A[i][j] = A[i-1][0] + triangle[i][j];
				else if(j==i) A[i][j] = A[i-1][j-1] + triangle[i][j];
				else A[i][j] = Math.max(A[i-1][j-1], A[i-1][j]) + triangle[i][j];
			}
		}
		
		int ans = 0;
		for(int j=0; j<N; j++) {
			if(A[N-1][j] >= ans) ans = A[N-1][j];
		}
		System.out.println(ans);
		
		sc.close();
	}

}
