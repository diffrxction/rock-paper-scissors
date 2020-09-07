
# Description

How about some brand new rules? The original game has a fairly small choice of options.

Extended versions of the game are decreasing the probability of draw, so it could be cool to play them.
Now, your program should be able to accept alternative lists of options, like Rock, Paper, Scissors, Lizard, Spock, or even a list like this:


![More Options Example](https://user-images.githubusercontent.com/65293175/92338776-3453ea80-f0d0-11ea-9990-5bb8a007f6c3.jpg)

At this stage, before the start of the game, the user will be able to choose the options that will be used. After entering his/her name, the user should provide a list of options separated by a comma. For example,
```
rock,paper,scissors,lizard,spock
```
If the user inputs an empty line, your program should start the game with default options: rock. paper and scissors.

After the game options are defined, your program should output `Okay, let's start`

Whatever list of options the user chooses, your program, obviously, should be able to identify which option beats which, that is, the relationships between different options. First, every option is equal to itself (causing a draw if both the user and the computer choose the same option). Secondly, every option wins over one half of the other options of the list and gets defeated by another half. How to determine which options are stronger or weaker than the option you're currently looking at? Well, you can try to do it this way: take the list of options (provided by the user or the default one). Find the option for which you want to know its relationships with other options. Take all the options that follow this chosen option in the list. Add to them the list of options that precede the chosen option. Now you have another list of options that doesn't include the "chosen" option and has the different order of elements in it (first go the options following the chosen one in the original list, after them are the ones that precede it). So, in this "new" list, the first half of the options will be defeating the "chosen" option, and the second half will get beaten by it.

For example, the user's list of options is `rock,paper,scissors,lizard,spock`. You want to know what options are weaker than lizard. By looking at the list `spock,rock,paper,scissors` you realize that `spock` and `rock` will be beating the `lizard`, and `paper` and `scissors` will get defeated by it. For `spock` it'll be almost the same, but it'll get beaten by `rock` and `paper`, and prevail over `scissors` and `lizard`. For the version of the game with 15 options, you can look at the picture above to understand the relationships between options.

Of course, this is not the most efficient way to determine which option prevails over which. You are welcome to try to develop some other methods of tackling this problem. 
