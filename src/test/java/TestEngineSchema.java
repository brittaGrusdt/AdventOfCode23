

import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

import org.apache.commons.collections4.CollectionUtils;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import aoc.utils.AdventOfCode;
import day3.EngineSchema;
import day3.PartNumber;
import day3.Symbol;

class TestEngineSchema {

	private static EngineSchema schema;

	@BeforeAll
	static void setup() {
		String input = AdventOfCode.getInputString("src/test/resources/", "test-input-day3.txt");
		schema = new EngineSchema(input.split("\n"));
	}
	
	@Test
	void testPartNumbers() {
		List<Long> partNumbers = schema.getPartNumbers()
				.stream().map(n -> n.number())
				.collect(Collectors.toList());
		List<Long> results = Arrays.asList(467L, 35L, 633L, 617L, 592L, 755L, 664L, 598L);
		assertTrue(CollectionUtils.isEqualCollection(partNumbers, results));
		long sum = partNumbers.stream().mapToLong(Long::longValue).sum();
		assertTrue(sum == 4361);
	}
	
	@Test
	void testPartNumbersSpecialCases() {
		String input = AdventOfCode.getInputString("src/test/resources/", "day3-own-checks.txt");
		EngineSchema schema = new EngineSchema(input.split("\n"));
		List<Long> partNumbers = schema.getPartNumbers()
				.stream()
				.map(n -> n.number())
				.collect(Collectors.toList());

		
		List<Long> results = Arrays.asList(58L, 592L, 1234567L);
		assertTrue(CollectionUtils.isEqualCollection(partNumbers, results));
	}
	
	
	@Test
	void testPartNumbersSpecialCases2() {
		String input = AdventOfCode.getInputString("src/test/resources/", "day3-fails.txt");
		EngineSchema schema = new EngineSchema(input.split("\n"));
		List<PartNumber> partNumbers = schema.getPartNumbers();
		
		List<Long> line1 = Arrays.asList(450L);
		List<Long> line2 = Arrays.asList(546L, 944L, 588L, 875L, 772L, 587L, 98L, 941L, 638L, 534L, 271L, 73L, 56L);
		List<Long> line3 = Arrays.asList(787L, 173L, 139L, 368L, 838L, 547L);

		List<PartNumber> pnLine1 = partNumbers.stream().filter(pn -> pn.row() == 0).collect(Collectors.toList());
		List<PartNumber> pnLine2 = partNumbers.stream().filter(pn -> pn.row() == 1).collect(Collectors.toList());
		List<PartNumber> pnLine3 = partNumbers.stream().filter(pn -> pn.row() == 2).collect(Collectors.toList());

		assertTrue(CollectionUtils.isEqualCollection(
				pnLine1.stream().map(n -> n.number()).collect(Collectors.toList()),
				line1));
		assertTrue(CollectionUtils.isEqualCollection(
				pnLine2.stream().map(n -> n.number()).collect(Collectors.toList()),
				line2));
		assertTrue(CollectionUtils.isEqualCollection(
				pnLine3.stream().map(n -> n.number()).collect(Collectors.toList()),
				line3));
	}
	
	
	@Test
	void testSymbols() {
		String[] input = {".....+.58."};
		EngineSchema schema = new EngineSchema(input);
		List<List<Symbol>> symbols = schema.getSymbols();
		assertTrue(symbols.size() == 1);
		List<Symbol> symbolsLine1 = symbols.get(0);
		assertTrue(symbolsLine1.size() == 1);
		assertTrue(symbolsLine1.get(0).sign().equals("+"));
		assertTrue(symbolsLine1.get(0).row() == 0);
		assertTrue(symbolsLine1.get(0).col() == 5);
	}
	
	@Test
	void testSchema() {
		List<String> inputStrings = Arrays.asList(schema.getInput());
		assertTrue(inputStrings.size() == 10);
		
		List<List<Symbol>> symbols = schema.getSymbols();
		assertTrue(symbols.get(1).get(0).sign().equals("*"));
		assertTrue(symbols.size() == 10);

		List<Integer> trueSizes = Arrays.asList(0, 1, 0, 1, 1, 1, 0, 0, 2, 0);
		
		for(int i=0; i<symbols.size(); i++) {
			int nbSymbols = symbols.get(i).size();
			assertTrue(nbSymbols == trueSizes.get(i));
		}
	}
	
	@Test
	void testGearRatios() {
		List<Long> gearRatios = schema.getGearRatios(true);
		long l1 = 467 * 35;
		long l2 = 755 * 598;
		List<Long> results = Arrays.asList(l1, l2);
		assertTrue(CollectionUtils.isEqualCollection(gearRatios, results));
		long sumGearRatios = gearRatios.stream().mapToLong(Long::longValue).sum();
		assertTrue(sumGearRatios == 467835);
	}

	@Test
	void testGearRatiosLargeNumbers() {
		String input = AdventOfCode.getInputString("src/test/resources/", "test-day3.txt");
		EngineSchema schema = new EngineSchema(input.split("\n"));
		List<Long> gearRatios = schema.getGearRatios(true);
		List<Long> results = Arrays.asList(1667L*3L);
		assertTrue(CollectionUtils.isEqualCollection(gearRatios, results));
	}
	
	@Test
	void testGearRatiosEndPos() {
		String input = AdventOfCode.getInputString("src/test/resources/", "day3-endPos.txt");
		EngineSchema schema = new EngineSchema(input.split("\n"));
		List<Long> gearRatios = schema.getGearRatios(true);
		List<Long> results = Arrays.asList(127L*2L);
		assertTrue(CollectionUtils.isEqualCollection(gearRatios, results));
	}
	
	@Test
	void testPabloTask1() {
		String input = AdventOfCode.getInputString("src/test/resources/", "day03-pablo.txt");
		EngineSchema schema = new EngineSchema(input.split("\n"));
		List<Long> partNumbers = schema.getPartNumbers()
				.stream().map(n -> n.number()).collect(Collectors.toList());
		long sum = partNumbers.stream().mapToLong(Long::longValue).sum();
		assertTrue(sum == 537832L);
	}

	@Test
	void testPabloTask2() {
		String input = AdventOfCode.getInputString("src/test/resources/", "day03-pablo.txt");
		EngineSchema schema = new EngineSchema(input.split("\n"));	
		List<Long> gearRatios = schema.getGearRatios(false);
		long sum = gearRatios.stream().mapToLong(Long::longValue).sum();
		assertTrue(sum == 81939900L);
	}

	
}
