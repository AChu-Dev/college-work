import time
import random

def Chop_wood(a):
    Wood_val = a + random.randint(2,5)
    time.sleep(2)
    print('\n' + str(Wood_val) , 'Wood')
    return (Wood_val)

def Make_traps(a,b):
    Wood_val = a - 1
    Trap_val = b + random.randint(1,4)
    time.sleep(2)
    print('\n' + str(Wood_val) ,  'Wood |' , Trap_val , 'Traps' )
    return Wood_val , Trap_val

def Get_game(a , b):
    Trap_val = a - 1
    Game_val = b + random.randint(1 , 5)
    time.sleep(2)
    print('\n' + str(Trap_val) , 'Traps |' , Game_val, 'Game')
    return Trap_val , Game_val

def Mine_ore(a , b , c):
    Ore_val = a + random.randint(2 , 6)
    Coal_val  = b + random.randint(5 , 20)
    Game_val = c - 1
    time.sleep(2)
    print('\n' + str(Ore_val) , 'Ore |' , Coal_val , 'Coal |' , Game_val , 'Game')
    return Ore_val , Coal_val ,  Game_val

def Refine_ore(a , b , c):
    Metal_val = a + random.randint(2, 5)
    Coal_val = b - random.randint(2 , 5)
    Ore_val = c - random.randint(1 , 3)
    time.sleep(2)
    print('\n' + str(Metal_val) , 'Metal |' , Coal_val , 'Coal |' , Ore_val , 'Ore')
    return Metal_val , Coal_val , Ore_val

def Hire_lumberjack(a , b):
    x = 1
    while x < 10:
        a = a + random.randint(1 , 3)
        x = x + 1
    Metal_val = b - random.randint(1 , 4)
    time.sleep(2)
    print('\n' + str(a) , 'Wood |' , Metal_val , 'Metal')
    return a , Metal_val 

def Hire_miner(Metal_val , Coal_val , Game_val):
    x = 1
    while x < 10:
        Ore_val = a + random.randint(1, 4)
        Coal_val = b + random.randint(5 , 6)
        x = x + 1
    Game_val = c - random.randint(4 , 6)
    Metal_val = Metal_val - random.randint(1 , 3)
    time.sleep(2)
    print('\n' + str (Metal_val) , 'Metal |' , Coal_val , 'Coal |' , Ore_val , 'Ore')
    return Metal_val , Coal_val , Game_val

def Build_town (Wood_val , Traps_val , Game_val , Ore_val , Coal_val , Metal_val ):
    x = ('you win')
    Wood_val = Wood_val - 50
    Metal_val = Metal_val - 50
    x = x.title()
    time.sleep(2)
    print(x)
    print('\n' + str(Wood_val) , 'Wood |' , Metal_val , 'Metal')
    global town
    town = True
    return (Wood_val , Traps_val , Game_val , Ore_val , Coal_val , Metal_val )


def help_(Wood_val , Traps_val , Game_val , Ore_val , Coal_val , Metal_val ):

    print(' You Have\n\n' , Wood_val , 'Wood \n' , Traps_val , 'Traps \n' , Game_val , 'Game \n' , Ore_val , 'Ore \n' , Coal_val , 'Coal \n' , Metal_val , 'Metal')
    
    if Wood_val > 0:
        print ('\n' +'You can chop wood using command chop_wood')
        
    if Wood_val > 1:
        print('\n' +'You can make traps using command make_traps')
    else:
        print('\n' +'You need more wood')
        
    if Traps_val > 1:
        print('\n' +'You can collect game using command get_game')
    else:
        print('\n' +'You need more traps')
        
    if Game_val > 1:
        print('\n' +'You can mine ore using command mine_ore')
    else:
        print('\n' +'You need more game')
        
    if Ore_val > 1 and Coal_val > 7:
        print('\n' +'You can refine metal using command refine_ore')
    else:
        print('\n' +'You need more Ore & coal')
        
    if Wood_val > 0 and Metal_val > 4:
        print('\n' +'You can hire a lumberjack using command hire_lumberjack')
    else:
        print('\n' +'You need more metal')

    if Game_val > 6 and Metal_val > 3:
        print('\n' +'You can hire a miner using command hire_miner')
    else:
        print('\n' +'You need more game and more metal')

    if Wood_val > 50 and Metal_val > 50:
        print('\n' +'You can build a town using command build_town , but this will finish your adventure...')       
    else:
        print('\n' +'You need more wood and more metal' , '\n')

#------------------------------------------------MAIN PROGRAM----------------------------------------------------------------------
Ore_val = 0
Traps_val = 0 
Metal_val = 0 
Game_val = 0
Wood_val = 4 + random.randint(1 , 10)
Coal_val = 0


name= input("What is your name?")
time.sleep(2)
name = name.title()
print("Hello" , name ," ")
time.sleep(2)
print("This is your legend")
time.sleep(2)
print("In this adventure you will create a town from scratch....")
time.sleep(2)
print("But we must start at the begining")
time.sleep(2)
print("You are in a forest you have many choices to make \n")
time.sleep(2)

global town
town = False

while town is False:
    
    word=input('type help_ for a list of commands relative to the resources you have\n')
    word=word.lower()


    if word == 'help_':
        help_(Wood_val , Traps_val , Game_val , Ore_val , Coal_val , Metal_val)

    elif word == 'chop_wood':
        Wood_val = Chop_wood(Wood_val)

    elif word == 'make_traps' and Wood_val>= 1:
        values = Make_traps(Wood_val , Traps_val)
        a , b = values
        Wood_val = a
        Traps_val = b
        
    elif word == 'get_game'and Traps_val >=1:
        values = Get_game(Traps_val , Game_val)
        a , b = values
        Traps_val = a
        Game_val= b

    elif word == 'mine_ore' and Game_val >=1:
        values=Mine_ore(Ore_val , Coal_val , Game_val)
        a , b , c =values
        Ore_val = a
        Coal_val = b
        Game_val = c
        

    elif word == 'refine_ore' and Ore_val >=3 and Coal_val >=5:
        values=Refine_ore(Metal_val , Coal_val , Ore_val)
        a , b , c = values
        Metal_val = a
        Coal_val = b
        Ore_val = c

    elif word == 'hire_lumberjack' and Metal_val >= 4:
        values=Hire_lumberjack(Wood_val , Metal_val)
        a , b = values
        Wood_val = a
        Metal_val = b

    elif word == 'hire_miner' and Game_val >=6 and Metal_val >= 3:
       values= Hire_miner(Metal_val , Coal_val , Game_val)
       a , b, c = values
       Metal_val = a
       Coal_val  = b
       Game_val  = c

    elif word == 'build_town' and Metal_val >= 50 and Wood_val >= 50:
        values = Build_town(Wood_val , Traps_val , Game_val , Ore_val , Coal_val , Metal_val )
        a , b , c , d , e , f = values
        Metal_val = f
        Wood_val = a
        
    else:
        print('You cannot do that, it is either because your resources are too low or you have spelt the command wrong\n')
        help_(Wood_val , Traps_val , Game_val , Ore_val , Coal_val , Metal_val)

    




    
    
    
