import java.util.*;
import java.io.*;



public class BOJ17299 {
	
	public static void main(String[] args) throws Exception{

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int N = Integer.parseInt(br.readLine());
		String[] input = br.readLine().split(" ");
		int[] nums = new int[N];
		HashMap<Integer, Integer> freq = new HashMap<>();
		for(int i=0; i < N; i++) {
			nums[i] = Integer.parseInt(input[i]);
			freq.put(nums[i], freq.getOrDefault(nums[i], 0) + 1);
		}
		
		int[] results = new int[N];
		Stack<Integer> not_found = new Stack<>();
		not_found.push(0);
		for(int i=0; i < N; i++) {
			while(!not_found.isEmpty() && freq.get(nums[not_found.peek()]) < freq.get(nums[i])) {
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
