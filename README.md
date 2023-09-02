# Motorman

![Title graphic](/assets/images/title.JPG)

The popular game of Hangman, has been redesigned and given the name MotorMan. It is a command line interface game and the player should guess a letter or a word within 6 tries, in order to win the game. The game  provides full user interaction to complete the game.

I trust you'll find the game enjoyable.

## Lucid Chart

![Flow Chart](/assets/images/Lucidchart.JPG)

Before commencing the game's initial development, I created a flowchart using Lucid Chart to map out my approach to writing the Python code for the game. At the start of the game, my intention was to inquire about the user's name and store it for later use. Additionally, I aimed to confirm the user's category choice and, in case of uncertainty, implement a loop to revisit the question.

In conclusion, my priority was to establish a clear visual representation of how the code would function in relation to letter guessing. Initially, I grappled with the question of whether the user had discovered the correct letter within a word, even though the word itself hadn't been established according to the flow chart. To address this, I revised the flow to indicate whether the given letter matched the correct word and, if not, whether it existed within the word before proceeding through the loop. 


## Design

![Start of game](/assets/images/Motorman.JPG)

The design element does not feature too much in this project, as it is a command line interface project. Whilst not requiring any ‘glamorous’ design, the function of the app works well enough. I have previously seen some other apps developed by students that hold a little more style, but for the purposes of the game, everything is fine.

### ASCII Art

![Gallows art](/assets/gallows-art.png)
![ASCII Art](/assets/ASCII%20Hangman.png)

I found myself particularly drawn to the concept of incorporating ASCII art, a graphical design technique that utilizes printable characters to craft images. Considering this game operates within a command-line environment, there was a risk of it appearing rather plain and uninteresting to users. In my perspective, there was room for greater utilization of ASCII art, potentially to convey the remaining number of lives.

## Testing

### Validation

I employed CI Python Linter for validation purposes and to ensure the integrity of the code by Code Institute. This tool facilitated comprehensive testing of the entire codebase, including an assessment against PEP8 standards, which govern the readability and consistency of Python code. While the test recommended an alternative method for exiting the program, it's worth noting that my current code functions without errors. Apart from minor readability concerns, which I'll address below, my code adheres to the PEP8 guidelines.
### Unsolved Errors

Testing involved using print statements to check whether a piece of code or function worked before really adding the true purpose of the code. 

I stumbled across a number of errors, when specifically trying to condense the code. One of my personal issues with the program is the amount of code, and whilst I endeavoured to replace many lines of code with just a few, sometimes errors would appear or the program would not work the way it was intended to.

![CI Python Linter](/assets/images/validator.JPG)

Due to the use of ASCII art, W605,W291,W292,W293 errors were registered according to PEP8 standards.

Also, E111 and E501 readability errors were registered according to PEP8 standards.

### Issues

I have come across a number of issues I found within the game. Some do affect the users experience and others have some visual implications.


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





## Thanks

I’d like to thank you for taking the time to read this README file, and I hope you have enjoyed playing the game. 
