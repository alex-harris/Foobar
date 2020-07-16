# Google Foobar Challenge

I recently got a funky pop up while doing some reading about Python and it turns out I had been invited to the Google Foobar challenge. After some quick searching I discovered it was a series of programming problems that Google uses for their 🤫*seeecret*🤫 hiring process. Although I'm not a programmer, I have been learning Python so I thought I'd give it a shot.

![foobar popup](images/foobar_popup.png)

## I want to play
Once you accept, you are taken to a Linux-y shell within Chrome where you can use a couple of commands to change directories and view files. The solutions can be written in either Java or Python. We start off as a lowly Minion :

Success! You've managed to infiltrate Commander Lambda's evil organization, and finally earned yourself an entry-level position as a Minion on her space station. From here, you just might be able to subvert her plans to use the LAMBCHOP doomsday device to destroy Bunny Planet. Problem is, Minions are the lowest of the low in the Lambda hierarchy. Better buck up and get working, or you'll never make it to the top...

## Level 1

Prompt: [Braille Translation](Questions/1_Braille_Translation.md)

The first challenge was not so bad, I found a translation chart on [wikipedia](https://en.wikipedia.org/wiki/Braille_ASCII) to help. The idea here is to map your string to the corresponding Braille, then use a loop to build the translated string from scratch.

Solution: [braille.py](Code/braille.py)



Input:
Solution.solution("The quick brown fox jumps over the lazy dog")
Output:
    000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110

