# to build a program which either encode or decode a word 

# encoding part 
a=input("Enter if you want to encode or decode: ")

if a=='encode':
    word1=input("Enter the word you want to encode: ")
    count_word=len(word1)  #counts the number of strings in the input word

    if count_word<3:
        encoded_word="".join(reversed(word1))                               #used to reverese the string
        print("The encoded version of the word you type is:",encoded_word)
    else:
        new_word=word1[1:]+word1[0]                      #used to remove the first letter and append it at the end of the string
        print("The new encoded letter is:","wer"+new_word+"gyt")

elif a=='decode':
    word2=input("Enter the word you want to decode: ")
    count_word2=len(word2)

    if count_word2<3:
        decoded_word="".join(reversed(word2))
        print("The decoded word for the word you entered is:",decoded_word)

    else:
        new_word2=word2[3:-3]
        final_word=new_word2[-1] + new_word2[:-1] #new_word[-1] gets the last letter from the word and new_word2[:-1] gets all the letter
                                                  #before the last letter and we join the two using +
        print("The decoded word is:",final_word)


