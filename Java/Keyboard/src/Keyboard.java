public class Keyboard {

	/*
	 Layout
	  		1 2 3 4 5 6 7 8 9 0
	  		q w e r t y u i o p
	  		a s d f g h j k l '
	  		z x c v b n m , . ?
	 */
	
	//Variables
	private char[][] board = new char[][] {						//array of arrays. 
		{'1','2','3','4','5','6','7','8','9','0'},
		{'q','w','e','r','t','y','u','i','o','p'},
		{'a','s','d','f','g','h','j','k','l','\''},
		{'z','x','c','v','b','n','m',',','.','?'}
		};
		
	private int[] mRange = {9,3};								//length, height of keyboard
	private int[] mKeyboardPos = {0,0};							//represents the highlighted character
	private String mOutput = "";								
	private int mCursorPos = 0;									//where the cursor is located in the text field
	
	

	
	public Keyboard() {
	}
	

	
	
	//Controlling the keyboard
	public void up() {
		if (mKeyboardPos[0] > 0) {
			mKeyboardPos[0]--;
		} else {
			mKeyboardPos[0] = 3;
		}
	}
	public void down() {
		if (mKeyboardPos[0] < mRange[1]) {
			mKeyboardPos[0]++;
		} else {
			mKeyboardPos[0] = 0;
		}
	}
	public void left() {
		if (mKeyboardPos[1] > 0) {
			mKeyboardPos[1]--;
		} else {
			mKeyboardPos[1] = 9;
		}
	}
	public void right() {
		if (mKeyboardPos[1] < mRange[0]) {
			mKeyboardPos[1]++;
		} else {
			mKeyboardPos[1] = 0;
		}
	}
	public void cursorLeft() {
		if (mCursorPos > 0) {
			mCursorPos--;
		}
	}
	public void cursorRight() {
		if (mCursorPos < mOutput.length()){
			mCursorPos++;
		}
	}
	public void select() {
		//adds the selected character to mOutput by storing mOutput in tempOutput, writing everything in tempOutput before 
		//cursorPosition to mOutput, writing the selected character to mCursorPosition, writing the rest of tempOutput
		//to mOutput, then incrementing mCursorPosition to put it after the newly inputed character
		String tempOutput = mOutput;
		mOutput = (tempOutput.substring(0, mCursorPos) + board[mKeyboardPos[0]][mKeyboardPos[1]] + tempOutput.substring(mCursorPos, tempOutput.length()));
		mCursorPos++;
	}
	public void backspace() {
		//very similar to select
		if (mOutput.length()>0){
			String temp = mOutput;
			mOutput = (temp.substring(0, mCursorPos-1) + temp.substring(mCursorPos, temp.length()));
			mCursorPos--;
		}
	}

	
	public String getOutput(){
		return mOutput;
	}
	public char getKeyboardPosition() {
		char toPrint = board[mKeyboardPos[0]][mKeyboardPos[1]];
		return toPrint;
	}
	public int getCursorPosition() {
		return mCursorPos;
	}
	public char[][] getBoard(){
		return board;
	}
	
	public int[] findCharacterPosition(char getPos) {
		int[] position = new int[] {0,0}; 
		for(int i=0; i<4; i++) {
			for(int j=0; j<10; j++) {
				if (getPos == board[i][j]) {
					position[0] = i;
					position[1] = j;
				}
			}
		}
		return position;
	}
}















