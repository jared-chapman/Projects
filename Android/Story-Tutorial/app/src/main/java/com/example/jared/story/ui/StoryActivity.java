package com.example.jared.story.ui;

import android.content.Intent;
import android.content.res.Resources;
import android.graphics.drawable.Drawable;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.example.jared.story.R;
import com.example.jared.story.model.Page;
import com.example.jared.story.model.Story;

import java.util.Stack;

import static android.R.attr.name;

public class StoryActivity extends AppCompatActivity {

private String name;
private Story story;
private ImageView storyImageView;                                                                   // declares variables
private TextView storyTextView;                                                                     // puts them in proper scope
private Button choice1Button;
private Button choice2Button;
private Stack<Integer> pageStack = new Stack<Integer>();                                            // Will keep track of pages so we can press back through them

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_story);

        storyImageView = (ImageView) findViewById(R.id.storyImageView);                             // defines variables
        storyTextView  = (TextView) findViewById(R.id.storyTextView);
        choice1Button  = (Button) findViewById(R.id.choice1Button);
        choice2Button  = (Button) findViewById(R.id.choice2Button);

        Intent intent = getIntent();                                                                // creates an Intent intent that holds the extras assigned in MainActivity

        name = intent.getStringExtra(getString(R.string.key_name));                                                       // Uses a reference as a key for the sake of consistency
        if (name == null || name.isEmpty()) {                                                       // In case reference doesn't match or user inputs an empty string
            name = "Friend";
        }

        story = new Story();                                                                        // Creates a story object
        loadPage(0);                                                                                // Loads page 0 when created
        //Toast.makeText(this, name, Toast.LENGTH_LONG).show();

    }

    private void loadPage(int pageNumber) {
        pageStack.push(pageNumber);
        final Page page = story.getPage(pageNumber);                                                      // Creates a new page object

        Drawable image = ContextCompat.getDrawable(this, page.getImageId());                        // Sets the variable image to the current page's id
        storyImageView.setImageDrawable(image);                                                     // Sets image

        String pageText = getString(page.getTextId());

        pageText = String.format(pageText, name);                                                   // Add name if placeholder is included, Won't add if not
        storyTextView.setText(pageText);                                                            // Sets text

        if (page.isFinalPage()) {
            choice1Button.setVisibility(View.INVISIBLE);
            choice2Button.setText(R.string.play_again_button_text);
            choice2Button.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    //finish();
                    loadPage(0);
                }
            });
        }else{
            loadButtons(page);
        }
    }

    private void loadButtons(final Page page) {
        choice1Button.setVisibility(View.VISIBLE);                                                  // Since visibility is set to INVISIBLE on final page,
        choice2Button.setVisibility(View.VISIBLE);                                                  // This makes sure buttons are always visible unless page is final
        choice1Button.setText(page.getChoice1().getTextId());                                       // Sets choice1Button text
        choice1Button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                int nextPage = page.getChoice1().getNextPage();
                loadPage(nextPage);
            }
        });


        choice2Button.setText(page.getChoice2().getTextId());                                       // Sets choice1Button text
        choice2Button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                int nextPage = page.getChoice2().getNextPage();
                loadPage(nextPage);
            }
        });
    }

    @Override
    public void onBackPressed() {                                                                   // Overrides default onBackPressed method
        pageStack.pop();                                                                            // Remove the most recent item in PageStack
        if (pageStack.isEmpty()){                                                                   // If the stack is empty (If only on the first page)
            super.onBackPressed();                                                                  // Execute the normal onBackPressed method, which goes to previous activity
        } else {
            loadPage(pageStack.pop());                                                              // Load the page and pop the page number (since it is pushed when loaded. This prevents a pageNumber from being added to the stack twice in a row
        }


    }
}
