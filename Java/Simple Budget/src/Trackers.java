import java.util.*;

public class Trackers {																			
	private String mName = "";
	private int mSpent;
	private int mPrevAmount;
	private int mBudget;
	private String mColor = "";
	
	java.sql.Date dateObj = new java.sql.Date(Calendar.getInstance().getTime().getTime());
	
	ArrayList<Entry> entryList = new ArrayList<Entry>();{										//creates a list of Entry objects within this tracker object
		entryList.add(new Entry(dateObj.toString()));
	}
	
	
	public Trackers(String name, int budget, String color){
		mName = name;
		mBudget = budget;
		mColor = color;
	}
	
	public void addToTotal(int amountToAdd, String date, String note){
		mPrevAmount = mSpent;
		entryList.add(new Entry(amountToAdd, date, note));
	}
	
	public void undo(){
		mSpent = mPrevAmount;
	}
	
	public String getName(){
		return mName;
	}
	
	public void setName(String newName){
		mName = newName;
	}
	
	public int getSpent(){
		int spent = 0;
		for(int i=0; i<entryList.size(); i++){
			spent += entryList.get(i).getAmount();
		}
		return spent;
	}
	
	public void setSpent(int newSpent){
		mSpent = newSpent;
	}
	
	public int getBudget(){
		return mBudget;
	}
	
	public void setBudget(int newBudget){
		mBudget = newBudget;
	}
	
	public String getColor(){
		return mColor;
	}
	
	public void setColor(String newColor){
		mColor = newColor;
	}
	
	public void displayStats(){
		int totalSpent = 0;
		for (int i=0; i<entryList.size(); i++){
			totalSpent += entryList.get(i).getAmount();
		}
		int amountLeft = mBudget-totalSpent;
		if (amountLeft>0){
			System.out.println("You have spent $" + totalSpent + " on " + mName+ ". You have $" + amountLeft + " left");
		}else{
			System.out.println("You have spent $" + totalSpent + " on " + mName+ ". You are $" + -amountLeft + " over budget");
		}
	}
	
}
