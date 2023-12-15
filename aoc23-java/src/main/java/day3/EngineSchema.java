package day3;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

public class EngineSchema {

	private String[] input;
	private List<List<Symbol>> symbols;
	private List<PartNumber> partNumbers;

	
	public EngineSchema(String[] input) {
		this.input = input;
		initSymbols();
		initPartNumbers();
	}
	
	private void initSymbols() {
		Pattern pattern = Pattern.compile("[^\\d\\.]+");
		List<List<Symbol>> allSymbols = new ArrayList<List<Symbol>>();
		
		for(int row=0; row<input.length; row++) {
			String line = input[row];
			List<Symbol> symbolsInLine = new ArrayList<Symbol>();			
			Matcher matcher = pattern.matcher(line);
			int col = 0;
			while(matcher.find()) {
				String sign = matcher.group();
				col = line.indexOf(sign, col);
				symbolsInLine.add(new Symbol(sign, row, col));
				col += 1;
			}
			allSymbols.add(symbolsInLine);
		}
		symbols = allSymbols;
	}
	
	private void initPartNumbers() {
		Pattern pattern = Pattern.compile("\\d+");
		List<PartNumber> partNumbers = new ArrayList<PartNumber>();
		for(int row = 0; row < input.length; row++) {
			String line = input[row];
			List<PartNumber> partNumbersLine = searchPartNumbersInLine(line, pattern, row);
			partNumbers.addAll(partNumbersLine);
		}
		this.partNumbers = partNumbers;
	}
	
	
	public List<PartNumber> getPartNumbers() {
		return partNumbers;
	}

	public String[] getInput() {
		return input;
	}
	
	public List<List<Symbol>> getSymbols() {
		return symbols;
	}

	
	public void printSymbols(int startLine, int endLine) {
		int maxRow = startLine + endLine; 
		if(maxRow >= symbols.size()) maxRow = symbols.size() - 1;
		
		for(int row=startLine; row <= maxRow; row++) {
			List<Symbol> symbolsLine = symbols.get(row);
			List<String> line = new ArrayList<String>();
			List<Integer> colIndices = new ArrayList<Integer>();
			for(Symbol s : symbolsLine) {
				line.add(s.sign());
				colIndices.add(s.col());
			}
			System.out.println("line " + (row+1) + ": " + line.toString() + "; " + colIndices.toString());
		}
	}
	
	public void printPartNumbers(int startLine, int endLine) {
		int maxRow = startLine + endLine >= symbols.size() ? symbols.size() - 1 : startLine + endLine; 
		List<PartNumber> selectedNumbers = this.partNumbers
				.stream().filter(partNb -> partNb.row() >= startLine && partNb.row() <= maxRow)
				.collect(Collectors.toList());
		System.out.println(selectedNumbers.toString());
	}
	
	
	private boolean checkIfPartNumber(int start_row, int start_col, int end_row, int end_col) {
		boolean isPartNumber = false;
		for(int row = start_row; row <= end_row; row++) {
			List<Symbol> symbolsInLine = symbols.get(row);
			if(symbolsInLine.size() == 0) continue;
			
			List<Symbol> matchingSymbols = symbolsInLine.stream()
				.filter(symbol -> symbol.col() >= start_col && symbol.col() <= end_col)
				.collect(Collectors.toList());
			
			if(matchingSymbols.size() > 0) {
				isPartNumber = true;
				break;
			}
		}
		return isPartNumber;
	}
	
	
	private List<PartNumber> searchPartNumbersInLine(String line, Pattern pattern, int row){
		int ncols = line.length();
		Matcher matcher = pattern.matcher(line);
		int col = 0;
		List<PartNumber> partNumbers = new ArrayList<PartNumber>();
		while(matcher.find()) {
			String number = matcher.group().trim();
			col = line.indexOf(number, col);
			
			SearchGrid grid = new SearchGrid(row, col, number.length(), input.length, ncols);
				
			if(checkIfPartNumber(grid.getStart_row(), grid.getStart_col(), grid.getEnd_row(), grid.getEnd_col())) {
				PartNumber partNumber = new PartNumber(Integer.parseInt(number), row, col);
				partNumbers.add(partNumber);
			}

			col += number.length();
		}
		return partNumbers;
	}	
	
	
	private boolean partNumberInGridColumns(PartNumber pn, SearchGrid grid) {
		boolean isWithin = pn.col() >= grid.getStart_col() && pn.col() <= grid.getEnd_col();
		
		int endPN = pn.col() + String.valueOf(pn.number()).length() - 1;
		int startPN = pn.col();
		// important: start of partNumber must not be after end of search grid column! 
		boolean startPNBeforeSearchStart =  endPN >= grid.getStart_col() && !(startPN > grid.getEnd_col());
		return isWithin || startPNBeforeSearchStart;
	}
	
	private boolean partNumberInGridRows(PartNumber pn, SearchGrid grid) {
		return pn.row() >= grid.getStart_row() && pn.row() <= grid.getEnd_row();
	}
	
	private List<PartNumber> getPartNumbersIfGear(Symbol symbol, SearchGrid grid) {
		if(!symbol.sign().equals("*")) return null;
		List<PartNumber> relevantNumbers = 
				partNumbers.stream().filter(pn -> partNumberInGridColumns(pn, grid) &&
												  partNumberInGridRows(pn, grid))
				.collect(Collectors.toList());
		if(relevantNumbers.size() != 2) return null;
		return relevantNumbers;
	}
	
	public List<Long> getGearRatios(boolean verbose) {
		List<Long> gearRatios = new ArrayList<Long>();
		for(List<Symbol> symbolsLine : this.symbols) {
			for(Symbol symbol : symbolsLine) {
				SearchGrid grid = new SearchGrid(symbol.row(), symbol.col(), 1, input.length, input[0].length());
				List<PartNumber> partNumbers= getPartNumbersIfGear(symbol, grid);
				if(partNumbers != null) {
					if(verbose) {
						System.out.println("line " + (symbol.row()+1) + ", col " + symbol.col() + 
								"; part numbers: " + partNumbers.stream().map(x -> x.number())
								.collect(Collectors.toList()).toString());
					}
					long ratio = partNumbers.get(0).number() * partNumbers.get(1).number();
					gearRatios.add(ratio);
				}
			}
		}
		return gearRatios;
	}

	
}
