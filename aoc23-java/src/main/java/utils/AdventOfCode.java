package utils;


import java.io.File;
import java.io.FileNotFoundException;
import java.util.AbstractMap;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.stream.Stream;


public class AdventOfCode {

	
	public static Scanner getScanner(String filename) {
		return(getScanner("src/main/resources/", filename, "\n"));
	}
	
	
	public static Scanner getScanner(String path, String filename, String delimiter) {
		String file = path + filename;
		Scanner scanner = null;
		try {
			scanner = new Scanner(new File(file));
			scanner.useDelimiter(delimiter);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		return(scanner);		
	}
	
	public static Scanner getScanner(String path, String filename) {
		return(getScanner(path, filename, "\n"));
	}
	
	
	public static String getInputString(String path, String filename, String delimiter) {
		Scanner scanner = getScanner(path, filename);
		List<String> inputStrings = new ArrayList<String>();
		while(scanner.hasNext()) {
			String line = scanner.next();
			inputStrings.add(line);
		}
		return inputStrings.stream().collect(Collectors.joining(delimiter));
	}
	
	public static String getInputString(String path, String filename) {
		return getInputString(path, filename, "\n");
	}
	
	/**
	 * when input is considered a matrix of nxm characters
	 * @param scanner
	 * @return
	 */
	public static Map<String, Integer> getInputSize(String path, String filename)
	{
		Scanner scanner = getScanner(path, filename);
		int numRows = 0;
		int numCols = 0;
		String line = "";
		while(scanner.hasNext()) {
			numRows += 1;
			line = scanner.next();
		}
		numCols = line.length();
		
		Map<String, Integer> size = Stream.of(
				  new AbstractMap.SimpleEntry<>("rows", numRows), 
				  new AbstractMap.SimpleEntry<>("cols", numCols))
				  .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
		
		return(size);
	}
	
	

}
