import java.io.*;
import java.util.*;

public class BOJ1373 {

	
	public static void main(String[] args) throws Exception {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
		StringBuilder sb = new StringBuilder();
		
		if(input.length() % 3 == 1) {
			sb.append(input.charAt(0));
		}
		else if(input.length() % 3 == 2) {
			sb.append((input.charAt(0) - '0')*2 + input.charAt(1) - '0');
		}
		
		for(int i = input.length()%3; i <= input.length()-3; i += 3) {
			sb.append((input.charAt(i) - '0')*4 + (input.charAt(i+1) - '0')*2 + (input.charAt(i+2) - '0'));
		}
		
		System.out.println(sb);
        
		
		
		
	}
}
