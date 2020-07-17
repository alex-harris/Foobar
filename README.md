# Google Foobar Challenge

I recently got a funky pop up while doing some reading about Python and it turns out I had been invited to the Google Foobar challenge. After some quick searching I discovered it was a series of programming problems that Google uses for their 🤫*seeecret*🤫 hiring process. Although I'm not a programmer, I have been learning Python so I thought I'd give it a shot.

![foobar popup](images/foobar_popup.png)

## I want to play
Once you accept, you are taken to a Linux-y shell within Chrome where you can use a couple of commands to change directories and view/edit files. The solutions can be written in either Java or Python. We start off as a lowly Minion :

Success! You've managed to infiltrate Commander Lambda's evil organization, and finally earned yourself an entry-level position as a Minion on her space station. From here, you just might be able to subvert her plans to use the LAMBCHOP doomsday device to destroy Bunny Planet. Problem is, Minions are the lowest of the low in the Lambda hierarchy. Better buck up and get working, or you'll never make it to the top...

## Level 1

Prompt: [Braille Translation](Questions/1_Braille_Translation.txt)

As you'll see in the prompt, Google gives you two test cases that should pass, but there are also **hidden** test cases that need to pass when you run your program. This became more of an issue in Level 3.

The first problem was not so bad, I found a translation chart on [wikipedia](https://en.wikipedia.org/wiki/Braille_ASCII) to help. The idea here is to map the characters in your string to the corresponding Braille, then use a for loop to build the translated string from scratch.

Solution: [braille.py](Code/braille.py)

## Level 2

Prompt: [Elevator Maintenance](Questions/2.1_Elevator_Maintenance.txt)

Level 2 had two problems, both seemingly straightforward but with some key components that needed to be implemented into the solutions. Make sure to read every detail in the prompts, so you don't spend half an hour questioning your logic when all you had to do was convert your output from integer to string.

![whoops](images/details.gif)

Solution: [elevator_maint.py](Code/elevator_maint.py)

#

After getting through Level 3, I realized that the second question in Level 2 could have been solved with a path finding algorithm. I had gone with a much more mathematical approach that is somewhat dependent on the chessboard's size. I'll be going back to retry this one.

Prompt: [Don't Get Volunteered!](Questions/2.2_Dont_Get_Volunteered.txt)

TL;DR, given a start and end point on a chessboard, return the minimum number of moves it would take a knight to get there.

| 0| 1| 2| 3| 4| 5| 6| 7|
|--|--|--|--|--|--|--|--|
| 8| 9|10|11|12|13|14|15|
|16|17|18|19|20|21|22|23|
|24|25|26|27|28|29|30|31|
|32|33|34|35|36|37|38|39|
|40|41|42|43|44|45|46|47|
|48|49|50|51|52|53|54|55|
|56|57|58|59|60|61|62|63|

Solution: [knight.py](Code/knight.py) ; _Better solution coming soon_

## Level 3

As someone who isn't a programmer, getting through two levels felt like a great accomplishment! Then Level 3 really kicked it up a notch.

Like I mentioned earlier, in addition to the two test cases are hidden cases that your program also needs to pass. In Level 3 this became an issue since I was fairly certain my code was working and I couldn't identify an edge case that would cause it to fail.

Prompt: [Bomb, Baby!](Questions/3.1_Bomb_Baby.txt)

I eventually realized here that my one failing case must have been caused by a timeout issue. Since the problem states that the input values can go up to 10^50, I needed to find a way to account for such large numbers. Reccursion seemed to be the way to go instead of a while loop. Using greatest common denominator to quickly identify the impossible cases also saves a lot of time. So, my first solution technically works...eventually.

Small number solution: [bomb_baby.py](Code/bomb_baby.py) ; Better solution: [bomb_baby2.py](Code/bomb_baby2.py)

#

Prompt: [Find the Access Codes](Questions/3.2_Find_the_Access_Codes.txt)

I really liked this one, but I ran into a similar situation again where one hidden test case was still failing. Even as I was coding it I had a feeling a triple nested for loop would be inefficient once the input list got sufficiently large.

Cubic solution: [accesscodes.py](Code/accesscodes.py) ; Better solution: [accesscodes2.py](Code/accesscodes2.py)

#



