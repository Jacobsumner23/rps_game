#!/usr/bin/env python
# coding: utf-8

# In[11]:


import random

while True: 
    print('Chose your weapon.\nRock, Paper, Scissors or "quit":')
    
    choice = str(input())
    choice = choice.lower()
    print("You chose", choice)
    
    weapon_lst = ['rock', 'paper', 'scissors']
    computer = random.choice(weapon_lst)
    print("Enemy chose", computer)

    if choice in weapon_lst:
        if choice == computer:
            print('Tie')
        if choice == 'rock':
            if computer == 'paper':
                print('Hold this L')
            elif computer == 'scissors':
                print('Winner winner chicken dinner!!')
        if choice == 'paper':
            if computer == 'scissors':
                print('You lose!')
            elif computer == 'rock':
                print('Great job you win!!')
        if choice == 'scissors':
            if computer == 'rock':
                print('Darn you lost.')
            elif computer == 'paper':
                print('You win!!')
    else:
        if choice == 'quit':
            break
       

    print()


# In[ ]:




