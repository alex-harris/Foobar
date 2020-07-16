# Google Foobar Challenge

I recently got a funky pop up while doing some reading about Python and it turns out I had been invited to the Google Foobar challenge. After some quick searching I discovered it was a series of programming problems that Google uses for their 🤫*seeecret*🤫 hiring process. Although I'm not a programmer, I have been learning Python so I thought I'd give it a shot.

![foobar popup](images/foobar_popup.png)

## I want to play
Once you accept, you are taken to a Linux-y shell within Chrome where you can use a couple of commands to change directories and view files. The solutions can be written in either Java or Python. We begin the challenge as a lowly Minion :

Success! You've managed to infiltrate Commander Lambda's evil organization, and finally earned yourself an entry-level position as a Minion on her space station. From here, you just might be able to subvert her plans to use the LAMBCHOP doomsday device to destroy Bunny Planet. Problem is, Minions are the lowest of the low in the Lambda hierarchy. Better buck up and get working, or you'll never make it to the top...

## Level 1

The first challenge was not so bad, I found a translation chart on [wikipedia](https://en.wikipedia.org/wiki/Braille_ASCII) to help. The idea here is to map your string to the corresponding Braille, then use a loop to build the translated string from scratch.

Solution: [braille.py](Code/braille.py)

### Braille Translation

Because Commander Lambda is an equal-opportunity despot, she has several visually-impaired minions. But she never bothered to follow intergalactic standards for workplace accommodations, so those minions have a hard time navigating her space station. You figure printing out Braille signs will help them, and - since you'll be promoting efficiency at the same time - increase your chances of a promotion. 

Braille is a writing system used to read by touch instead of by sight. Each character is composed of 6 dots in a 2x3 grid, where each dot can either be a bump or be flat (no bump). You plan to translate the signs around the space station to Braille so that the minions under Commander Lambda's command can feel the bumps on the signs and ""read"" the text with their touch. The special printer which can print the bumps onto the signs expects the dots in the following order:
1 4
2 5
3 6

So given the plain text word ""code"", you get the Braille dots:

11 10 11 10
00 01 01 01
00 10 00 00

where 1 represents a bump and 0 represents no bump.  Put together, ""code"" becomes the output string ""100100101010100110100010"".

Write a function solution(plaintext) that takes a string parameter and returns a string of 1's and 0's representing the bumps and absence of bumps in the input string. Your function should be able to encode the 26 lowercase letters, handle capital letters by adding a Braille capitalization mark before that character, and use a blank character (000000) for spaces. All signs on the space station are less than fifty characters long and use only letters and spaces.

### Languages

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

### Test cases

Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution("code")
Output:
    100100101010100110100010

Input:
solution.solution("Braille")
Output:
    000001110000111010100000010100111000111000100010

Input:
solution.solution("The quick brown fox jumps over the lazy dog")
Output:
    000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110

-- Java cases --
Input:
Solution.solution("code")
Output:
    100100101010100110100010

Input:
Solution.solution("Braille")
Output:
    000001110000111010100000010100111000111000100010

Input:
Solution.solution("The quick brown fox jumps over the lazy dog")
Output:
    000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110

