import random
from random import randint

given_tasks = ['Adjust engine output', 'Calibrate distributor', 
'Map course', 'Clear out O2 filter', 'Destroy asteroids', 
'Redirect power', 'Empty garbage', 'Secure wiring', 
'Fill engines tanks', 'Inspect laboratory', 'Move shields', 'Steady steering', 'Initiate reactor', 'Submit personal info', 
'Sign in with ID', 'Enable manifolds', 'Sync data']

class Character:
    '''
    Purpose: A character in a player elimination game
    Instance variables:
        self.name: character's name
        color: character's color
        hat: type of hat
        num_tasks: number of tasks
        status: character's health status
        task_list: list of tasks
    Methods:
        __init__: initializes instance variables
        repr(): returns character status
        get_identity(): returns 'Character'
    '''


    def __init__(self, name, color, hat, num_tasks):
        self.name = name
        self.color = color
        self.hat = hat
        self.num_tasks = num_tasks
        self.status = True
        self.task_list = random.sample(given_tasks, num_tasks)
    
    def __repr__(self):
        if self.status:
            status = 'Alive'
        else:
            status = 'Ghost'
        return(self.name + ': ' + self.color + ', wearing a ' + self.hat + ' - Health status: ' + status)

    def get_identity(self):
        return 'Character'

class Crewperson(Character):
    '''
    Purpose: specific methods for a crew person type character
    Instance variables: 
        self.name: character's name
        color: character's color
        hat: type of hat
        num_tasks: number of tasks
        task_list: list of tasks
    Methods: 
        __init__: initializes instance variables
        get_identity(): returns 'Crewperson'
        complete_task(): completes tasks
    '''
    def __init__(self, name, color, hat, num_tasks):
        Character.__init__(self, name, color, hat, num_tasks)
    
    def get_identity(self):
        return 'Crewperson'
    
    def complete_task(self):
        if len(self.task_list) != 1:
            print(self.name + ' has completed the ' + self.task_list[0] + ' task.')
            self.task_list.remove(self.task_list[0])
        else:
            self.task_list.remove(self.task_list[0])
            print(self.name + ' has completed all their tasks.')

class Pretender(Character):
    '''
    Purpose: specific methods for a pretender type character
    Instance variables: 
        self.name: character's name
        color: character's color
        hat: type of hat
        status: character's health status
        task_list: list of tasks
    Methods: 
        __init__: initializes instance variables
        get_identity(): returns 'Pretender'
        eliminate(self, target): eliminates target
    '''
    def __init__(self, name, color, hat, num_tasks):
        Character.__init__(self, name, color, hat, num_tasks)
    def get_identity(self):
        return 'Pretender'
    
    def eliminate(self, target):
        target.status = False
        print(self.name + ' eliminated ' + target.name)

class Game():
    '''
    Purpose: plays character elimination game
    Instance variables: 
        self.player_list: player objects list
    Methods: 
        __init__(): initializes instance variables
        check_winner(): checks if there is a winner
        meeting(): creates meeting for characters to vote on one character to eliminate
        play_game(): play game
    '''
    def __init__(self, player_list):
        self.player_list = player_list
    
    def check_winner(self):
        lstof_pretenders = []
        lstof_crewpersons = []
        crew_alive = 0
        pret_alive = 0
        for player in self.player_list:
            if player.get_identity() == 'Crewperson':
                lstof_crewpersons.append(player)
            else:
                lstof_pretenders.append(player)

        for c in lstof_crewpersons:
            if c.status:
                crew_alive += 1
        for p in lstof_pretenders:
            if p.status:
                pret_alive += 1
        
        completed_tasks = all(len(c.task_list) == 0 for c in lstof_crewpersons)
        pret_dead = all(p.status == False for p in lstof_pretenders)

        if completed_tasks or pret_dead:
            print('Crewpersons win!')
            return('C')
        elif pret_alive >= crew_alive:
            print('Pretenders win!')
            return('P')
        elif (completed_tasks or pret_dead) and (pret_alive >= crew_alive):
            print('Crewpersons win!')
            return('C')
        else:
            return('-')

    def meeting(self):
        alive_players = []
        for player in self.player_list:
          if player.status:
            alive_players.append(player)

        meetingTarget = random.choice(alive_players)

        for player in alive_players:
            print(player.name + ' voted for ' + meetingTarget.name)
        print(meetingTarget.name + ' was eliminated.')
        meetingTarget.status = False

    def play_game(self):
      
        flag = False
      
        while flag is False:
            for player in self.player_list:
                if player.get_identity() == 'Crewperson':
                    player.complete_task()
                elif player.get_identity() == 'Pretender' and player.status is True:
                    random_target = random.choice(self.player_list)
                    player.eliminate(random_target)
                
            
            if self.check_winner() == 'C':
                return self.check_winner()
            elif self.check_winner() == 'P':
                return self.check_winner()
            else:
                self.meeting()

            if self.check_winner() == 'C':
                return self.check_winner()
            elif self.check_winner() == 'P':
                return self.check_winner()