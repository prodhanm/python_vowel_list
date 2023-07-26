The point of this coding exercise was to take an existing exercise and take it one step further. The original exercise utilized only the vowel count of a single word. So in addition to this aspect of the exercise, the code was set to elevate the difficulty in three ways.

The first way is that instead of a single word, we are utilizing a lsit of words.
The second way was to use nested for loop to solve the problem. 
THe third way was to then go one step furhter, to list the vowels that are on each individual words. 

The result of the function, would display the number of vowels in each word and the list of vowels of each word. Here is an example of what the code produces:

    There are 5 vowels in abstemious.
    abstemious = ['o', 'u', 'e', 'i', 'a']

    word        w   vowels  count
    abstemious  1   a        1
                2   e       +1
                3   i       +1
                4   o       +1
                5   u       +1
    ______________________________________
                total_count  5   

What about in a situation where there are repeating vowels:
    There are 2 vowels in luxury.
    luxury = ['u']

    word        w   vowels  count
    luxury      1   u        1
                2   u       +1
    ______________________________________
                total_count  2

Notice that the list of the vowel for the word luxury is just 'u' listed once. The reason for that, is to ensure that the list is clean and does not clutter. In order to list the vowel once instead of twice in a list, the list had to be casted twice. Once as a set with the use of the set() to reduce the list with a reapeating value to once and then casting the now set list to a list with the use of the list(). By casting the values back and forth, we got the desired result.

There is an edge case to this code, where when testing the code, it did not count the capitalized vowel letter of an individual word. The use of the lower() method was used to solve the problem.
