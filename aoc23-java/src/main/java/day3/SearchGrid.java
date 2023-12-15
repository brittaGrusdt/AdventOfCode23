package day3;

public class SearchGrid {

	private int start_col;
	private int end_col;
	private int start_row;
	private int end_row;
	
	public SearchGrid(int row, int col, int len, int nbRows, int nbCols) {
		int end_col = col + len;
		end_col = end_col >= nbCols ? nbCols - 1 : end_col;
		this.end_col = end_col;
		this.start_col = col > 0 ? col-1 : 0;
		
		this.start_row = row == 0 ? row : row-1;
		this.end_row = row == nbRows - 1 ? row : row + 1;
	}

	public int getStart_col() {
		return start_col;
	}


	public int getEnd_col() {
		return end_col;
	}

	public int getStart_row() {
		return start_row;
	}


	public int getEnd_row() {
		return end_row;
	}

	
}
