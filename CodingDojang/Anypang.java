// reference: http://codingdojang.com/scode/583?answer_mode=hide

package test;

import java.util.*;

class Coord{
	public int x;
	public int y;
	Coord(int x, int y){
		this.x = x;
		this.y = y;
	}
	public String toString() {
		return String.format("(%d,%d)", this.x, this.y);
	}
}

// 5x5 board
// More than 3 same numbers(row/column) continuously => pang!
// Pang => turns into zero => numbers above it fall down to fill the board
public class Anypang {
	static void printBoard(int[][] board) {
		for(int i=0;i<board.length;i++) {
			System.out.println(Arrays.toString(board[i]));
		}
	}
	
	static void pang(int[][] board, List<Coord> pangs) {
		for(Coord coord: pangs) {
			board[coord.x][coord.y] = 0;
		}
	}
	
	static void fill(int[][] board) {
		List<Integer> verLine;
		int idx;
		for(int j=0;j<5;j++) {
			idx = 4;
			verLine = new ArrayList<Integer>();
			for(int i=0;i<5;i++) {
				if(board[i][j] != 0) {
					verLine.add(board[i][j]);					
				}
			}
			while(!verLine.isEmpty()) {
				board[idx--][j] = verLine.remove(verLine.size()-1);
			}
			while(idx>=0) {
				board[idx--][j] = 0;
			}
		}
			
	}
	
	static List<Coord> horizontalPangs(int[][] board) {
		int last;
		// 각 가로줄에서 연속된 부분의 y좌표를 담을 임시 공간
		Set<Integer> idx = new HashSet<Integer>();
		 // 팡 터질 좌표들
		List<Coord> pangs = new ArrayList<Coord>();
		for(int i=0;i<5;i++) {
			last = board[i][0];
			idx.clear();
			idx.add(0);
			for(int j=1;j<5;j++) {
				// same number => add that index and the last index
				if(board[i][j] == last && last != 0) {
					idx.add(j);
					idx.add(j-1);
				// different number before 3 same numbers => reset the index
				}else if(board[i][j] != last && idx.size()<3) {
					idx.clear();
				// different number after more than 3 same numbers => done
				}else if(board[i][j] != last && idx.size()>=3) {
					break;
				}
				last = board[i][j];
			}
			if(idx.size()>=3) {
				for(int j:idx) {
					pangs.add(new Coord(i,j));
				}
			}
		}
		return pangs;
	}
	static List<Coord> verticalPangs(int[][] board) {
		int last;
		// 각 세로줄에서 연속된 부분의 x좌표를 담을 임시 공간
		Set<Integer> idx = new HashSet<Integer>();
		// 팡 터질 좌표들
		List<Coord> pangs = new ArrayList<Coord>();
		for(int j=0;j<5;j++) {
			last = board[0][j];
			idx.clear();
			idx.add(0);
			for(int i=1;i<5;i++) {
				if(board[i][j] == last && last != 0) {
					idx.add(i);
					idx.add(i-1);
				}else if(board[i][j] != last && idx.size()<3) {
					idx.clear();
				}else if(board[i][j] != last && idx.size()>=3) {
					break;
				}
				last = board[i][j];
			}
			if(idx.size()>=3) {
				for(int i:idx) {
					pangs.add(new Coord(i,j));
				}
			}
		}
		return pangs;
	}
	
	public static void main(String[] args) {
		int[][] board = new int[][] {
			{2,4,1,2,1},
			{3,4,2,3,3},
			{2,4,1,2,2},
			{4,4,4,1,2},
			{4,2,3,3,2}
		};
		while(true) {
			List<Coord> pangs = horizontalPangs(board);
			pangs.addAll(verticalPangs(board));
			System.out.println(pangs);
			if(pangs.size()==0) {
				break;
			}else {
				pang(board,pangs);
				fill(board);
			}
			printBoard(board);
			System.out.println("===================");
		}


	}
}	
