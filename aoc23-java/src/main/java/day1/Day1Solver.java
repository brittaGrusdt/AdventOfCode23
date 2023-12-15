package day1;

import java.util.List;
import java.util.Scanner;

import utils.AdventOfCode;

public class Day1Solver {

	public static void runTask1() {
		Scanner scanner = AdventOfCode.getScanner("input-day1.txt");
		List<Integer> values = Calibrator.getCalibratorValues(scanner);
		int summedValue = Calibrator.sumOfCalibrationValues(values);
		System.out.println("summed calibration values: " + summedValue);		
	}
	
	public static void runTask2() {
		Scanner scanner = AdventOfCode.getScanner("input-day1.txt");
		List<Integer> values = Calibrator.getCalibratorValuesTask2(scanner);
		int summedValue = Calibrator.sumOfCalibrationValues(values);
		System.out.println("summed calibration values: " + summedValue);
		
//		for(int n : values) {
//			System.out.println(n);
//		}
	}
	
	public static void main(String[] args) {
		runTask1();
		runTask2();
	}
}
