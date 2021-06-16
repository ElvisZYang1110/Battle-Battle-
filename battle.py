 
from referential_array import ArrayR, T
from stack_adt import ArrayStack
from queue_adt import CircularQueue          #CircularQueue
from army import Army 

class Battle:


    def __init__(self):
# time complexity: min and max O(1)
        pass 
        
    def gladiatorial_combat(self, player_one: str, player_two: str) -> int:
         #read and create an army for each player and set those armies in stack formation and calls methods 
        #parameter 1 is the name in string format player_one 
        #parameter 2 is player_two and also in string format
        #for the best case and worse case is the same with the complexity O(1)

        
        if len(player_one)==0 or len(player_two)==0:
            raise ValueError("player's name should not be empyty")

        formation=0 
        army1=Army() 
        army2=Army()


        #create the abstract data 


        army1.choose_army(player_one,formation)
        army2.choose_army(player_two,formation)



        winner=Battle.__conduct_combat(self,army1,army2,formation)
        if winner==0:
            return "Two players are draws"

        if winner==1: 
            return" player_one wins"

        if winner ==2:
            return "player_two wins"
        pass 
           

    
    def fairer_combat(self, player_one: str, player_two: str) -> int:
        if len(player_one)==0 or len(player_two)==0:
            raise ValueError("player's name should not be empyty")

        formation=1 
        army1=Army() 
        army2=Army()



        army1.choose_army(player_one,formation)
        army2.choose_army(player_two,formation)



        winner=Battle.__conduct_combat(self,army1,army2,formation)

        print(winner)# This will return 0,1,2 on deciding which one is winner 

        
        if winner==0:
            print( "Two players are draws")

        if winner==1: 
            print( str(player_one)+" wins")

        if winner ==2:
            print( str(player_two)+" wins")
        pass 
           
           
            

    def __conduct_combat(self, army1: Army, army2: Army, formation: int) -> int:
         #conducts combat based on the formation of the two armies based on the formation of the two armies passed. Either
        #based on the formation of the two armies passed 
        # parameter 1will take army1 with property of Army class 
        #parameter 2 will take army2 with the porperty of Army classmethod
        #for the complexity is O(n) with n is the length of the two armies 
        #In this function the best case and worse case is exactly same  
        #for here if the formation is 1 it will go to the CircularQueue process 
        # if the formation is 0 it will go to the ArrayStack process 
        
        
        if formation==1: # if formation is equal to 1, this means queue 

            while army1.force.length!=0 and army2.force.length!=0:
                U1=army1.force.serve()
                U2=army2.force.serve()
                s=0 # this is defend damage
                a=0
                b=0
                c=0
            

                    #conduct the battle 
                    
                if U1.get_speed() > U2.get_speed():# when U1 speed > U2 speed 
                        #army1 attack first 
                    attack=U1.attack_damage()
                    s=U2.defend(attack) # army 2 defend 
                    U2.lose_life(s) # army 2 lose life 
                    if U2.is_alive():# if U2 is alive then U2 attack U1 defend 
                        attack1=U2.attack_damage()
                        a=U1.defend(attack1)
                        U1.lose_life(a)

                
                                    
                elif U1.get_speed()==U2. get_speed(): # when speed are equal, they will attack simutanously 
                    while U1.is_alive() and U2.is_alive():
                        attack2=U1.attack_damage()
                        b=U2.defend(attack2) # both of U1 and U2 attack and lost life 
                        U2.lose_life(b)
                        attack3=U2.attack_damage()
                        c=U1.defend(attack3)
                        U1.lose_life(c)

                    


    # trying to figure out which one is stil alive 
                if U1.is_alive() and U2.is_alive(): # if both of them alive just minus one life then push back 
                    U1.lose_life(1)
                    U2.lose_life(1)
                    army1.force.append(U1)
                    army2.force.append(U2)
                    break

                elif U1.is_alive():
                    U1.gain_experience(1)  # if U1 still alive get 1 experince 
                    army1.force.append(U1)
                    break 

                elif U2.is_alive():
                    U2.gain_experience(1) # if U2 still alive get 1 experience 
                    army2.force.append(U2)
                    break
# test which unit is going to be the winner 
            if army1.force.length==army2.force.length:
                return 0
            if army1.force.length>army2.force.length:
                return 1 
            if army1.force.length<army2.force.length:
                return 2 
# 0 is draw, 1 is U1 win, 2 is U2 win 
  
        if formation==0: # if formation is equal to zero this means that the defend method use queue 
             while army1.force.length!=0 and army2.force.length!=0:


                U1=army1.force.pop() # this is to 
                U2=army2.force.pop()
                s=0 # this is defend damage
                a=0
                b=0
                c=0
                

                        #conduct the battle 
                        
                if U1.get_speed() > U2.get_speed():
                            #army1 attack first 
                    attack=U1.attack_damage()
                    s=U2.defend(attack)
                    U2.lose_life(s)  # army 2 lose life 
                    if U2.is_alive():
                        attack1=U2.attack_damage()# if U2 is alive then U2 attack U1 defend 
                        a=U1.defend(attack1)
                        U1.lose_life(a)

                    
                                        
                                        
                elif U1.get_speed()==U2. get_speed():# when speed are equal, they will attack simutanously 
                    while U1.is_alive() and U2.is_alive():
                        attack2=U1.attack_damage()# both of U1 and U2 attack and lost life 
                        b=U2.defend(attack2)
                        U2.lose_life(b)
                        attack3=U2.attack_damage()
                        c=U1.defend(attack3)
                        U1.lose_life(c)

                    
                            


        # trying to figure out which one is stil alive 
                if U1.is_alive() and U2.is_alive(): # if both of them alive just minus one life then push back
                    U1.lost_life(1)
                    U2.lost_life(1)
                    army1.force.push(U1)
                    army2.force.push(U2)
                    break

                    
        

                elif U1.is_alive():# if U1 still alive get 1 experince 
                    U1.gain_experience(1)
                    break
                    
        

                elif U2.is_alive():# if U2 still alive get 1 experience 
                    U2.gain_experience(1)
                    break
        
        



# test which unit is winner 
        if army1.force.length==army2.force.length:
            return 0
        if army1.force.length>army2.force.length:
            return 1 
        if army1.force.length<army2.force.length:
            return 2 
# 0 is draw, 1 is U1 win, 2 is U2 win 





Battle.fairer_combat(Battle,"Tom","Jerry")        
                       


                
                      


 
    
