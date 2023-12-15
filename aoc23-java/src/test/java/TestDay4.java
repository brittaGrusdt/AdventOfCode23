

import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.Arrays;
import java.util.List;

import org.apache.commons.collections4.CollectionUtils;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import day4.Day4Solver;

public class TestDay4 {

	private static Day4Solver solver;
	
	@BeforeAll
	static void setup() {
		solver = new Day4Solver("src/test/resources/", "test-input-day4.txt");
	}
	
	@Test
	void testSummedValue() {
		int value = Integer.parseInt(solver.runTask1());
		assertTrue(value == 13);
	}
	
	@Test
	void testWinningNumbers() {
		
		List<Integer> winningNumbers1 = Arrays.asList(41, 48, 83, 86, 17);
		List<Integer> winningNumbers2 = Arrays.asList(13, 32, 20, 16, 61);
		List<Integer> winningNumbers3 = Arrays.asList(1, 21, 53, 59, 44);
		List<Integer> winningNumbers4 = Arrays.asList(41, 92, 73, 84, 69);
		List<Integer> winningNumbers5 = Arrays.asList(87, 83, 26, 28, 32);
		List<Integer> winningNumbers6 = Arrays.asList(31, 18, 13, 56, 72);
		List<List<Integer>> winningNumbers = Arrays.asList(winningNumbers1,
				winningNumbers2, winningNumbers3, winningNumbers4, 
				winningNumbers5, winningNumbers6);
		
		for(int i=0; i<6; i++) {
			assertTrue(CollectionUtils.isEqualCollection(solver.getCards().get(i).getWinningNumbers(), 
					winningNumbers.get(i)));
		}
	}
	
	@Test
	void testTask2() {
		int nbCards = Integer.parseInt(solver.runTask2());
		assertTrue(nbCards == 30);
	}
}
