package day2;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import utils.AdventOfCode;

public class Day2Solver {
	
	public static final CubeSet constraintsTask1 = new CubeSet(14, 12, 13);

	
	public static Game setupGame(String line) {
		String[] components = line.split(":");
		String gameId = components[0].substring("Game ".length());
		String[] subsets = components[1].split(";");
		Set<CubeSet> cubes = new HashSet<CubeSet>();
		
		for(String s : subsets) {
			Map<Color, Integer> occurrences = new HashMap<Color, Integer>();
			for(Color col : Color.values()) {
				Pattern pattern = Pattern.compile("\\d+ " + col.toString().toLowerCase());
				Matcher matcher = pattern.matcher(s);
				String content = "";
				int nb = 0;
				if(matcher.find()) content = matcher.group();
				if(!content.isEmpty()) nb = Integer.parseInt(content.split(" ")[0].trim());
				occurrences.put(col, nb);
			}
			cubes.add(new CubeSet(occurrences.get(Color.BLUE),
								  occurrences.get(Color.RED),
								  occurrences.get(Color.GREEN)));
		}
		Game game = new Game(Integer.parseInt(gameId), cubes);
		return game;
	}
	
	public static void runTask1() {
		Scanner scanner = AdventOfCode.getScanner("input-day2.txt");
		int sum = 0;
		while(scanner.hasNext()) {
			String line = scanner.next();
			Game game = setupGame(line);
			boolean isPossible = game.checkIfPossibleGame(constraintsTask1);
			if(isPossible) sum += game.getId();
		}
		System.out.println("Sum of IDs of possible games is: " + sum);
	}
	
	public static void runTask2() {
		Scanner scanner = AdventOfCode.getScanner("input-day2.txt");
		int sum = 0;
		while(scanner.hasNext()) {
			String line = scanner.next();
			Game game = setupGame(line);
			int power = game.getPower();
			sum += power;
		}
		System.out.println("Sum of powers: " + sum);
	}

	
	public static void main(String[] args) {
		runTask1();
		runTask2();
	}

}
