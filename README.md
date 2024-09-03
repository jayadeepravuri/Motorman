# Motorman

![Title graphic](/assets/images/title.JPG)
[Here is the live version of my project](https://motorman-002301103e6a.herokuapp.com/)

The popular game of Hangman, has been redesigned and given the name MotorMan. It is a command line interface game and the player should guess a letter or a word within 6 tries, in order to win the game. The game  provides full user interaction to complete the game.

I trust you'll find the game enjoyable.

## Lucid Chart

![Flow Chart](/assets/images/lucid chart 1.png)
![Flow Chart](/assets/images/Lucid chart 2.png)
Before commencing the game's initial development, I created a flowchart using Lucid Chart to map out my approach to writing the Python code for the game. At the start of the game, my intention was to inquire about the user's name and store it for later use. Additionally, I aimed to confirm the user's category choice and, in case of uncertainty, implement a loop to revisit the question.

In conclusion, my priority was to establish a clear visual representation of how the code would function in relation to letter guessing. Initially, I grappled with the question of whether the user had discovered the correct letter within a word, even though the word itself hadn't been established according to the flow chart. To address this, I revised the flow to indicate whether the given letter matched the correct word and, if not, whether it existed within the word before proceeding through the loop. 


## Design

![Start of game](/assets/images/Motorman.JPG)

The design element does not feature too much in this project, as it is a command line interface project. Whilst not requiring any ‘glamorous’ design, the function of the app works well enough. I have previously seen some other apps developed by students that hold a little more style, but for the purposes of the game, everything is fine.

### Features

* Firstly , there is a username validator
* Now, the player gets to begin the game, by guessing either a word or a letter.
* If the player correctly selects a single letter or a word, he wins or a loses a life.
* If the player incorrectly selects a word or a letter, he loses a life utill all the 6 
  lifes are used.
* If the player enters multiple letter or any other character than an alphabet, he can try 
  again.
* If the player enters an already guessed letter, he gets to try again, without losing a 
  life.

### ASCII Art

![ASCII Art](/assets/images/ASCII.JPG)

I was particularly captivated by the idea of integrating ASCII art, a creative graphical technique that employs printable characters to construct visual representations. Given that this game operates within a command-line environment, there was a concern that it might come across as simplistic and unengaging to users. From my viewpoint, there was an opportunity to leverage ASCII art more extensively, potentially to communicate the remaining number of lives.

## Testing

### Validation

I employed CI Python Linter for validation purposes and to ensure the integrity of the code by Code Institute. This tool facilitated comprehensive testing of the entire codebase, including an assessment against PEP8 standards, which govern the readability and consistency of Python code. While the test recommended an alternative method for exiting the program, it's worth noting that my current code functions without errors. Apart from minor readability concerns, which I'll address below, my code adheres to the PEP8 guidelines.
### Unsolved Errors

Testing involved using print statements to check whether a piece of code or function worked before really adding the true purpose of the code. 

![CI Python Linter](/assets/images/validator.JPG)

Due to the use of ASCII art, W605,W291,W292,W293 errors were registered according to PEP8 standards.

Also, E111 and E501 readability errors were registered according to PEP8 standards.

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

The above steps, created a usable application.

## Future Development

* Firstly, the game could have different levels of difficulty, according to category of 
  words.
* The guessed letter could be displayed.
* Multiple letters can be taken instead of a single letter.
* Score system could be added.
* Also the code for me seems very clunky and would definitely benefit from being condensed 
  so that the readability improves significantly.

## Credits and Mentions

* Code institute for the template.
* Youtube for great tutorials and inspiration.
* My family for the suppport.
