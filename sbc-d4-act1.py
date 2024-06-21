import random                                                   #Import library to randomize this game.

print("-" * 50)                                                 #We print a - 50 times to separate each execution.
player1 = input("Choose 'Kulob' or 'Hayang': ")                 #We use input function for the user input they choose.
                                                                #In this line we use while loop for input validation
while player1 not in ["Kulob", "Hayang"]:
    player1 = input("Invalid input! Enter 'Kulob' or 'Hayang': ") #Then if the player1 input a invalid choice.
choices = ["Kulob", "Hayang"]                                    #Then in this line we use choices as a variable with the list of the choises.
c2, c3 = choices[random.randint(0, 1)], choices[random.randint(0, 1)] #Then we convert the 0 and 1 integer into String choices "Kulob and Hayang".
print("-" * 50)
print(f"Player1   = {player1}\nComputer2 = {c2}\nComputer3 = {c3}") #Dre gi pang tawag nanato ang players sailang mga plangalan, player1 as Player1, c2 as Computer2, and c3 as a Computer3. \n it means "new line".
print("-" * 50)
result = "It's a tie!" if player1 == c2 == c3 else "Player1 WINS!" if player1 != c2 and player1 != c3 else f"{'Computer3' if c2 == player1 or c2 == c3 else 'Computer2'} WINS ✓"
print(result)
print("-" * 50)

# Condition1 = "It's a tie!" if player1 == c2 == c3
#1. Para sa last na condition, ang player1 and c2, c3 badaw kay equal? if equal then mo result syag "Its a tie!"
#2. After ma execute ang condition sa first "if statement" then we add "else statement" para after matuman ang first "if statement" si else ang mo buhat sa another logic.
# Condition2 = "Player1 WINS!" if player1 != c2 and player1 != c3
#3. Sa sulod ni else nag condition na sab tag second "if statement", if si player1 daw is not equal to c2 and c3 daog daw si Player1.
# else f"{'Computer3' if c2 == player1 or c2 == c3 else 'Computer2'} WINS ✓"
#4. Naa tay pang last na condition para kay c2 and c3, we use f strig para isa ray magamit na WINs string naka dependi nalang sa logic na mahitabo sa sulod sa f string and also sa random picking.
