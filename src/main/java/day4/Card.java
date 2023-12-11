package day4;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Card {
	
	private List<Integer> winningNumbers;
	private int id;
	
	public int getId() {
		return id;
	}

	public List<Integer> getWinningNumbers(){
		return winningNumbers;
	}
	
	public Card(String input) {
		String[] arr = input.split(":");
		String id = arr[0].substring("Card ".length());
		this.id = Integer.parseInt(id.trim());
		
		List<String> numberStrings = Arrays.asList(arr[1].trim().split("\\s"))
				.stream().filter(n -> !n.isEmpty()).collect(Collectors.toList());
		this.winningNumbers = numberStrings.stream().map(n -> Integer.parseInt(n.trim()))
				.collect(Collectors.toList());
	}
	
	public Card(int id, List<Integer> numbers) {
		this.winningNumbers = numbers;
		this.id = id;
	}
	
	
	public double computeCardValue(List<Integer> numbers) {
		int nbMatches = numbers.stream().filter(n -> winningNumbers.contains(n)).
			collect(Collectors.toList()).size();
		return  nbMatches == 0 ? 0 : Math.pow(2, nbMatches-1); 
	}
}
