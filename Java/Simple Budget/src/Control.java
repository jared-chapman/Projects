//This program has annoyingly excessive comments
//I'm sorry

import java.io.IOException;
import java.util.*;


public class Control {
	public boolean mExit = false;																					//When exit is true, the program will exit. 
	java.sql.Date dateObj = new java.sql.Date(Calendar.getInstance().getTime().getTime());							//Use dateObj.toString() to get date
	
	ArrayList<Trackers> trackerList = new ArrayList<Trackers>();{													//Makes an ArrayList of Tracker objects. Trackers can be added to this ArrayList later
		trackerList.add(new Trackers("fuhgeddaboudit", 0, ""));														//This tracker is a placeholder. Don't need it, but not sure how to not have an item in list[0]
	}
	
	public Control(){
	
	}
	
	public void mainLoop() {																	
		System.out.print("First, let's add a tracker\n");															//When the main loop first starts
		addTracker();																								//Add a tracker
		while(!mExit){																								//Do all of this until user exits program with 7
			Scanner sc = new Scanner(System.in);																	//Setup the Scanner. Allows input with sc.nextLine()
			System.out.println("\n\nWhat would you like to do?"														//Think of these lines as the main menu
					+ "\n1 - Input Spending"
					+ "\n2 - Show Totals"
					+ "\n3 - Show Details"
					+ "\n4 - Add a Tracker"
					+ "\n5 - Edit a Tracker"
					+ "\n6 - Remove a Tracker"
					+ "\n7 - Exit");
			int doThis = 0;																							//Declare the variable doThis so it's in the correct scope
			try{doThis = Integer.parseInt(sc.nextLine());}															//Try checking the user's input
			catch(NumberFormatException e){}																		//If they don't give a correct number, keep going. This will cause the switch statement in the next line to default without problems
			switch(doThis){																							//Do one of the following based on user's input
				case 1: addToTracker(); break;
				case 2: showTotals(); break;
				case 3: showDetails(); break;
				case 4: addTracker(); break;
				case 5: editTracker(); break;
				case 6: removeTracker(); break;
				case 7: exit(); break;
				default: 																							//If incorrect input, loop again
					System.out.println("Try again");
			}
		}
	}
	
	//Add an Entry to a Tracker's Entry ArrayList
	public void addToTracker(){								
		String date = dateObj.toString();																			//Get the date to add to the Entry
		Scanner sc = new Scanner(System.in);																		//Setup scanner
		System.out.println("How much did you spend?");																//Asks user how much they spent
		int amountToAdd = 0;																						//Declare int amountToAdd so it's in the correct scope
		while (amountToAdd == 0){																					//Basically, do this until amountToAdd changes
			try {  amountToAdd = Integer.parseInt(sc.nextLine());													//Check that input is an int
			} catch(NumberFormatException e){ 
				System.out.println("please enter a number");														//And if it isn't, try again
			}
		}
		Trackers chosenTracker = chooseTracker();																	//Call chooseTracker() and choose a tracker
		System.out.println("Note:  (Enter to skip)");																//Get input
		String noteToAdd = sc.nextLine();																			//Add input to noteToAdd
		chosenTracker.addToTotal(amountToAdd, date, noteToAdd);														//Call addToTotal on chosenTracker, which is what actually creates the entry
		chosenTracker.displayStats();																				//Display the stats
	}

	//Undo last Entry
	public void undo(){
		Trackers chosenTracker = chooseTracker();
		chosenTracker.undo();
		chosenTracker.displayStats();
	}
	
	//Show totals of all Trackers
	public void showTotals(){
		for(int i=1; i<trackerList.size(); i++){																	//For each Tracker
			String name = ((Trackers) trackerList.get(i)).getName();  												//Get the Tracker name
			int spent = ((Trackers) trackerList.get(i)).getSpent();													//Get the Tracker amount spent
			int budget = ((Trackers) trackerList.get(i)).getBudget();												//Get the tracker Budget
			if (budget >= spent){
				System.out.println(name + ": $" + spent + " Out of " + "$" + budget + " spent. $" + (budget-spent) + " remaining");
			} else {
				System.out.println(name + ": $" + spent + " Out of " + "$" + budget + " spent. You are $" + (-budget-spent) + " over budget!");
			}
		}
	}
	
	
	//Shows Details (Entry Objects)
	public void showDetails(){																	
		Trackers chosenTracker = chooseTracker();																	//Choose Tracker
		int detailLength = chosenTracker.entryList.size();															//Find the size of the chosen Tracker's Entry ArrayList
		System.out.println(chosenTracker.getName() + " Created on " + chosenTracker.entryList.get(0).getDate());	//Display when the Tracker was created
		for (int i=1; i<detailLength; i++){																			//For (the size of the chose Trackers Entry ArrayList
			int amount = chosenTracker.entryList.get(i).getAmount();												//Get the Entry amount for this loop number
			String date = chosenTracker.entryList.get(i).getDate();													//Get the Entry date for this loop number
			String note = chosenTracker.entryList.get(i).getNote();													//Get the Entry note for this loop number
			System.out.println("$" + amount + " spent on " + date + " " + note );									//Print them
		}
	}
	
	public void addTracker(){
		Scanner sc = new Scanner(System.in);
		String name = "";
		while (name.equals("")){
			System.out.println("What is the name of your new Tracker?");
			name = sc.nextLine();
			if(name.equals("")){
				System.out.println("Please enter a name");
			}
			
		}
		System.out.println("What is your budget?");
		int budget = 0;
		while (budget == 0){
			try {  budget = Integer.parseInt(sc.nextLine());
			} catch(NumberFormatException e){ 
				System.out.println("please enter a number");
			}
		}
		
		trackerList.add(new Trackers(name, budget, "White"));
	}
	
	public void editTracker(){												
		Scanner sc = new Scanner(System.in);
		System.out.println("Which Tracker would you like to edit?");
		Trackers trackerToEdit = chooseTracker();
		
		//checks for blank line, if not blank updates the name (then budget, then color)
		System.out.println("New Name: (Enter to skip)");
		String newName = sc.nextLine();
		if (!newName.equals("")){
			trackerToEdit.setName(newName);
		}
		//update budget
		System.out.println("New Budget: (Enter to skip)");					
		int newBudget = trackerToEdit.getBudget();							//set newBudget to current budget
		while (newBudget == trackerToEdit.getBudget()){						//as long as it's the same
			String budgetString = sc.nextLine();							//check the input
			if (!budgetString.equals("")){									//if isn't blank
				try { newBudget = Integer.parseInt(budgetString); }			//check to see if the input is a number
				catch(NumberFormatException e){ 							//if it's not (i.e. you get an exception
					System.out.println("please enter a number");			//prompt the user for a number
				}
			} else {														//if the input isn't blank and it is verified as a number
				trackerToEdit.setBudget(newBudget);							//set the tracker's budget to the input
				break;
			}
			trackerToEdit.setBudget(newBudget);								//if the input was blank, set budget to newbudget, which was set to budget earlier	
		}																	//i.e. budget stays the same
		//update color
		System.out.println("New color: (Enter to skip)");
		String newColor = sc.nextLine();
		if (newColor != ""){
			trackerToEdit.setColor(newColor);
		}
		
	}
	
	public void removeTracker(){
		Scanner sc = new Scanner(System.in);
		System.out.println("Which Tracker would you like to remove?");
		for (int i=1; i<trackerList.size(); i++){
			System.out.println(i + " - " + ((Trackers) trackerList.get(i)).getName());
		}
		int toDelete = Integer.parseInt(sc.nextLine());
		System.out.println(((Trackers) trackerList.get(toDelete)).getName() + " Removed");
		trackerList.remove(toDelete);
	}
	
	public void exit(){
		mExit = true;
	}
	
 	public Trackers chooseTracker(){												//OK, this is a fun one
		Scanner sc = new Scanner(System.in);
		int chosenTracker = 0;														//This will be the position in the trackerList ArrayList of the chosen Tracker 
		while (chosenTracker == 0){													//Until a valid Tracker is chosen
			System.out.println("Choose Tracker");									//Prompt User
			for(int i=1; i<trackerList.size(); i++){								//For each Tracker in trackerList
				String name = ((Trackers) trackerList.get(i)).getName();  			//This code casts trackerList.get(j)).getName() as a Trackers 
				System.out.println(i + " - " + name);								//Print the trackers name. 
			}
			String chosenTrackerString = "";										//Initialize chosenTrackerString, which will hold the user input
			while (chosenTrackerString.equals("")){									//As long as it isn't blank
				chosenTrackerString = sc.nextLine();								//Get the user's input
				if (!chosenTrackerString.equals("")){								//If the input isn't blank
					try{		
						chosenTracker = Integer.parseInt(chosenTrackerString);		//chosenTracker is set to user input, as long as it doesn't throw an error
						if (chosenTracker > trackerList.size()){					//If the user's input is a number higher than the size of trackerList, i.e. not a Tracker
							System.out.println("Please enter a valid number");		//Tell user input is invalid
							chosenTracker = 0;										//Reset chosenTracker to 0. That way the loop will repeat
						}
					} catch(NumberFormatException e){								//If the input isn't an integer
						System.out.println("Please enter a number");				//Tell user input is invalid
					}
				} else {															//If the input isn't blank
					System.out.println("Try again");								//Tell user input is invalid. Loop repeats
				}
			}
		}		
		return (Trackers) trackerList.get(chosenTracker);							//If input is a valid number, return the proper Tracker object
	}
 	

}
