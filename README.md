# Motorman

![Title graphic](/assets/images/title.JPG)

The popular game of hangman, presented on a command line application format. The game is suitable to all persons, providing full user interaction to complete the game.

This game was created using the popular and powerful programming language called Python. It has been developed as project 3 of a 5 part series of repositories for Code Institute. Code institute offer a Diploma in Full Stack software development, that require the five projects to be submitted in order to succesfully pass the course.

I hope that you enjoy the game.

## Lucid Chart

![Flow Chart](/assets/flowchart.png)

Prior to initial implementation of the game, I constructed a flow chart using [Lucid Chart](https://www.lucidchart.com/pages/) to help me understand how I would be able to write the python code for the game. At the beginning of the game, I wanted to ask the user their name, and use it later on. Also I wanted to ask the user whether they were sure about their category decision. If not, I wanted to loop back to the question.

Finally, I needed to ensure that I could visually see how the code would work with regards to the guessing of letters. I was confused to begin with as I was asking myself whether the user found the correct letter in a word, which did not exist yet according to the flow chart. I rectified this to show that if the letter given was the correct word, and if not whether it was in the word before moving through the loop. 

I found the use of a flow chart incredibly useful when developing the application. It’s incredibly handy to have a visual representation of what I want my code to do, before writing it out. Although it is an early draft, I think adding to the chart as I was writing my code would have benefitted me further, as it was sometimes difficult to keep up with what I was coding.

## Design

![User interface](/assets/user-interface.png)
![Start of game](/assets/begin-game.png)

The design element does not feature too much in this project, as it is a command line interface project. Whilst not requiring any ‘glamorous’ design, the function of the app works well enough. I have previously seen some other apps developed by students that hold a little more style, but for the purposes of the game, everything is fine.

### ASCII Art

![Gallows art](/assets/gallows-art.png)
![ASCII Art](/assets/ASCII%20Hangman.png)

Looking at previous projects from other students, I really liked the idea of using ASCII (A graphical design technique using printable characters to create images) art. As a command line program, this game could easily have looked bland and boring to a user. I feel there could have been more use of the ASCII art, perhaps to display how many lives were remaining, as I don not feel this is highlighted quite as well as it should be.

## Testing

### Validation

![Snyk validator](/assets/snyk-validate.png)

For validation, I used Snyk. This allowed me to test the entire code and test it up to the PEP8 standards. PEP8 (Python Enhancement Proposal) dives into the readability and consistency of the Python code written. This test suggested I use a different method to exit the program, however there are no errors in what my current code does. Aside from my own personal readability issues (more below) my code conforms to PEP8.

### Game testing

Testing involved using print statements to check whether a piece of code or function worked before really adding the true purpose of the code. 

I stumbled across a number of errors, when specifically trying to condense the code. One of my personal issues with the program is the amount of code, and whilst I endeavoured to replace many lines of code with just a few, sometimes errors would appear or the program would not work the way it was intended to.

![Select Category](/assets/category-select.png)

Above is a test I did of the category select function. Here shows that if the user inputs an invalid character, then an error message will appear. This prompts the user to alter their input.

![Random word](/assets/random-word-test.png)

Here is an earlier version of the repository testing the random word function. Here I commented out the welcome player function to allow me to run the random word tests.

![Letter select](/assets/letter-select-test.png)

I tested whether the letter selected by the user would show up in the blank dashes. I printed the word so I would know which letters to input.

### Issues

I have come across a number of issues I found within the game. Some do affect the users experience and others have some visual implications.

![Correct gueses](/assets/correct-guess-bug.png)

I managed to find that when a user guesses correctly initially, rather than just printing the correct guess and staying with the hangman art, you are able to solve the word with correct guesses without actually seeing the gallows. This to me would be frustrating for the user and I feel this tarnishes the game a little.

![Spaced words](/assets/spaced-words.png)

Here an issue arose when the hidden word is actually two words. When typing the letters of South Africa, the user should win. However you are required to put a space in to win the game. Looking back, I would like to create a hint within the code that picks up on this, or even omit spaces altogether.

![Top of screen bug](/assets/top-screen-bug2.png)

After surviving the game, the word is printed out as well as two dashes that sit above it. This is not intentional, and I could't quite figure out exactly what caused this.

## Deployment

The following deployment stages were taken. Through Gitpod, I would have to stage regular commits.

* `git add .` - Adds saved files to Git's staging area
* `git commit -m ""` - Commits the saved files to the local repository
* `git push` - Pushes the commits

As this was a command line program, I had to deploy via Heroku. Heroku is a cloud based application platform. I had to use this software to be able to build a terminal in the form of a website, so that the game could be tested and assessed. The following deployment stages are.

* On the settings section of the application dashboard, select config vars.
* Set the Key to PORT and the value to 8000
* Add buildpacks, python and node.js
* From the Deploy tab, deploy manually at the bottom of the page.

![Setting tab](/assets/settings-tab.png)
![Config Vars](/assets/config-vars-settings.png)
![Buildpacks](/assets/settings-buildpack.png)
![Deploy](/assets/heroku-deploy.png)

The above steps, created a usable application.

## Future Development

I feel there is a lot more scope and potential for this game. Firstly an issue for me is that the user is not allowed to select a new category after each retry. Whilst I added some code that rectified this, it did create issues elsewhere. Also the code for me seems very clunky and would definitely benefit from being condensed so that the readability improves significantly.

Moving forward, I would like to see more ASCII art within the game. Post development, I stumbled across a module that would have enabled me to create these art pieces, as supposed to finding them from other repositories (mentioned below). Also, maybe some music in the background in true 8-bit style would have really leant to the nostalgia feel of the game.

## Credits and Mentions

The foundation of the game was build upon the work of [wynand1004](https://github.com/wynand1004). I built upon his already great game and tried to make it my own.

Both him and [rrice2004](https://github.com/rrice2004) project’s assisted me with the gallows and hangman artwork. I really liked the simple graphics to depict each gallow for a wrong letter choice. I also liked the idea of having seperate files for each of the random words, as supposed to inputting it in the already clunky run.py file.

## Thanks

I’d like to thank you for taking the time to read this README file, and I hope you have enjoyed playing the game. 
