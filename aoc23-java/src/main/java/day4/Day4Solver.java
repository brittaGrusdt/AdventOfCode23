package day4;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

import utils.Solver;

public class Day4Solver extends Solver{
	
	private List<List<Integer>> numbers;
	private List<Card> cards;
	private Map<Integer, Integer> copiedCards;
	
	public Map<Integer, Integer> getCopiedCards() {
		return copiedCards;
	}

	public void setCopiedCards(Map<Integer, Integer> copiedCards) {
		this.copiedCards = copiedCards;
	}

	public Day4Solver(String path, String filename) {
		super(path, filename);
		List<List<Integer>> numbers = new ArrayList<List<Integer>>();
		List<Card> cards = new ArrayList<Card>();
		for(String line : super.getInput()) {
			String[] arr = line.split(" \\| ");
			List<String> ownNumbers = Arrays.asList(arr[1].trim().split("\\s"))
					.stream().filter(n -> !n.isEmpty()).collect(Collectors.toList());
			numbers.add(ownNumbers.stream().map(n -> Integer.parseInt(n.trim())).collect(Collectors.toList()));
			cards.add(new Card(arr[0]));
		}
		this.numbers = numbers;
		this.cards = cards;
		this.copiedCards = new HashMap<Integer, Integer>();
	}
	
	public List<List<Integer>> getNumbers() {
		return numbers;
	}

	public List<Card> getCards() {
		return cards;
	}

	public String runTask1() {
		int totalValue = 0;
		for(int i=0; i<cards.size(); i++) {
			Card card = cards.get(i);
			totalValue += card.computeCardValue(numbers.get(i));
		}
		System.out.println("The Elf's pile of scratchcards is worth " + totalValue + " points.");
		return String.valueOf(totalValue);
	}
	
	public String runTask2() {
		for(int i=0; i<cards.size(); i++) {
			Card card = cards.get(i);
			int cardID = card.getId();
			int nbMatches = card.getNumberMatches(numbers.get(i));
			//check if there are copies of current card 
			IntStream stream = IntStream.range(cardID+1, cardID + nbMatches+1);
			int nbCopiesOfCard = copiedCards.getOrDefault(cardID, 0);
			
			stream.forEach(num -> {
				int nbExistingCopies = copiedCards.getOrDefault(num, 0);
				copiedCards.put(num, nbExistingCopies + 1 + nbCopiesOfCard);
			});
		}		
		
		int nbCopiedCards = copiedCards.values().stream().mapToInt(Integer::intValue).sum();
		int nbTotalCards = nbCopiedCards + cards.size();
		
		System.out.println("The Elf's pile of scratchcards contains " + nbTotalCards + " cards.");
		return String.valueOf(nbTotalCards);
	}

	
	public static void main(String[] args) {
		Day4Solver solver = new Day4Solver("src/main/resources/", "input-day4.txt");
//		for(String line : solver.getInput()) {
//			System.out.println(line);
//		}
		solver.runTask1();
		solver.runTask2();
	}



}
