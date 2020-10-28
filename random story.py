import random as r

player_one = 'neo'
health = 100
inventory = []
information = []
#milestones = []
milestones = ['moscow', 'oslo', 'tokyo', 'nyc']

def show_inventory():
    print('inventory:', inventory)
    show_map()

def show_information():
    print('information:', information)
    show_map()

def show_milestones():
    print('milestones:', milestones)
    show_map()

def white_rabbit():
    print('wow', player_one, ', you really did it!')
    mission_one()

def brown_rabbit():
    print('oooops, it seems you took a wrong turn!')
    show_map()

def mission_one():
    print('welcome to your mission,', player_one)
    show_map()

def show_map():
    map = ['oslo', 'tokyo', 'moscow', 'nyc', 'johannesburg', 'beijing', 'inventory', 'exit']
    print('here is an overview of areas, make your choice where to go!')
    print(map)    
    answer = input("select an area: ").upper()
    if answer == "OSLO":        
        oslo_start()        
    elif answer == "TOKYO":
        tokyo_start()
    elif answer == "MOSCOW":
        moscow_start()
    elif answer == "NYC":
        nyc_start()
    elif answer == "JOHANNESBURG":
        not_unlocked()
    elif answer == "BEIJING":
        not_unlocked()       
    elif answer == "VIENNA":
        print('wow you found an easter egg!!')
        vienna_start() 
    elif answer == "RESTART":
        print('new game')
        start_game()
    elif answer == "INVENTORY":
        show_inventory()
    elif answer == "I":
        show_inventory()
    elif answer == "MILESTONES":
        show_milestones()
    elif answer == "M":
        show_milestones()
    elif answer == "INFO":
        show_information()
    elif answer == "EXIT":
        game_exit()
    else:
        print('it seems you made a speeling mistake. try again!')
        show_map()

def game_exit():
    print('inventory:', inventory)
    print('milestones:', milestones)
    print('come and play again soon.')
 
def not_unlocked():
    print('this area or mission is not unlocked yet')
    show_map()

def oslo_start():
    print('welcome to oslo,', player_one)
    print('you move along the streets of oslo. you find calm and peace. it feels like a quiet town.')
    answer = input('a norwegian guy comes your way. do you want to talk to him? ').upper()
    if answer == "YES":
        information.append('missing daughter')        
        answer = input('my daughter has been missing since the incident. will you help me find her? ').upper()
        if answer == "YES":
            print('that is an interesting suggestion. what can i do to help?')
            oslo_sidequest()
        elif answer == "NO":
            print('i can understand you. no worries. you might find some activity at the harbor. it usually gets busy after 5 pm.')
            oslo_harbor()
        else:
            oslo_start()       
    elif answer == "NO":
        print('you move along the street. as you stroll along you see the harbor and move along. there is a harbor at the distance')
        oslo_harbor()
    else:
        oslo_start()

def oslo_harbor():
    harbor = ['1. boat', '2. shop', '3. park']
    print('at the harbor you see', harbor, 'which place do you head next?')
    answer = input('did you make up your choice? press 1, 2 or 3 accordingly ').upper()
    if answer == "1":
        print('you are now searching the boat.')
        print('...')
        print('you just found a silver key.')
        inventory.append('silver key')
        print ('inventory:', inventory)
        print('lets move on and go to the park next.')
        oslo_harbor()
    elif answer == "2":
        print('you are now entering the shop.')
        if 'wallet' in inventory:
            answer = input('there is a knife on display. do you want to buy it? ').upper()
            if answer == "YES":
                inventory.append('knife')
                inventory.remove('wallet')
                print ('inventory:', inventory)
                print('nice. lets return to the harbor')
                oslo_harbor()
            elif answer == "NO":
                print('fair enough. lets return to the harbor.')
                oslo_harbor()
            else:
                print('something went wrong')
                oslo_harbor()
        else:
            print('it seems you dont have any monrey. maybe you should rather head to the park.')
            oslo_harbor()
    elif answer == "3":
        print('you are now heading towards the park.')
        oslo_park()
    else:
        print('it seems you made a typing mistake, try again')
        oslo_harbor()

def oslo_sidequest():
    print('coming up')
    oslo_harbor()

def oslo_park():
    print('at the opposite side you see the townhall building. you move over there and try to open the door. it is locked. do you have a key?')
    print('1. deploy your key 2. head back to the park')
    answer = input('press 1 or 2 ').upper()
    if answer == "1":
        if 'silver key' in inventory:
            print('nice the key worked. i am in.')
            oslo_success()
        else:
            print('i cannot open the door without they key. lets head back to the harbor')
            oslo_harbor()
    elif answer == "2":
        oslo_harbor()
    else:
        print('it seems you made a typing mistake, try again')
        oslo_harbor()

def oslo_success():
    print('congrats you have finished mission oslo')
    milestones.append('oslo')
    show_map()

def tokyo_start():
    print('welcome to tokyo,', player_one)
    print('the city is blinking and shiny. there appears a beautiful lady in a red dress.')
    answer = input('do you want to follow her? ').upper()
    if answer == "YES":
        tokyo_lady()
    elif answer == "NO":
        print('good call, she looks suspicious.')
        tokyo_start()
    else:
        print('it seems there was a typing error. try again.')
        tokyo_start()

def tokyo_lady():
    answer = input('it turns out the lady is an android for sex. do you want to engage further? ').upper()
    if answer == "YES":
        print('it seems you fell asleep for a while. something is odd. your inventory is gone. mika must have robbed you!')
        information.append('android mika')
        inventory.clear()
        show_inventory()
    elif answer == "NO":
        tokyo_start()
    else:
        tokyo_start()

def moscow_start():
    print('welcome to moscow,', player_one)
    print('it is freezing cold here. you see a guy in the allay wearing a coat. do have it in you to fight him?')
    moscow_alley = ['1. fight', '2. run']
    print (moscow_alley)
    answer = input('press 1 or 2 ').upper()
    if answer == "1":
        print('give me your coat! i am freezing..')
        moscow_fighting()
    elif answer == "2":
        print('good call, the guy looks like a bear')
    elif answer == "3":
        print('option not yet available')
    else:
        print('it seems you made a typing mistake, try again')
        moscow_start()

def moscow_fighting():
    print('do you want to start a fight?')
    player_one = r.randint(1, 6) + r.randint(1, 6)
    print('you stroke with a', player_one)    
    player_two = r.randint(1, 6) + r.randint(1, 6)
    print('your oponent stroke back with', player_two)
    if player_one  < player_two:
        print('oh no! you lost. all items are gone. return to the map')
        inventory.clear()
        show_inventory()
        show_map()
    elif player_one > player_two:
        print('congrats! you won the fight. take the coat and continue.')
        inventory.append('coat')
        inventory.append('wallet')
        print ('inventory:', inventory)
        moscow_success()
        show_map()
    else:
        print('it seems there is no victor.')
        show_map()

def moscow_success():
    print('congrats you have finished mission moscow')
    milestones.append('moscow')
    show_map()

def nyc_start():
    if 'oslo' in milestones:
        if 'moscow' in milestones:
            if 'tokyo' in milestones:
                print('welcome to NYC,', player_one)
                nyc_square()
            else:
                not_unlocked()
        else:
            not_unlocked()
    else:
        not_unlocked()

def nyc_square():
    print('you are in the middle of times square. more to come soon')
    show_milestones()
    show_map()

def vienna_start():
    print('welcome to vienna,', player_one)
    print('the UN area is currently empty.')
    show_map()

def start_game():
    inventory.clear()
    #milestones.clear()
    print('welcome to the dystopic afermath of humanities experiments with AI. not that there was a full out war, but the global order has been shattered, governments and financial instituations are gone and a strange mix of tech corporates, mafia, cyborgs and low tech robots roam the world now. it seems singuality has failed and general purpose AI disappeared.')
    print('hello neo! you are the one. look out for the white rabbit...')
    answer = input("a brown rabbit appears. do you want to follow the rabbit? (yes/no)").upper()
    if answer == "YES":        
        brown_rabbit()        
    elif answer == "NO":
        answer = input("now a white rabbit appears. do you want to follow the white rabbit? ").upper()
        if answer == "YES":
            white_rabbit()
        elif answer == "NO":
            show_map()
    elif answer == "MAYBE":
        print('wow you found an easter egg!!')
        inventory.append('easteregg')
        print ('inventory:', inventory)
        show_map()

start_game()