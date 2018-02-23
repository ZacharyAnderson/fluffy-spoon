def tickets(people):
    quarters = 0
    fifties = 0
    hundreds = 0
    #While the queue of people is not at the end of line
    for i in people:
        #If customer has a 25$ bill
        if i == 25:
            quarters += 1
        #If customer has a 50$ bill
        elif i == 50:
            if quarters < 1:
                return "NO"
            else:
                fifties += 1
                quarters -= 1
        #If customer has a $100 bill
        elif i == 100:
            if (quarters >= 1 and fifties >= 1):
                quarters -= 1
                fifties -= 1
                hundreds += 1
            elif (quarters >=3):
                quarters -= 3
                hundreds += 1
            else:
                return "NO"
    return "YES"

'''
An "Avengers" ticket costs 25 dollars.
Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.
Can Vasya sell a ticket to each person and give the change if he initially has no money and sells the tickets strictly in the order people follow in the line?
Return YES, if Vasya can sell a ticket to each person and give the change with the bills he has at hand at that moment. Otherwise return NO.
### Python ###

tickets([25, 25, 50]) # => YES 
tickets([25, 100]) 
         # => NO. Vasya will not have enough money to give change to 100 dollars

'''