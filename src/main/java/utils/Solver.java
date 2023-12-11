package utils;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public abstract class Solver{

	protected List<String> input;
	
	public List<String> getInput() {
		return input;
	}

	public void setInput(List<String> input) {
		this.input = input;
	}

	protected Solver(String path, String filename) {
		this.input = getInputStrings(path, filename);
	}
	
	protected List<String> getInputStrings(String path, String filename) {
		Scanner scanner = getScanner(path, filename);
		List<String> inputStrings = new ArrayList<String>();
		while(scanner.hasNext()) {
			String line = scanner.next();
			inputStrings.add(line);
		}
		return inputStrings;
	}
	
	
	protected Scanner getScanner(String path, String filename) {
		String file = path + filename;
		Scanner scanner = null;
		try {
			scanner = new Scanner(new File(file));
			scanner.useDelimiter("\n");
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		return(scanner);		
	}
	
	protected Scanner getScanner(String filename) {
		return(getScanner("src/main/resources/", filename));
	}
	
	public abstract String runTask1();
	public abstract String runTask2();
	
}
