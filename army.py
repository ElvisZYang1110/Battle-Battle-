from abc import ABC, abstractmethod
from referential_array import ArrayR, T
from stack_adt import ArrayStack
from queue_adt import CircularQueue


class Fighter(ABC):

    def __init__(self, life: int, experience: int) -> None:
        if type(self).__name__=="Soldier" or type(self).__name__=="Archer":
            self.life=3
            self.experience=0
        elif type(self).__name__=="Cavalry":
            self.life =4 
            self.experience=0
        else:
            raise ValueError("life and experience must great than 0 ")

        pass    




        
        


    def is_alive(self) -> bool:
# it returns True if the fighter’s life is greater than 0
# time complexity: min and max O(1)

        if self.life >= 0:
            return True
# return false if fighter's life is less than or = 0
        else:
            return False



    def lose_life(self, lost_life:int) -> None:
# time complexity: min and max O(1)
# it decreases the life of the unit by the amount indicated by lost life (by precondition, must be ≥ 0).
# check precondition
# param argue 1 the life lost 
# if precondition checked, life = life- lost_life
        if lost_life >=0:
            self.life = self.life - lost_life
            return self.life
        else:
            raise ValueError("lost_life must be greater than 0")
   



    def gain_experience(self, gained_experience: int) -> None:
# time complexity: min and max O(1)
# it increases the experience of the unit by the amount
# indicated by gained experience (by precondition, must be ≥ 0).
        if gained_experience <= 0:
            raise ValueError("gained_experience must be greater than 0")
# if precondition check, experience = experience + gained_experience
        if gained_experience > 0:
            self.experience = self.experience + gained_experience

    def get_experience(self) -> int:
# time complexity: min and max O(1)
# it returns the experience of the unit.
        return self.experience

        
    def get_unit_type(self) -> str:

        return self.get_unit_type





@abstractmethod 
def get_speed(self) -> int:
    # pass because abstract method
    pass

@abstractmethod
def get_cost(self) -> int:
    # pass because abstract method
    pass

@abstractmethod
def attack_damage(self) -> int:
    # pass because abstract method
    pass

@abstractmethod
def defend(self, damage: int) -> None:
    pass

@abstractmethod
def __str__(self) -> str:
    # pass because abstract method
    # here we define the string method and then put them into different classes 

    pass

@abstractmethod 
def get_experience (self)-> int:
    pass
     # pass because the abstract method 
 

class Soldier(Fighter):
    COST: int = 1
    SPEED: int = 0

    def __init__(self) -> None:
    # time complexity: min and max O(1)
    # access the fighter __init__ function using preset values
        Fighter.__init__(self, 3, 0)

    def get_speed(self) -> int:
# time complexity: min and max O(1)
# it returns the speed of the unit.
        Soldier.SPEED = 1 + self.experience
        return Soldier.SPEED

    def get_cost(self) -> int:
# time complexity: min and max O(1)
# it returns the cost of the unit.
        return self.cost

    def attack_damage(self) -> int:
# time complexity: min and max O(1)
# it returns the amount of damage performed by the unit when it attacks
# calls get_experience from Fighter class
        attack_damage = 1 + Fighter.get_experience(self)
        return attack_damage

    def defend(self, damage: int) -> None:
# time complexity: min and max O(1)
# decreases the life by the amount lost (if any) after defending from an attack that inflicted the
# amount of damage indicated by damage (by precondition, must be ≥ 0).
## param argue is the integer of damge 
# check precondition
        if damage < 0:
            raise ValueError("Cannot gain from damage")
# if damage is greater than experience
        if damage > Fighter.get_experience(self):
            self.life = self.life - 1
            return 1
        else:
            self.life = self.life
            return 0 


   


    

    def __str__(self) -> str:
# return string "Soldier’s life = X and experience = Y"
# time complexity: min and max O(1)
        life = self.life
        exp = self.experience
        return "Soldier's life = " + str(life) + " and experience = " + str(exp)


class Archer(Fighter):
    COST: int = 2
    SPEED: int = 3

    def __init__(self) -> None:
# time complexity: min and max O(1)
# access the fighter __init__ function using preset values
        Fighter.__init__(self, 3, 0)

    def get_speed(self) -> int:
# time complexity: min and max O(1)
# it returns the speed of the unit.
        return self.SPEED

    def get_cost(self) -> int:
# time complexity: min and max O(1)
# it returns the cost of the unit.
        return self.COST

    def attack_damage(self) -> int:
# time complexity: min and max O(1)
# it returns the amount of damage performed by the unit when it attacks
# call get_experience from Fighter class
        attack_damage = 1 + Fighter.get_experience(self)
        return attack_damage

    def defend(self, damage: int) -> None:
# time complexity: min and max O(1)
# produces change in life after attack
# check damage isn't less than 0
        if damage < 0:
            raise ValueError("No damage occurred")
# if damage >= 0, life = life - 1
        else:
            self.life = self.life - 1
            return 0

    def __str__(self) -> str:
# time complexity: min and max O(1)
# returns string of format "Archer’s life = X and experience = Y"
        life = self.life
        exp = self.experience
        return "Archer's life = " + str(life) + " and experience = " + str(exp)


class Cavalry(Fighter):
    COST: int = 3
    SPEED: int = 2

    def __init__(self) -> None:
# time complexity: min and max O(1)
# access the fighter __init__ function using preset value
        Fighter.__init__(self, 4, 0)

    def get_speed(self) -> int:
# time complexity: min and max O(1)
# it returns the speed of the unit.
        return self.SPEED

    def get_cost(self) -> int:
# time complexity: min and max O(1)
# it returns the cost of the unit.
        return self.COST

    def attack_damage(self) -> int:
# time complexity: min and max O(1)
# it returns the amount of damage performed by the unit when it attacks
# use get_experience from fighter class
# attack_damage = (2*experience) + 1
        attack_damage = (2 * Fighter.get_experience(self)) + 1
        return attack_damage

    def defend(self, damage: int) -> None:
# time complexity: min and max O(1)
# it decreases the life of the unit by the amount lost (if any) after
# defending from an attack that inflicted the amount of damage indicated by damage (by precondition, must be ≥ 0).
# check the precondition that damage is greater than or equal to 0
        if damage < 0:
            raise ValueError("Damage cannot be negative")
# if damage is greater get_experience/2 then life = life -1
        elif damage > (Fighter.get_experience(self) / 2):
            self.life = self.life - 1
            return 0
        else:
            self.life = self.life
            return 0

    def __str__(self) -> str:
# time complexity: min and max O(1)
# returns string of format "Cavalry’s life = X and experience = Y"
        life = self.life
        exp = self.experience
        return "Cavalry's life = " + str(life) + " and experience = " + str(exp)

# return "Cavalry's life = " + str(self.life) + " and experience = " + str(self.experience)


class Army(Soldier, Archer, Cavalry, ABC):

    def __init__(self) -> None:
        self.force=None 
        self.name=None 
 

 
# time complexity: min and max O(1)
       
  
    def choose_army(self, name: str, formation: int) -> None:

# time complexity: min O(1) and max O(n)
# The method then reads the input, ensures the user gave three integers s, a and c, and calls the internal
# method __correct_army_given(s, a, c) to ensure the input is valid.
#para1 take is the string of name 
#para2 take is the integer of formation 


       
#user input
        SAC = str(input("Player " + name + " choose your army as S A C where \n S is the number of soldiers, \n A is the number of archers, \n C is the number of cavalry:"))
#seperate each integar in string
        SAC = SAC.split(" ")
#convert to int
        S = int(SAC[0])
#check is int and greater than 0
        if type(S) is not int:
            raise ValueError("must be an int")
        if S < 0:
            raise ValueError("must be positive")
#convert to int
        A = int(SAC[1])
# check is int and greater than 0
        if type(A) is not int:
            raise ValueError("must be an int")
        if A < 0:
            raise ValueError("must be positive")
#convert to int
        C = int(SAC[2])
# check is int and greater than 0
        if type(C) is not int:
            raise ValueError("must be an int")
        if C < 0:
            raise ValueError("must be positive")


#if correct army given is correct then assign army with given values
        if self.__correct_army_given(S, A ,C) is True:
            self.__assign_army(name, S, A, C, formation)
            #print(self.force)
        else:
            raise ValueError("must be a correct army")


    def __correct_army_given(self, soldiers: int, archers: int, cavalry: int) -> bool:
# time complexity: min and max O(1)
# returns True if the numbers are valid, that is, if they are all >= 0, and the player did not spend more than
# the allocated budget. Otherwise, it returns False.
#para 1 take is integer of soldier 
#para2 take is that the integer number of archers 
#para 3 take si that the integer number of calvary 

        budget = soldiers+ archers+ cavalry
        if soldiers >= 0 and archers >= 0 and cavalry >= 0 and budget <= 30:
            return True
        else:
            return False


    def __assign_army(self, name: str, sold: int, arch: int, cav: int, formation: int) -> None:
# time complexity: min O(1) ,this is where formation is not 0 or 1 and max O(n) otherwise
# sets the formation of the army to either stack or queue form, depending on the value of formation. , pushes each purchased
#para1 is that the string of name 
# para 2 is the integer of number of soldiers
#para 3 is the integer number of archer 
# para4 s the integer of the Cavalry 
# para 5 is the integer of information, as this question, it will be zero 
        if formation != 0 and formation != 1:
            raise ValueError("formation must be 0 for stack or 1 for queue")
# stack
        if formation == 0:
#creates a stack of the appropriate size
            length = sold + arch + cav
            force = ArrayStack(length)
            s = Soldier()
            a = Archer()
            c = Cavalry()

     

# fighter into the player’s stack in the correct order FILO
            for i in range(cav):
                force.push(c)
            for i in range(arch):
                force.push(a)
            for i in range(sold):
                force.push(s)
#binds the name and force variables.
            self.force = force
            self.name = name
    
    
        elif formation==1:
            #this is queue method to append items into the circular queue 
            #using First out first in method 

            length=sold+arch+cav 
            force=CircularQueue(length)
            s=Soldier() 
            a=Archer()
            c=Cavalry()
            for i in range(sold):
                force.append(s)
            for i in range(arch):
                force.append(a)
            for i in range(cav):
                force.append(c)
            
            self.force=force
            self.name=name 



    def __str__(self) -> str:
# time complexity: min and max O(1)
#returns string of self.force
        Force=self.force
        output=str(Force)

        return output 






