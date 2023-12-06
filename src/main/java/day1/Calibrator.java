package day1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Calibrator {
	
	private static final Map<String, Integer> NUMBERS = Map.of(
			"one", 1, "two", 2, "three", 3, "four", 4, "five", 5, "six", 6, "seven", 7, "eight", 8, "nine", 9
			);
	
	private static String find2Digits(String line) {
		String digits = Arrays.asList(line.split("\\D"))
				.stream()
				.filter(s -> !s.equals(""))
				.collect(Collectors.joining(""));
		if(digits.isEmpty()) return "";
		int last = digits.length() - 1;
		String digit1 = digits.substring(0, 1);
		String digit2 = digits.substring(last, last+1);
		return digit1 + digit2;
	}
	
	public static List<Integer> getCalibratorValues(Scanner scanner) {
		List<Integer> twoDigitValues = new ArrayList<Integer>();
		while(scanner.hasNext()) {
			String line = scanner.next();
			String twoDigits = find2Digits(line);
			twoDigitValues.add(Integer.parseInt(twoDigits));
		}
		return twoDigitValues;
	}
	
	public static int sumOfCalibrationValues(List<Integer> values) {
		return values.stream().reduce(0, Integer::sum);
	}
	
	private static String getWrittenNumber(String line, boolean firstNb) {
		int idx= firstNb ? line.length() - 1 : -1;
		boolean found = false;
		String foundNb = "";
		for(String number : NUMBERS.keySet()) {
			int idxCurrent = firstNb ? line.indexOf(number) : line.lastIndexOf(number);
			found = idxCurrent != -1;
			// first written out number
			if(found && firstNb && idxCurrent < idx) {
				foundNb = number;
				idx = idxCurrent;
				if(idx==0) break;
			}
			// last written out number
			if(found && !firstNb && idxCurrent > idx) {
				foundNb = number;
				idx = idxCurrent;
			}
		}
		return foundNb;
	}
	
	public static List<Integer> getCalibratorValuesTask2(Scanner scanner){
		List<Integer> values = new ArrayList<Integer>();
		while(scanner.hasNext()) {
			String line = scanner.next();
			String twoDigits = find2Digits(line);
			
			int val1 = -1; 
			int val2 = -1;
			int idx1 = line.length();
			int idx2 = -1;
			if(!twoDigits.isEmpty()) {
				val1 = Integer.parseInt(twoDigits.substring(0, 1));
				val2 = Integer.parseInt(twoDigits.substring(1, 2));;
				idx1 = line.indexOf(twoDigits.charAt(0));
				idx2 = line.lastIndexOf(twoDigits.charAt(1)); // IMPORTANT TO USE LASTINDEXOF HERE!!!
			}
			String foundFirst = getWrittenNumber(line, true);
			String foundLast = getWrittenNumber(line, false);
			if(!foundFirst.isEmpty() && line.indexOf(foundFirst) < idx1) {
				val1 = NUMBERS.get(foundFirst);
			}
			if(!foundLast.isEmpty() && line.lastIndexOf(foundLast) > idx2) {
				val2 = NUMBERS.get(foundLast);
			}
			String result = String.valueOf(val1) + String.valueOf(val2);
			//System.out.println(result);
			int nb = Integer.parseInt(result);
			values.add(nb);
		}
		return values;
	}

}
