package com.example.jared.story.ui;

import android.content.Intent;
import android.content.res.Resources;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import com.example.jared.story.R;
import com.example.jared.story.ui.StoryActivity;

public class MainActivity extends AppCompatActivity {

        // creates variables for name field and button
        private EditText nameField;
        private Button startButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // when activity is created, set nameField and startButton
        // to appropriate Views
        nameField = (EditText) findViewById(R.id.nameEditText);
        startButton = (Button) findViewById(R.id.startButton);

        // sets the oncClickListener for the button. code here will execute
        // when button is tapped
        startButton.setOnClickListener(new View.OnClickListener() {
            @Override                                                                               //overriding parent class
            public void onClick(View v) {
                String name = nameField.getText().toString();                                       //Converts editable text data type to String and stores it in the variable string
                //Toast.makeText(MainActivity.this, name, Toast.LENGTH_LONG).show();                //Creates toast message. Can't use "this" since we're in an anonymous class, so must use parent class's full name
                startStory(name);                                                                   //Runs startStory method and passes name

            }
        });
    }

    @Override
    protected void onResume() {                                                                     // This code always runs after onCreate
        super.onResume();                                                                           // Whether new activity or when using back button
        nameField.setText("");
    }

    private void startStory(String name) {
        Intent intent = new Intent(this, StoryActivity.class);                                      //Creates an intent. first parameter is current context, second is which activity you want to start
        Resources resources = getResources();                                                       //This allows access to the Resources class, which contains strings.xml
        String key = resources.getString(R.string.key_name);
        intent.putExtra(key, name);                                                                 //taking key parameter, which was passed from the onClickListener method above
        startActivity(intent);                                                                      //Starts new activity and takes intent as a parameter
    }


}
