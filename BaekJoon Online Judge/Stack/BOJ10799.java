import java.util.*;
import java.io.*;



public class BOJ10799 {
	
	public static void main(String[] args) throws Exception{

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		String s = br.readLine();
		int result = 0;
		int paren = 0;
		boolean was_open = false;
		for(Character c: s.toCharArray()) {
			if(c == '(') {
				if(was_open) {
					paren += 1;
					result += 1;
				}
				was_open = true;
			}
			else {
				// lazor
				if(was_open) {
					result += paren;
				}
				else {
					paren -= 1;
				}
				was_open = false;
			}
		}
		System.out.println(result);
		
		
		
		br.close();
		bw.close();

	}

}
