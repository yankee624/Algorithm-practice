import java.util.*;
import java.io.*;

public class BOJ1476_CalculateYear {
	
	public static void main(String[] args) throws Exception{

		Scanner sc = new Scanner(System.in);
		// (TargetYear-1) % 15 = E
		// (TargetYear-1) % 28 = S
		// (TargetYear-1) % 19 = M
		int E = sc.nextInt() - 1;
		int S = sc.nextInt() - 1;
		int M = sc.nextInt() - 1;
		
		// year = TargetYear - 1
		int year = 0;
		for(int i=0;;i++) {
			year = i*15 + E;
			if(year % 28 == S && year % 19 == M) break;
		}
		
		System.out.println(year+1);
		sc.close();
	}

}
