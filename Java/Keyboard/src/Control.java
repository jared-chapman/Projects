
public class Control {
	private String mSolve = "";
	private String mAnswer = "";
	private String mInputBox = "";
	
	Keyboard k = new Keyboard();
	
	
	
	public Control(String solve) {
		mSolve = solve;
	}
	public Control() {	
	}
	
	
	
	
	public void input(String input) {								//accepts a string to control keyboard input
		for(int i=0; i<input.length(); i++) {
			switch (input.charAt(i)) {
				case('u'): k.up(); break;
				case('d'): k.down(); break;
				case('l'): k.left(); break;
				case('r'): k.right(); break;
				case('<'): k.cursorLeft(); break;
				case('>'): k.cursorRight(); break;
				case('s'): k.select(); break;
				case('b'): k.backspace(); break;
			}		
		}
	}
	public void print() {											//prints keyboard.mOutput
		System.out.println(k.getOutput());
	}
	public int[] findCharacterPosition(char getPos) {				//returns the current position on the keyboard
		int[] position = new int[] {0,0}; 
		for(int i=0; i<4; i++) {
			for(int j=0; j<10; j++) {
				if (getPos == k.getBoard()[i][j]) {
					position[0] = i;
					position[1] = j;
				}
			}
		}
		return position;
	}
	public int[] getDistance(char one, char two) {					//accepts two characters and returns the distance between them
		int[] positionOne = findCharacterPosition(one);
		int[] positionTwo = findCharacterPosition(two);
		int xDistance = positionTwo[0]-positionOne[0];
		int yDistance = positionTwo[1]-positionOne[1];
		int[] distance = new int[] {xDistance,yDistance};
		return distance;
	}


	
	
	
	
	
	
	
	
	
	
}
