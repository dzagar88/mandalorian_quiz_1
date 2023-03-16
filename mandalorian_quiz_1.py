# Dan Zagar
# Python 3.9.5
# Mandalorian Quiz


# Welcome
print("Welcome to the Mandalorian Quiz! Let's test your knowledge on The Mandalorian!")

# Score is tracked
score = 0
retry = 0

# Enter Name
player = input('First, enter your name here: ')
print('___')
print('___')

print('OK, ' + player + ", welcome to the quiz! Let's begin")
print('___')
print('___')

# Question 1:
# When does The Mandalorian take place?

question1 = False

print('#1: When does The Mandalorian take place?')
print('[A] 5 years after The Rise of Skywalker.     [B] 5 years after Return of the Jedi\n' + '[C] 5 years after The Phantom Menace         [D] 5 Years after Revenge of the Sith')

answer1 = 'b'

while question1 == False:
    input1 = (input('Enter A, B, C or D here: ')).lower()
    if input1 == answer1:
        score += 10
        print('Correct! The series takes place five years after the events of Return of the Jedi and 25 years prior to the events of The Force Awakens.')
        question1 == True
        break
    else:
        print('Try again!')
        retry += 1

print('___')
print('___')


# Question 2:
# What is the Mandalorian's name?

question2 = False

print("#2: What is the Mandalorian's name?")
print('[A] Greef Karga                [B] Fennec Shand\n' + '[C] He doesn' + "'" + 't have a name     [D] Din Djarin')

answer2 = 'd'

while question2 == False:
    input2 = (input('Enter A, B, C or D here: ')).lower()
    if input2 == answer2:
        score += 10
        print('Correct! Din Djarin, commonly known as "the Mandalorian" or "Mando" for short, is a bounty hunter during the New Republic Era.')
        question2 == True
        break
    else:
        print('Try again!')
        retry += 1

print('___')
print('___')


# Question 3:
# What is the Mandalorian's armor made of?

question3 = False

print("#3: What is the Mandalorian's armor made of?")
print('[A] Durium       [B] Beskar\n' + '[C] Mithril      [D] Carbonite')

answer3 = 'b'

while question3 == False:
    input3 = (input('Enter A, B, C or D here: ')).lower()
    if input3 == answer3:
        score += 10
        print('Correct! Beskar, also known as Mandalorian steel, is an alloy notable for its high tolerance to extreme forms of damage.')
        question3 == True
        break
    else:
        print('Try again!')
        retry += 1

print('___')
print('___')


# Question 4:
# In the first episode of The Mandalorian, Mando's Mythrol bounty mentions trying to get home for which holiday?

question4 = False

print("#4: In the first episode of The Mandalorian, Mando's Mythrol bounty mentions trying to get home for which holiday?")
print('[A] Freedom Day     [B] Durin' + "'" + 's Day\n' + '[C] Life Day        [D] Colonial Day')

answer4 = 'c'

while question4 == False:
    input4 = (input('Enter A, B, C or D here: ')).lower()
    if input4 == answer4:
        score += 10
        print('Correct! Life Day was a central part of the plot for the much maligned Star Wars Holiday Special (1978).')
        question4 == True
        break
    else:
        print('Try again!')
        retry += 1

print('___')
print('___')

# Question 5:
# What is the name of the Mandalorian's ship?

question5 = False

print("#5: What is the name of the Mandalorian's ship?")
print('[A] Razor Crest     [B] Slave I\n' + '[C] Ebon Hawk       [D] Rogue Shadow')

answer5 = 'a'

while question5 == False:
    input5 = (input('Enter A, B, C or D here: ')).lower()
    if input5 == answer5:
        score += 10
        print("Correct! A former military craft used to patrol local territories in the time before the Empire, the Razor Crest is the Mandalorian's trusty transport and living quarters as he scours the Outer Rim for fugitives.")
        question5 == True
        break
    else:
        print('Try again!')
        retry += 1

print('___')
print('___')

# Question 6:
# What did fans name "The Child"?

question6 = False

print('#6: What did fans name "The Child"?')
print('[A] Baby Mando     [B] Baby Jabba\n' + '[C] Baby Oola      [D] Baby Yoda')

answer6 = 'd'

while question6 == False:
    input6 = (input('Enter A, B, C or D here: ')).lower()
    if input6 == answer6:
        score += 10
        print('Correct! The Child, colloquially referred to as "Baby Yoda" by fans and the media, is a member of the same alien species as Jedi Master Yoda.')
        question6 == True
        break
    else:
        print('Try again!')
        retry += 1

print('___')
print('___')

# Question 7:
# What creature does Mando learn to ride on Arvala-7?

question7 = False

print('#7: What creature does Mando learn to ride on Arvala-7?')
print('[A] Blurrg     [B] Zabrak\n' + '[C] Bantha     [D] Noghri')

answer7 = 'a'

while question7 == False:
    input7 = (input('Enter A, B, C or D here: ')).lower()
    if input7 == answer7:
        score += 10
        print('Correct! Kuiil teaches the Mandalorian to ride a Blurrg in order to traverse the local terrain.')
        question7 == True
        break
    else:
        print('Try again!')
        retry += 1

print('___')
print('___')


# Question 8:
# What bounty hunter does the Mandalorian team up with to capture "The Child"?

question8 = False

print('#8: What bounty hunter does the Mandalorian team up with to capture "The Child"?')
print('[A] Bossk     [B] IG-11\n' + '[C] HK-47     [D] Cad Bane')

answer8 = 'b'

while question8 == False:
    input8 = (input('Enter A, B, C or D here: ')).lower()
    if input8 == answer8:
        score += 10
        print('Correct! Upon reaching the Nikto hideout, the Mandalorian is forced to team up with bounty droid IG-11. Together, they clear the facility of its guards and discover that the bounty is a green, big-eared, fifty-year-old infant.')
        question8 == True
        break
    else:
        print('Try again!')
        retry += 1

print('___')
print('___')

# Question 9:
# What does Mando trade with the Jawas who stripped his ship?

question9 = False

print('#9: What does Mando trade with the Jawas who stripped his ship?')
print('[A] The Horn     [B] The Claw\n' + '[C] The Egg      [D] The Child')

answer9 = 'c'

while question9 == False:
    input9 = (input('Enter A, B, C or D here: ')).lower()
    if input9 == answer9:
        score += 10
        print('Correct! The Mandalorian grudgingly bargains with the Jawas who agree to return his ship' + "'" + 's parts if he will retrieve "The Egg".')
        question9 == True
        break
    else:
        print('Try again!')
        retry += 1

print('___')
print('___')


# Question 10:
# What is Kuiil fond of saying?

question10 = False

print('#10: What is Kuiil fond of saying?')
print('[A] "I have spoken"                 [B] "So say we all"\n' + '[C] "May the force be with you"     [D] "It is finished"')

answer10 = 'a'

while question10 == False:
    input10 = (input('Enter A, B, C or D here: ')).lower()
    if input10 == answer10:
        score += 10
        print('Correct! When Kuiil wishes to put his foot down, he ends discussion with the phrase "I have spoken."')
        question10 == True
        break
    else:
        print('Try again!')
        retry += 1

print('___')
print('___')

# Game Over + Print Results

print("The end! Let's see how you did: ")
print('___')
print('___')
print('Name: ' + player)
print('Score: ' + str(score) + '%')
print('Retries: ' + str(retry))
print('Thanks for playing, ' + player + '!')

'''
Questions pulled from:
https://www.usefultrivia.com/movie_trivia/the_mandalorian_trivia.html
'''