import java.util.*;
import java.io.*;



public class BOJ17298 {
	
	public static void main(String[] args) throws Exception{

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int N = Integer.parseInt(br.readLine());
		String[] input = br.readLine().split(" ");
		int[] nums = new int[N];
		for(int i=0; i < N; i++) {
			nums[i] = Integer.parseInt(input[i]);
		}
		
		int[] results = new int[N];
		Stack<Integer> not_found = new Stack<>();
		not_found.push(0);
		for(int i=0; i < N; i++) {
			while(!not_found.isEmpty() && nums[not_found.peek()] < nums[i]) {
				results[not_found.pop()] = nums[i];
			}
			not_found.push(i);
		}
		while(!not_found.isEmpty()) {
			results[not_found.pop()] = -1;
		}
		
		StringBuilder sb = new StringBuilder();
		for(int num: results) {
			sb.append(num + " ");
		}
		System.out.println(sb.toString().trim());
		
		br.close();
		bw.close();

	}

}
