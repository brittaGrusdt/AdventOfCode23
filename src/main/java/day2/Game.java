package day2;

import java.util.Map;
import java.util.Set;

public class Game {

	private int id;
	private Set<CubeSet> cubeSubsets;
	
	public int getId() {
		return id;
	}

	public Set<CubeSet> getCubeSubsets() {
		return cubeSubsets;
	}

	public Game(int id, Set<CubeSet> revealedCubes) {
		this.id = id;
		this.cubeSubsets = revealedCubes;
	}
	
	/** 
	 * TODO: well probably could be done better, without printing out each case
	 * @param constraints
	 * @return id if possible, 0 otherwise
	 */
	public boolean checkIfPossibleGame(CubeSet constraints) {
		boolean isPossible = true;
		for(CubeSet set : this.getCubeSubsets()) {
			if(constraints.blue() < set.blue()) {
				isPossible = false;
				break;
			}
			if(constraints.red() < set.red()) {
				isPossible = false;
				break;
			}
			if(constraints.green() < set.green()) {
				isPossible = false;
				break;
			}
		}
		return isPossible;
	}
	
	public int getPower() {
		CubeSet minimalSet = getMinimalPossibleConfig();
		return minimalSet.blue() * minimalSet.green() * minimalSet.red();
	}
	
	
	public CubeSet getMinimalPossibleConfig() {
		int maxBlue = 0;
		int maxRed = 0;
		int maxGreen = 0;
		for(CubeSet set : this.getCubeSubsets()) {
			if(set.blue() > maxBlue) maxBlue = set.blue();
			if(set.red() > maxRed) maxRed = set.red();
			if(set.green() > maxGreen) maxGreen = set.green();
		}
		return new CubeSet(maxBlue, maxRed, maxGreen);
	}
}
