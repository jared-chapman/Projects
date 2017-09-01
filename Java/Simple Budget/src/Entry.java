import java.util.Calendar;

public class Entry {
	private int mSpentOnEntry;
	private String mDate = "";
	private String mNote = "";
	java.sql.Date dateObj = new java.sql.Date(Calendar.getInstance().getTime().getTime());
	
	//Constructor with all details
	public Entry(int spent, String date, String note){																
		mSpentOnEntry = spent;
		mDate = date;
		mNote = note;
	}
	
	//Constructor without note
	public Entry(int spent, String date){																			
		mSpentOnEntry = spent;
		mDate = date;
	}
	
	//Constructor with just date. Not currently used
	public Entry(String date){																						
		mDate = date;
	}
	
	//Displays Entry Details. Not used
	/*public void displayEntryDetails(){																				
		String note = "";
		if (mNote.length()>0){
			note = (" " + mNote);
		}
		if (mSpentOnEntry>0){
			System.out.println("$" + mSpentOnEntry + " spent on " + mDate + note);
		} else {
			System.out.println("Tracker created on" + mDate);
		}
	}*/
	public int getAmount(){
		return mSpentOnEntry;
	}
	
	public String getDate(){
		return mDate;
	}
	
	public String getNote(){
		return mNote;
	}
}
