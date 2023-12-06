package aoc23.day2;

import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.Set;

import org.apache.commons.collections4.CollectionUtils;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import aoc.utils.AdventOfCode;
import day2.CubeSet;
import day2.Day2Solver;
import day2.Game;

class TestGame {

	private static final List<Game> games = new ArrayList<Game>();
	
	@BeforeAll
	static void initGames() {
		Scanner scanner = AdventOfCode.getScanner("src/test/resources/", "test-input-day2.txt");
		while(scanner.hasNext()) {
			String line = scanner.next();
			games.add(Day2Solver.setupGame(line));
		}
	}
	
	@Test
	void testGameID() {
		for(int i=0; i<games.size(); i++) {
			int id = games.get(i).getId();
			assertTrue(id == i+1);
		}
	}

	@Test
	void testCubeSets() {
		CubeSet game1Set1 = new CubeSet(3, 4, 0);
		CubeSet game1Set2 = new CubeSet(6, 1, 2);
		CubeSet game1Set3 = new CubeSet(0, 0, 2);
		Set<CubeSet> subsetsGame1 = games.get(0).getCubeSubsets();
		assertTrue(subsetsGame1.contains(game1Set1));
		assertTrue(subsetsGame1.contains(game1Set2));
		assertTrue(subsetsGame1.contains(game1Set3));
		
		List<Integer> nbSubsets = Arrays.asList(3, 3, 3, 3, 2);
		for(int i=0; i<games.size(); i++) {
			assertTrue(games.get(i).getCubeSubsets().size() == nbSubsets.get(i));
		}
	}
	
	@Test
	void testPossibleGames(){
		List<Boolean> possibleGames = Arrays.asList(true, true, false, false, true);
		int sum = 0;
		for(int i=0; i<games.size(); i++) {
			Game game = games.get(i);
			boolean isPossible = game.checkIfPossibleGame(Day2Solver.constraintsTask1);
//			System.out.println("Game " + (i+1) + " is possible: " + isPossible);
			assertTrue(isPossible == possibleGames.get(i));
			if(isPossible) sum+= game.getId();
		}
		assertTrue(sum == 8);
	}

	@Test
	void testPower() {
		List<Integer> results = Arrays.asList(48, 12, 1560, 630, 36);
		List<Integer> powers = new ArrayList<Integer>();
		for(Game game : games) {
			powers.add(game.getPower());
		}
		assertTrue(CollectionUtils.isEqualCollection(powers, results));
	}
	
}
