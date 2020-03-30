from itertools import permutations
from tkinter import *


##USING TKINTER TO CREATE A TEXT WINDOW AND CUSTOMIZE TEXT

window = Tk()
window.title("WHIZZ")
window.configure(bg="LightCyan2")

txtMessages = Text(window, width=60,bg="azure")
txtMessages.grid(row=0, column=0, padx=10, pady=10)

txtYourMessage = Entry(window, width=50,bg="azure")
txtYourMessage.insert(0,"")
txtYourMessage.grid(row=1, column=0, padx=0, pady=0)

txtMessages.tag_config('you', background="azure", foreground="tomato",font = ('Comic Sans MS',14))
txtMessages.tag_config('bot', background="azure", foreground="DodgerBlue2",font = ('Comic Sans MS',14))
txtMessages.insert(END,"Disclaimer, this program uses brute force hence it may take some time to execute the problem so please be patient"+"\n\n")
txtMessages.insert(END, "Whizz: Heya! I'm Whizz and this is a 'Crypyarithematic' solver. I can Solve any puzzle, Just type it in this format :'xxxx + xxxx = xxxx' and try yourself!" + "\n\n" ,'bot')

##ALGO TO SOLVE THE CRYPTARITHEMATIC PROBLEM

def solve(string):
    expression, result = string.split(' = ')
    words = expression.split(' + ')
    unique_letters = []
    for character in string:
        if character.isalpha() and character not in unique_letters:
            unique_letters.append(character)
    # Loop over all possible permutations according to number of unique letters:
    for permutation in permutations(range(10), len(unique_letters)):
        # Assign numbers of current permutation to unique letters:
        letters_and_numbers = {}
        for letter, number in zip(unique_letters, permutation):
            letters_and_numbers[letter] = number
        # Calculate value of result using current letter & number pairs:
        result_value = ''
        for character in result:
            result_value += str(letters_and_numbers[character])
        # Skip to next permutation if value of result is invalid:
        if result_value.startswith('0'):
            continue
        # Calculate value of sum of words using current letter & number pairs:
        words_value = 0
        for word in words:
            word_value = ''
            for character in word:
                word_value += str(letters_and_numbers[character])
            # Skip to next permutation if value of word is invalid:
            if word_value.startswith('0'):
                continue
            words_value += int(word_value)
        # Print solution and break loop if a solution is found:
        if words_value == int(result_value):
            for letter, number in sorted(letters_and_numbers.items()):
                txtMessages.insert(END,f'{letter}: {number}'+"\n",'bot')
            break
txtMessages.insert(END,"\n\n")


###INITIALIZING BUTTONS AND THEIR FUNCTIONS

def insert():
    if __name__ == '__main__':
     sendMessage()
     txtYourMessage.delete(0, END)
     txtMessages.see("end")

def enterkey(event):
    insert()
window.bind('<Return>', enterkey)

def sendMessage():
    you = txtYourMessage.get()
    txtMessages.insert(END, "You: "+ you +  "\n\n",'you')
    txtMessages.insert(END, "Whizz: All individual exclusive values are:-" + "\n\n", 'bot')
    solve(you)

btnSendMessage = Button(window, text="Send", width=20, command=insert,bg="lavender")
btnSendMessage.grid(row=1, column=1, padx=1, pady=1)

window.mainloop()