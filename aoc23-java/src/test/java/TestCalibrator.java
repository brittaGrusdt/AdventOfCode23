

import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

import org.apache.commons.collections4.CollectionUtils;
import org.junit.jupiter.api.Test;

import utils.AdventOfCode;
import day1.Calibrator;

class TestCalibrator {

	
	@Test
	void testGetCalibratorValues() {
		Scanner scanner = AdventOfCode.getScanner("src/test/resources/", "test-input-day1.txt");		
		List<Integer> calibrations = Calibrator.getCalibratorValues(scanner);
		List<Integer> result = Arrays.asList(12, 38, 15, 77);
		System.out.println(calibrations.toString());
		assertTrue(CollectionUtils.isEqualCollection(calibrations, result));
	}
	
	@Test
	void testSum() {
		Scanner scanner = AdventOfCode.getScanner("src/test/resources/", "test-input-day1.txt");		
		List<Integer> calibrations = Calibrator.getCalibratorValues(scanner);
		int summedValue = Calibrator.sumOfCalibrationValues(calibrations);
		assertTrue(summedValue == 142);
	}
	
	
	@Test
	void testTask2() {
		Scanner scanner = AdventOfCode.getScanner("src/test/resources/", "test-input-day1-task2.txt");	
		List<Integer> calibrations = Calibrator.getCalibratorValuesTask2(scanner);
		List<Integer> result = Arrays.asList(29, 83, 13, 24, 42, 14, 76);
		System.out.println(calibrations.toString());
		assertTrue(CollectionUtils.isEqualCollection(calibrations, result));
		
		int summedValue = Calibrator.sumOfCalibrationValues(calibrations);
		assertTrue(summedValue == 281);
	}
	
	
	@Test
	void testTask2OwnExamples() {
		Scanner scanner = AdventOfCode.getScanner("src/test/resources/", "test-day1-task2.txt");	
		List<Integer> calibrations = Calibrator.getCalibratorValuesTask2(scanner);
		List<Integer> result = Arrays.asList(83, 79, 22, 82, 81, 13, 13, 12, 12, 55, 55, 11, 14, 38, 14, 38);
		System.out.println(calibrations.toString());
		assertTrue(CollectionUtils.isEqualCollection(calibrations, result));
		int summedValue = Calibrator.sumOfCalibrationValues(calibrations);
		assertTrue(summedValue == 622);
	}
	
	@Test
	void testTask2ExamplesFromInput() {
		Scanner scanner = AdventOfCode.getScanner("src/test/resources/", "day1-task2.txt");	
		List<Integer> calibrations = Calibrator.getCalibratorValuesTask2(scanner);
		List<Integer> result = Arrays.asList(72, 37, 41, 24, 54, 56, 26, 92, 76, 47);
		System.out.println(calibrations.toString());
		assertTrue(CollectionUtils.isEqualCollection(calibrations, result));
		int summedValue = Calibrator.sumOfCalibrationValues(calibrations);
		assertTrue(summedValue == 525);
	}
}
