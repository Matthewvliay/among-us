import random
from random import randint

given_tasks = ['Adjust engine output', 'Calibrate distributor', 
'Map course', 'Clear out O2 filter', 'Destroy asteroids', 
'Redirect power', 'Empty garbage', 'Secure wiring', 
'Fill engines tanks', 'Inspect laboratory', 'Move shields', 'Steady steering', 'Initiate reactor', 'Submit personal info', 
'Sign in with ID', 'Enable manifolds', 'Sync data']

class Character():
    '''
    Purpose: A character in a social deduction game
    Instance variables: 
        self.name: name of the character, 
        color: color of the character, 
        hat: type of hat, 
        status: health status of player, which can be 'Ghost' or 'Alive',
        task_list: the list of tasks for a character
    and what does each represent in a few words?)
    Methods: 
        __init__: initializes instance variables
        repr(): returns the brief status for a character character
        get_identity(): returns 'Character'
    '''
    def __init__(self,name,color,hat,num_tasks):
        self.name = name
        self.color = color
        self.hat = hat
        self.status = True
        self.task_list = random.sample(given_tasks, num_tasks)
    def __repr__(self):
        status = 'Alive' if self.status else 'Ghost'
        return '{}: {}, wearing a {} - Health status: {}'.format(self.name, self.color, self.hat, status)
    def get_identity(self):
        return 'Character'

class Crewperson(Character):
    '''
    Purpose: inherited class of character with specialized methods for a crew person
    Instance variables: 
        self.name: name of the crew person, 
        color: color of the crew person, 
        hat: type of hat, 
        status: health status of player, which can be 'Ghost' or 'Alive',
        task_list: the list of tasks for the crew person
    Methods: 
    __init__(): initializes instance variables,
    get_identity(): returns identity 'Crewperson'
    complete_task(): completing a task 
    '''
    def __init__(self,name,color,hat,num_tasks):
        Character.__init__(self, name, color, hat, num_tasks)
    def get_identity(self):
        return 'Crewperson'
    def complete_task(self):
        if self.task_list == []:
            print('{} has completed all their tasks'.format(self.name))
            return 

        print('{} completed the {} task.'.format(self.name, self.task_list[0]))
        self.task_list.pop(0)

class Pretender(Character):
    '''
    Purpose: inherited class of character with specialized methods for a pretender
    Instance variables: 
        self.name: name of the pretender, 
        color: color of the pretender, 
        hat: type of hat, 
        status: health status of player, which can be 'Ghost' or 'Alive',
        task_list: list of tasks for the pretender
    Methods: 
    __init__(): initializes instance variables,
    get_identity(): returns identity 'Pretender',
    eliminate(self, target): eliminates a target 
    '''
    def __init__(self,name,color,hat,num_tasks):
        Character.__init__(self,name,color,hat,num_tasks)
    def get_identity(self):
        return 'Pretender'
    def eliminate(self, target):
        target.status = False
        print('{} eliminated {}.'.format(self.name, target.name))


# cp = Crewperson("Zaela", "White", "party hat", 4)
# print(cp.task_list)
# cp.complete_task()
# print(cp.task_list)
# cp = Crewperson("Greta", "Brown", "lab goggles", 4)
# pt = Pretender("Rachel", "Pink", "sticky note", 4)
# print(pt.name, pt.status, pt.get_identity(), pt.color, pt.hat)

class Game():
    '''
    Purpose: play a game of social deduction
    Instance variables: 
        self.player_list: list of player objects
    Methods: 
    __init__(): initializes instance variables,
    check_winner(): checks the winner of the game,
    meeting(): a meeting for players to vote who to eliminate
    play_game(): play the Game. 
    '''
    def __init__(self,player_list):
        self.player_list = player_list
    def check_winner(self):
        crew_people = [x for x in self.player_list if x.get_identity() == 'Crewperson']
        pretenders = [x for x in self.player_list if x.get_identity() == 'Pretender']
        crew_people_alive = 0
        pretenders_alive = 0
        # for player in self.player_list:
        #     if player.get_identity() == 'Crewperson':
        #         crew_people.append(player)
        #     else:
        #         pretenders.append(player)
        for cp in crew_people:
            if cp.status:
                crew_people_alive+=1
        for pt in pretenders:
            if pt.status:
                pretenders_alive+=1

        #check if crew people won        
        cp_tasks_complete = all(len(cp.task_list) == 0 for cp in crew_people) # T/F
        pretenders_eliminated = all(p.status == False for p in pretenders) # T/F
        if cp_tasks_complete or pretenders_eliminated:
            print('Crewpersons win!')
            return 'C'
        #check if pretenders won
        elif pretenders_alive >= crew_people_alive:
            print('Pretenders win!')
            return 'P'
        #check if crew people won
        elif (cp_tasks_complete or pretenders_eliminated) and (pretenders_alive >= crew_people_alive):
            print('Crewpersons win!')
            return 'C'
        else:
            return '-' 
    def meeting(self):
        vote_dict = {}
        alive = [x for x in self.player_list if x.status]
        print(self.player_list)
        for current_player in alive:
            rand_player = random.choice([x for x in alive if x != current_player]) # chooses anyone but the current person
            print('{} voted for {}'.format(current_player.name, rand_player.name))
            vote_dict[rand_player.name] = vote_dict.get(rand_player.name, 0) + 1

        most_voted = max(vote_dict, key=vote_dict.get)
        most_voted_list = [x for x, p in vote_dict.items() if p == vote_dict[most_voted]] # puts the most voted people with the same value in a list

        if len(most_voted_list) == 1: # if there is only one most voted person
            print('{} was elminated'.format(most_voted))
            person = [x for x in alive if x.name == most_voted_list[0]] # find the most voted person
            person[0].status = False
            return person[0].name
        elif len(most_voted_list) > 1: # two or more with the same highest number of votes
            print('Nobody was eliminated')

p_list = [Pretender("Jerry", "Blue", "mohawk", 4),
              Crewperson("Jackson", "Orange", "bird nest", 4),
              Crewperson("Yuchen", "Purple", "witch hat", 4),
              Crewperson("Zaela", "White", "party hat", 4),
              Crewperson("Audrey", "Lime", "wet floor sign", 4),
              Crewperson("Rachel", "Pink", "sticky note", 4),
              Crewperson("Nikhil", "Cyan", "pirate hat", 4),
              Pretender("Julia", "Yellow", "green fedora", 4),
              Crewperson("Greta", "Brown", "lab goggles", 4),
              Crewperson("Nate", "Red", "banana peel", 4)]
g = Game(p_list)

print(g.meeting())
