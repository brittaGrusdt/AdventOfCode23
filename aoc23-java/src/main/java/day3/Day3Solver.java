package day3;

import java.util.List;
import java.util.stream.Collectors;

import utils.AdventOfCode;


public class Day3Solver {

	private EngineSchema schema;
	
	public Day3Solver(String path, String filename) {
		String input = AdventOfCode.getInputString(path, filename);
		String[] lines = input.split("\n");
		System.out.println("nb lines read: " + lines.length);
		EngineSchema schema = new EngineSchema(lines);
		this.schema = schema;
	}
	
	public void runTask1() {
		List<Long> partNumbers = schema.getPartNumbers()
				.stream().map(n -> n.number()).collect(Collectors.toList());
		long sum = partNumbers.stream().mapToLong(Long::longValue).sum();
		System.out.println("Sum of all part numbers is: " + sum);
//		schema.printSymbols(130, 140);
//		schema.printPartNumbers(0, 140);
	}
	
	public void runTask2(boolean verbose) {
		List<Long> gearRatios = schema.getGearRatios(verbose);
		long sumGearRatios = gearRatios.stream().mapToLong(Long::longValue).sum();
		System.out.println("Sum of all gear ratios is: " + sumGearRatios + " (from " + gearRatios.size() + ") gears.");
	}
	
	
	public static void main(String[] args) {
		Day3Solver solver = new Day3Solver("src/main/resources/", "input-day3.txt");
		solver.runTask1();
		solver.runTask2(false);
	}

}
