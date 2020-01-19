from tkinter import *

from tkinter import messagebox, simpledialog

import random

import time 

root=Tk()

root.title("A Grot's life 2")

root.geometry("400x400+900+200")



area_list=(" Woods of the Topsy Turvy King", "Forest of the Humourless Harlequins","Forgotten Graveyard of Ermm..","Castle of the Blackest Knight","Farm of Old McYondor","Bouncy Castle of Borgon",
         "Swamp of the Slimy Hobbits", "Lightest Dungeons", "Ruins of the Fallen Turnip God","Fun House of Eternal Damnation", "Wardrobes of Lady L Moore")


area_list1=("Heart of Darkness" ,"Doomville", "Red Jester's Torture Chamber","Temple of Apshai","Dungeons of Doom","Grot Fortress of Snikrik,","Hidden Hideout of Nine Dead Eyes",
            "Mountains of the Wild Berserker","Stronghold of Daggerfall","Walking Hills of Cthulhu","Forlorn Islands of Lost Souls"," Mysterious Swampland of Kuluth")

action_list=("an epic fight,","a violent revelation,","a grueling misadventure with your new comrade,","a sneaky attack from behind,","a one sided wrestling match,","a bone breaking dance showdown,",
             "a deadly game of tag,","an unfortunate stabbing incident,","a thumb war to the death,","a game of hide and seek that went horribly wrong,","a pathetic slap fight, ","taking an arrow to the knee,"
             ,"a heated argument that ended in a tragic death","an dishonourable duel")


action_list1=("an epic fight,","a violent struggle,","a bloody fight,","a magnificant duel,","a vicious battle,","a battle to the death,","a legendary fight that even your grandchildren will still be talking about,",
              "a surprise attack,","a narrow escape from being critically wounded,")

action_list2=("a narrow escape from impending doom,","barely surviving from the cosmic encounter,","a nightmareish struggle that left your mind consumed with terror,")
        
loot_list=["a fist full of straws","a fish bone","an old stick","a dirty potato sack","a rope"]

loot_list1=["some mechanical bits","a greater demon horn","a beholder eye","some crumbling stones","a giant shoe","a rusty umbrella",]

trader_list=["a greater demon horn","a beholder eye","a few pages of the Necronomicon","fragments of the Old Ones"]

loot_list2=["the statue of Mog","the statue of Gog","the statue of Krog"]

loot_list3=["a few pages of the Necronomicon","fragments of the Old Ones","an ancient bone flute"]

food_taste=["tasty","salty","disgusting","vile","smelly","delicious","foul"]

description_list=("a stupid","a heart broken","a deranged","a morbid","a tiny","a suicidal","a sexy","a skinny","a peaceful","a silly","a drunk","a sadistic","a young", "a shy","a talkative", "a nihilistic","a hungry",
                     "a dyslexic", "a lovestruck","a sarcastic","a forelorn","a happy","a friendly","a psychopathic","an optimistic","a mysterious","a beautiful","a malnourished","a zealous","a hot-headed","a mad","a drunk")


description_list1=("a stupid","a heart broken","a deranged","a morbid","a giant","a suicidal","a skinny","a racist","a drunk","a sadistic","a nihilistic","a tiny","a murderous","a evil","a heartless",
                    "a sarcastic","a homophobic","a forelorn","a psychopathic","a mysterious","a beautiful","a malnourish","a zealous","a hot-headed","hateful","a mad","a violent")

rumour=("'You need the power of a tank to face the Womb of Chaos'","'You can fully recover your health by hiring a room which also comes with a nice wormy dinner.'","'Craft items to make life easier for yourself.'","'Need more gold? Craft the Purse Snatcher.'",
        "'You can only find certain crafting material from specific areas,'","A long time ago,a grot became so popular that they were crowned the Grot King.'","'The Shadowland is much more dangerous than The land of Mad Jack'",
        "'You find yourself doing very silly things in the land of Mad Jack'","There is a hidden gambling den somewhere in the back of this Inn","Beware of that mysterious trader, he is up to no good")

game=("poker","dice","mahjong","bingo","rummy","roulette")

enemy_list2= ("dragon","demon","blob","zombie","vampire","beholder","troll","chaos giant","ettin","mimic","red jester",
            "succubus","bone devil","clay golem","drow","gnoll","swamp hag","night grot","half-ogre","hobgrot","bog imp","owlbear","winter wolf","chaos harlequin","abomination")



enemy_list1= ("hobbit","pony ","farmer","kobold","gnome","jester","harlequin","elf","druid","hill giant","grot","dwarf","werefish","cowman","imp","fairy","bandit","bard","hermit","ranger","thief","knight","rogue","orc","dragonkin")

enemy_list3= ("Azathoth","Shub-Niggurath","Cthulhu","The King in Yellow","Yog-Sothoth","Nug and Yeb")

inventory=[]
food=("psychedelic mushrooms","meaty bones","rotten apples","spoiled meat","mouldy bread","dead rats","foul smelling eggs","nutritious cow poo","jaw breaking nuts","black algae","plump worms","spicy fireflys")
larder=[]
goal=[""]

 


class Goblin(object):

    
    def __init__(self, name, hunger,health,provision,gold,reputation ):
        self.name = name
        self.hunger = hunger
        self.health= health
        self.provision= provision
        self.gold=gold
        self.reputation=reputation
        self.ranking= "Grot Cannon Fodder "
        self.end=False
        self.quest=1
        self.reward=0
        self.item=""
        self.doomday=10
        self.gamble=0



    def __pass_time(self):
        self.hunger -= 4
        self.stats()
        self.fight_death()
        self.hunger_death()
        self.rep()
        self.rank()
        self.health_warning()
        

        

    def message(self):
        answer = simpledialog.askstring("A Grots Life", "What is your name, You filthy Grot ?")
        if answer is None:
            answer="Snikrick"
        if answer =="":
            answer="Gutrot"

        self.name=answer 

        message=str(self.name)
        message+=(" ??? What a stupid name !! ")
        message+=("It suits you")
        message+=(". Now do what grots do... Kill, eat sleep till your heart explodes")
        message+=(" and maybe find a place where your grubby face can call home.                                 ------------------------------")
        message+=("If you think you are hard enough...")
        message+=("Someone stole the statues of our gods Mog,Gog and Krog. ")
        message+=("Old Man Blabgut saw them escaping towards the Womb of Chaos. ")
        message+=("Bring them back and you shall be rewarded ")


        lb_tasks.insert(0.0, message)
        self.rep()   # can also be gob.rep() really depends if you want it specific for an 'object' 

        

    def fight_death(self):
    
        if gob.health<=0:
            grotPic.config(image = ripphoto)
            messagebox.showinfo("RIP", "You have been wounded too many times, You have bled to death ")
            quit()

    def hunger_death(self):
     
        if gob.hunger<=0:
            grotPic.config(image = ripphoto)
            messagebox.showinfo("RIP", "You have starved to death")
            quit()
            
        

    def quit(self):
        MsgBox = messagebox.askquestion ('Exit game','Are you sure you want to retire your Grot ?',icon = 'warning')
        if MsgBox == 'yes':
            quit()
        else:
            pass

        


    def stats(self):

        stat="Hunger:"
        stat+=str(gob.hunger)
        stat+=" Health:"
        stat+=str(gob.health)
        stat+=" Provisions:"
        stat+=str(gob.provision)
        stat+=" Gold:"
        stat+=str(gob.gold)

        lbl_stat_lbl["text"]=stat



    def rep(self):

        message="Reputation: "
        message+=str(gob.reputation)
        message+="  Name: "
        message+=str(gob.name)

        lbl_stat_lb3["text"]=message

    def scavenge(self,stash=2):

        grotPic.config(image = huntphoto)


        if ("Grub Net") in goal :
            
            
            grub=random.choice(food)
            self.provision+=4
            larder.append(grub)
            larder.append(grub)
            message="Using your Grub Net,"
            message+=" you scavenge a bunch of "
            message+=str(grub)
            message+=". You gain "
            message+=str(4)
            message+=" provisions."
            lb_tasks.delete(0.0, END)
            lb_tasks.insert(0.0, message)
            self.__pass_time()

        else: 

            
        
            grub=random.choice(food)
            self.provision+= stash
            larder.append(grub)
            message="You have found some "
            message+=str(grub)
            message+=". You have gained "
            message+=str(stash)
            message+=" provisions"
            lb_tasks.delete(0.0, END)
            lb_tasks.insert(0.0, message)
            self.__pass_time()


    def eat(self, eat = 12,stew=24):
        
     
        if self.hunger >=104:
            grotPic.config(image = normalphoto)
            message="You are not hungry"
            lb_tasks.delete(0.0, END)
            lb_tasks.insert(0.0, message)

        elif self.provision>0 and ("Stone Pot") in goal :
            grotPic.config(image = eatphoto)
            mep=random.choice(larder)
            larder.remove(mep)
            self.hunger += stew
            if self.hunger>104:
                self.hunger=104

            self.provision-=2

            message= "You make some comforting stew with your "          
            message+=str(mep)
            message+=" in your stone pot. "
            message+="You gobble it up like a good grot"
        

            lb_tasks.delete(0.0, END)
            lb_tasks.insert(0.0, message)

        elif self.provision>0:
            grotPic.config(image = eatphoto)
            mep=random.choice(larder)
            tas=random.choice(food_taste)
            larder.remove(mep)
            self.hunger += eat

            if self.hunger>104:
                self.hunger=104

            self.provision-=2
           
            message="You eat some "
            message+=str(mep)
            message+=". It was a "
            message+=str(tas)
            message+=" snack."
          
            lb_tasks.delete(0.0, END)
            lb_tasks.insert(0.0, message)
                   
      
        else:
            grotPic.config(image = normalphoto)
            message=("You do not have any food")
            lb_tasks.delete(0.0, END)
            lb_tasks.insert(0.0, message)

        self.__pass_time()

    def second_win(self):
        grotPic.config(image = explorephoto)
        global window
        window=Tk()
        window.title("Explore")
        window.geometry("120x80+840+320")

        btn_add_task=Button(window,text="  Land of Mad Jack  ",fg="black",bg="white",command=gob.explore)
        btn_add_task.grid(row=1,column=0)

        btn_add_task=Button(window,text="      Shadow land      ",fg="black",bg="white",command=gob.explore1)
        btn_add_task.grid(row=2,column=0)

        btn_add_task=Button(window,text="   Womb of Chaos   ",fg="black",bg="white",command=gob.explore2)
        btn_add_task.grid(row=3,column=0)

        

       
        

    def explore(self):
        window.destroy()
        adventure=random.choice(area_list)
        description=random.choice(description_list)
        loot=random.choice(loot_list)
        action=random.choice(action_list)
        enemy=random.choice(enemy_list1)
        if ("Fish Bone Spear") in goal and not ("Grotonaut")in goal:
            message1=(" Armed with your Fish Bone Spear... ")
            lb_tasks.delete(0.0, END)
            damage=random.randint(1,10)
            self.health-=damage

        elif ("Grotonaut")in goal :
            message1=("Enclosed within a War Machine of Death...")
            lb_tasks.delete(0.0, END)
            damage=random.randint(1,2)
            self.health-=damage
           
            
        else:
            message1=("With a desire for adventure...")
            damage=random.randint(10,30)
            self.health-=damage
            lb_tasks.delete(0.0, END)

        
         
        message2="You explore the "
        message2+=str(adventure)
        message2+=". You come across "
        message2+=str (description)
        message2+=" "
        message2+=str(enemy)
        message2+=". After "
        message2+=str(action)
        message2+=" you took "
        message2+=str(damage)
        message2+=" damage. "
        

        if loot in inventory:
            message3= "You see nothing of interest"
            

            
        else:
            inventory.append(loot)
            message3="You find "
            message3+=str(loot)
            
        if ("Purse Snatcher") in goal : 
            coin=random.randint(10,20)
            self.gold+=(coin)
            message4= ". With your Purse Snatcher,"
            message4+=" no purse is safe"
            message4+=" you gain "
            message4+=str(coin)
            message4+=" gold"

        else:
            
            coin=random.randint(1,3)
            self.gold+=coin
            message4=". You gain "
            message4+=str(coin)
            message4+=" gold"

        lb_tasks.insert(0.0, message4)
        lb_tasks.insert(0.0, message3)
        lb_tasks.insert(0.0, message2)
        lb_tasks.insert(0.0, message1)
        self.stats()
        self.__pass_time()



    def explore1(self):
        window.destroy()
        adventure=random.choice(area_list1)
        description=random.choice(description_list1)
        loot=random.choice(loot_list1)
        action=random.choice(action_list1)
        enemy=random.choice(enemy_list2)
        
        if ("Fish Bone Spear") in goal and not ("Grotonaut")in goal:
            message1=(" Armed with your Fish Bone Spear... ")
            lb_tasks.delete(0.0, END)
            damage=random.randint(15,30)
            self.health-=damage

        elif ("Grotonaut")in goal :
            message1=("Enclosed within a War Machine of Death...")
            lb_tasks.delete(0.0, END)
            damage=random.randint(1,10)
            self.health-=damage
            
        else:
            message1=("With a lust for danger...")
            damage=random.randint(50,90)
            self.health-=damage
            lb_tasks.delete(0.0, END)

        
        message2="You explore the "
        message2+=str(adventure)
        message2+=". You come across "
        message2+=str (description)
        message2+=" "
        message2+=str(enemy)
        message2+=". After "
        message2+=str(action)
        message2+=" you took "
        message2+=str(damage)
        message2+=" damage. " 

        

        if loot in inventory:
            message3= "You see nothing of interest"
            

            
        else:
            inventory.append(loot)
            message3="You find "
            message3+=str(loot)

        if ("Purse Snatcher") in goal :
            coin=random.randint(35,65)
            self.gold+=(coin)
            message4= ". With your Purse Snatcher,"
            message4+=" no purse is safe"
            message4+=" you gain "
            message4+=str(coin)
            message4+=" gold"

        else:
            
            coin=random.randint(20,40)
            self.gold+=coin
            message4=". You gain "
            message4+=str(coin)
            message4+=" gold"
            


        lb_tasks.insert(0.0, message4)
        lb_tasks.insert(0.0, message3)
        lb_tasks.insert(0.0, message2)
        lb_tasks.insert(0.0, message1)
        self.stats()
        self.__pass_time()



    def explore2(self):
        window.destroy()
        loot =random.choice(loot_list3)
        enemy=random.choice(enemy_list3)
        action=random.choice(action_list2)
        if self.end==False:
            loot=random.choice(loot_list2)
            

        
        if ("Fish Bone Spear") in goal and not ("Grotonaut")in goal:
            message1=(" Armed with your Fish Bone Spear... ")
            lb_tasks.delete(0.0, END)
            damage=random.randint(100,120)
            self.health-=damage

        elif ("Grotonaut")in goal :
            message1=("Enclosed within a War Machine of Death...")
            lb_tasks.delete(0.0, END)
            damage=random.randint(15,35)
            self.health-=damage
            
        else:
            message1=("With an optimistic outlook...")
            damage=random.randint(200,999)
            self.health-=damage
            lb_tasks.delete(0.0, END)

        
         
        message2="You explore the "
        message2+=" The Womb of Chaos"
        message2+=". You come across"
        message2+=" "
        message2+=str(enemy)
        message2+=". After "
        message2+=str(action)
        message2+=" you took "
        message2+=str(damage)
        message2+=" damage. "
        

        if loot in inventory:
            message3= "You see nothing of interest"
            
        else:
            inventory.append(loot)
            message3="You find "
            message3+=str(loot)
            gob.end_game1()
            
        coin=random.randint(60,120)
        self.gold+=coin
        message4=". You gain "
        message4+=str(coin)
        message4+=" gold"

        lb_tasks.insert(0.0, message4)
        lb_tasks.insert(0.0, message3)
        lb_tasks.insert(0.0, message2)
        lb_tasks.insert(0.0, message1)
        self.stats()
        
        self.__pass_time()


    def rest(self):
        grotPic.config(image = restphoto)
     
        if self.health>=100:
            message=("You do not need rest")
            lb_tasks.delete(0.0, END)
            

        else:
      

            if("Straw Bed") in goal:
                message=("You rest better in your Straw Bed.")
                lb_tasks.delete(0.0, END)
                
                sleep=random.randint(18,30)
                

            else:
                message=("Sleeping on the rough floor...")
                lb_tasks.delete(0.0, END)
               
                sleep=random.randint(5,20)
             

            bob=self.health
            self.health+=sleep

            if self.health>=100:
                self.health=100

            recover= self.health-bob   
            message1=" You recover "
            message1+=str(recover)
            message1+=" health"
            lb_tasks.insert(0.0, message1)


        lb_tasks.insert(0.0, message)
        self.__pass_time()



 
    def craft_spear(self):
        grotPic.config(image = spearphoto)
        if ("Fish Bone Spear") in goal:
            grotPic.config(image = spearphoto)
            message="You only need one"
            message+="    ------------------------------"
            message+=" Good for stabbing gnomes and hobbits"
            
        elif "a fish bone" in inventory and "an old stick" in inventory:
            inventory.remove("a fish bone")
            inventory.remove("an old stick")
            goal.append("Fish Bone Spear")
            message="You have crafted a Fish Bone Spear"
            btn_add_task=Button(root,text="Fish Bone Spear",fg="red",bg="white",command=gob.craft_spear)
            btn_add_task.grid(row=1,column=3)
            grotPic.config(image = spearphoto)
            gob.end_game()

        else:
            grotPic.config(image = questionphoto)
            message="You do not have the crafting material "
            message+="    ------------------------------"
            message+=" Good for stabbing gnomes and hobbits"
            message+="    ------------------------------"
            message+="(Material: Stick and Bone )"
            message+="    ------------------------------"
            message+="Found in the land of Mad Jack"
            
            

        lb_tasks.delete(0.0, END)
        lb_tasks.insert(0.0, message)
    
        



    def straw_bed(self):
        if ("Straw Bed") in goal:
            grotPic.config(image = bedphoto)
            message="You only need one"
            message+="    ------------------------------"
            message+="Better than sleeping on the cold floor"
           
            
        elif "a fist full of straws" in inventory and "a dirty potato sack" in inventory:
            inventory.remove("a fist full of straws")
            inventory.remove("a dirty potato sack")
            goal.append("Straw Bed")    
            message=("You have crafted Straw Bed")
            btn_add_task=Button(root,text="    Straw Bed    ",fg="red",bg="white",command=gob.straw_bed)
            btn_add_task.grid(row=2,column=3)
            grotPic.config(image = bedphoto)
            gob.end_game()

        else:
            grotPic.config(image = questionphoto)
            message="You do not have the crafting material"
            message+="    ------------------------------"
            message+="Better than sleeping on the cold floor"
            message+="    ------------------------------"
            message+="(Material: Straw and Sack )"
            message+="    ------------------------------"
            message+="Found in the land of Mad Jack"

        lb_tasks.delete(0.0, END)
        lb_tasks.insert(0.0, message)
        
        



    def shoe_hut(self):
        
        if ("Shoe Hut") in goal:
            grotPic.config(image = housephoto)
            message="You only need one"
            message+="    ------------------------------"
            message+="A hut made out of a giant shoe, home sweet home !! "

        elif "some crumbling stones" in inventory and "a rusty umbrella" in inventory and "a giant shoe" in inventory:
            inventory.remove("some crumbling stones")
            inventory.remove("a rusty umbrella")
            inventory.remove("a giant shoe")
            goal.append("Shoe Hut")    
            message= "You have crafted a Shoe Hut"
            btn_add_task=Button(root,text="     Shoe Hut    ",fg="red",bg="white",command=gob.shoe_hut)
            btn_add_task.grid(row=6,column=3)
            grotPic.config(image = housephoto)
            gob.end_game()

        else:
            grotPic.config(image = questionphoto)
            message="You do not have the crafting material"
            message+="    ------------------------------"
            message+="A hut made out of a giant shoe, home sweet home !! "
            message+="    ------------------------------"
            message+="(Material: Umbrella, Stone and Shoe )"
            message+="    ------------------------------"
            message+="Found in the Shadow Land "

        lb_tasks.delete(0.0, END)
        lb_tasks.insert(0.0, message)
        


    def purse_snatcher(self):
        if ("Purse Snatcher") in goal:
            grotPic.config(image = snatcherphoto)
            message="You only need one"
            message+="    ------------------------------"
            message+=" Hook, pull and then RUN "

        elif "a fish bone" in inventory and  "a rope" in inventory:
            inventory.remove("a fish bone")
            inventory.remove("a rope")
            goal.append("Purse Snatcher")    
            message= "You have crafted a Purse Snatcher"
            btn_add_task=Button(root,text="Purse Snatcher",fg="red",bg="white",command=gob.purse_snatcher)
            btn_add_task.grid(row=4,column=3)
            grotPic.config(image = snatcherphoto)

        else:
            grotPic.config(image = questionphoto)
            message="You do not have the crafting material"
            message+="    ------------------------------"
            message+=" Hook, pull and then RUN "
            message+="    ------------------------------"
            message+="(Material: Bone and Rope)"
            message+="    ------------------------------"
            message+="Found in the land of Mad Jack"

        lb_tasks.delete(0.0, END)
        lb_tasks.insert(0.0, message)
        


    def stone_pot(self):
        grotPic.config(image = potphoto)
        if ("Stone Pot") in goal:
            grotPic.config(image = potphoto)
            message="You only need one"
            message+="    ------------------------------"
            message+="Good for making unicorn stew, just like Momma Grot "
            
        elif "some crumbling stones" in inventory and "a rope" in inventory:         
            inventory.remove("some crumbling stones")
            inventory.remove("a rope")
            goal.append("Stone Pot")    
            message= "You have crafted a Stone Pot"
            btn_add_task=Button(root,text="    Stone Pot    ",fg="red",bg="white",command=gob.stone_pot)
            btn_add_task.grid(row=5,column=3)
            grotPic.config(image = potphoto)
            gob.end_game()

        else:
            grotPic.config(image = questionphoto)
            message="You do not have the crafting material"
            message+="    ------------------------------"
            message+="Good for making unicorn stew, just like Momma Grot "
            message+="    ------------------------------"
            message+="(Material: Stone and Rope)"
            message+="    ------------------------------"
            message+="Found in the land of Mad Jack and Shadow land"


        lb_tasks.delete(0.0, END)
        lb_tasks.insert(0.0, message)
        
        
    def grub_net(self):
        
        if ("Grub Net") in goal:
            grotPic.config(image = netphoto)
            message="You only need one"
            message+="    ------------------------------"
            message+=" Gotta catch them all, all those tasty grubs"

        elif "a dirty potato sack" in inventory and "an old stick" in inventory:
            inventory.remove("a dirty potato sack")
            inventory.remove("an old stick")
            goal.append("Grub Net")    
            message= "You have crafted a Grub Net "
            btn_add_task=Button(root,text="     Grub Net    ",fg="red",bg="white",command=gob.grub_net)
            btn_add_task.grid(row=3,column=3)
            grotPic.config(image = netphoto)
            gob.end_game()

        else:
            grotPic.config(image = questionphoto)
            message="You do not have the crafting material "
            message+="    ------------------------------"
            message+=" Gotta catch them all, all those tasty grubs"
            message+="    ------------------------------"
            message+="(Material : Sack and Stick)"
            message+="    ------------------------------"
            message+="Found in the land of Mad Jack"

        lb_tasks.delete(0.0, END)
        lb_tasks.insert(0.0, message)
        



    def grotonaut(self):
        if ("Grotonaut") in goal:
            grotPic.config(image = robotphoto)
            message="You only need one"
            message+="    ------------------------------"
            message+="A war machine of immense power, when grots go wild !! "

        elif "some mechanical bits" in inventory and "a greater demon horn" in inventory and "a beholder eye" in inventory and "a rope"in inventory:
            inventory.remove("some mechanical bits")
            inventory.remove("a greater demon horn")
            inventory.remove("a beholder eye")
            inventory.remove("a rope")
            goal.append("Grotonaut")    
            message= "You have crafted a Grotonaut "
            btn_add_task=Button(root,text="    Grotonaut   ",fg="red",bg="white",command=gob.grotonaut)
            btn_add_task.grid(row=7,column=3)
            grotPic.config(image = robotphoto)

        else:
            grotPic.config(image = questionphoto)
            message="You do not have the crafting material"
            message+="    ------------------------------"
            message+="A war machine of immense power, when grots go wild !! "
            message+="    ------------------------------"
            message+="(Material:Demon horn, Beholder eye, rope and some mechanical bits) "
            message+="    ------------------------------"
            message+="Found in the land of Mad Jack and Shadow land"
            

        lb_tasks.delete(0.0, END)
        lb_tasks.insert(0.0, message)
    
        
        
    
    def inventory(self):
        grotPic.config(image = inventphoto)
        message="You have"
        message+=str(inventory)
        message+=" in your chest."
        message+="                     "
        message+="------------------------"
       # message+="                      crafted"
      #  message+=str(goal)
        
        
        lb_tasks.delete(0.0, END)
        lb_tasks.insert(0.0, message)



    def third_win(self):
        grotPic.config(image = pubphoto)
        global window
        window=Tk()
        window.title("Inn")
        window.geometry("150x80+840+350")

        btn_add_task=Button(window,text="  Drink 1g    ",fg="black",bg="white",command=gob.drink)
        btn_add_task.grid(row=1,column=0)

        btn_add_task=Button(window,text="  Round 10g  ",fg="black",bg="white",command=gob.round)
        btn_add_task.grid(row=1,column=1)
 
        btn_add_task=Button(window,text="  Room 120g ",fg="black",bg="white",command=gob.room)
        btn_add_task.grid(row=2,column=0)

        btn_add_task=Button(window,text="  Feast 200g ",fg="black",bg="white",command=gob.feast)
        btn_add_task.grid(row=2,column=1)

        btn_add_task=Button(window,text=" Mysterious Trader ",fg="black",bg="white",command=gob.trader)
        btn_add_task.grid(row=3,column=0,columnspan=2)

        btn_add_task=Button(window,text=" Gambling Den ",fg="black",bg="white",command=gob.fourth_win)
        btn_add_task.grid(row=4,column=0,columnspan=2)

    def fourth_win(self):
        window.destroy()
        grotPic.config(image = pubphoto)
        global window1
        window1=Tk()
        window1.title("?")
        window1.geometry("40x80+840+350")
        

        btn_add_task=Button(window1,text="  Place bet 250g       ",fg="black",bg="white",command=gob.low)
        btn_add_task.grid(row=1)

        btn_add_task=Button(window1,text="  Place bet 500g       ",fg="black",bg="white",command=gob.med)
        btn_add_task.grid(row=2)
 
        btn_add_task=Button(window1,text="  Place bet 1000g     ",fg="black",bg="white",command=gob.high)
        btn_add_task.grid(row=3)

    def low(self):
        window1.destroy()
        if 250 > self.gold:
            message="You do not have enough gold"

            lb_tasks.delete(0.0, END)
            lb_tasks.insert(0.0, message)   
        else:
            self.gamble=250
            self.dice()

            

    def med(self):
        window1.destroy()
        if 500 > self.gold:
            message="You do not have enough gold"

            lb_tasks.delete(0.0, END)
            lb_tasks.insert(0.0, message)   
        else:
            self.gamble=500
            self.dice()

    def high(self):
        window1.destroy()
        if 1000 > self.gold:
            message="You do not have enough gold "

            lb_tasks.delete(0.0, END)
            lb_tasks.insert(0.0, message)   
            
        else:
            self.gamble=1000
            self.dice()
            

    def dice(self):
        game1=random.choice(game)
        bet=int(self.gamble)
        bet1=bet*3
        guess=random.randint(1,3)
        die1=random.randint(1,4)
        if die1!=guess:
            message="you lose in a game of "
            message+=str(game1)
            message+=". Your lose "
            message+=str(bet)
            message+=" gold"
            
            self.gold-=bet
        else:
            message="You win in a game of "
            message+=str(game1)
            message+=". You gain "
            message+=str(bet1)
            message+=" gold"
            self.gold+=bet*3

        lb_tasks.delete(0.0, END)
        lb_tasks.insert(0.0, message)
        self.stats()
         
            


    def doom_day(self):

        if self.doomday==8:
            messagebox.showinfo("???","You are making some easy money from this shadowy figure")
            messagebox.showinfo("???","Is there more than meet the eyes ? ")

        if self.doomday==5:
            messagebox.showinfo("???","The shadowy being grins as he pay your fee")
            messagebox.showinfo("???","My precious Grot, the old ones thank you")

        
        if self.doomday==3:
            messagebox.showinfo("???","You have a strong feeling in your stomach")
            messagebox.showinfo("???","if you keep working with the trader, he will doom us all")

        if self.doomday==1:
            messagebox.showinfo("???","Your gut tells you not to bring anymore items to this being")
            messagebox.showinfo("???","It might be his evil smile but you have an inkling")
            messagebox.showinfo("???","He only needs one more thing to complete his 'work'")
        
        if self.doomday==0:
            messagebox.showinfo("RIP","As you leave the Inn, you hear the mysterious trader chanting")
            messagebox.showinfo("RIP","You turn around but a blinding light consume the room")
            messagebox.showinfo("RIP","You wake up in rubbles with your whole village destroyed")
            messagebox.showinfo("RIP","You watch a green mountain walk into the distance")
            messagebox.showinfo("Congratulations","Congrats you have found one of the secret endings.")
            messagebox.showinfo("Congratulations","  The End ( Game Written by Tommy Kwong )    " )
            quit()
            quit()

        else:
            pass
            
            
        
         


    def trader(self):

        window.destroy()
        if self.quest==1:
        
            #global quest  ( can be used instead of 'self.quest) 
            self.item=random.choice(trader_list)
            #global reward
            self.reward=random.randint(500,1000)
            self.quest=2
            message="If you find "
            message+=str(self.item)
            message+=". I will offer you "
            message+=str(self.reward)
            message+=" gold."


        else:
            if self.item in inventory:
                message="Well done, "
                message+="you have acquired the requested item for me."
                message+=" Here is your "
                message+=str(self.reward)
                message+=" gold."
                self.quest=1
                inventory.remove(self.item)
                self.gold+=(self.reward)
                self.doomday-=1
                self.doom_day()
        

                    

            else:
                message="Please come back when you have found "
                message+=str(self.item)
                message+="."
                

        lb_tasks.delete(0.0, END)
        lb_tasks.insert(0.0, message)        
                



    def drink(self):
        rumour1=random.choice(rumour)
        window.destroy()
        if self.gold>=1:
            message="You drink by yourself alone, so alone but you do hear a rumour. "
            message+=str(rumour1)
            self.gold-=1
            self.hunger+=4

        else:
            message="Bog off, you don't have enough gold"

         
        self.__pass_time()
        lb_tasks.delete(0.0, END)
        lb_tasks.insert(0.0, message)


    def round(self):
        
        window.destroy()
        
        if self.gold>=10:
            message="A round on you !! Your grot mates cheer you on. "
            message+="After retelling some of your misadventures, "
            message+="your grots mate respects you more."
            self.reputation+=1
            self.gold-=10
            self.hunger+=4

        else:
            message="Bog off, you are too poor ! "

        self.__pass_time()
        lb_tasks.delete(0.0, END)
        lb_tasks.insert(0.0, message)

    def feast(self):
        
        window.destroy()
        if self.gold>=200:
            message="All food and drinks on your tab !!"
            message+=" Everyone leaves with a fully belly, "
            message+="and greater admiration for you, thank you "
            message+=str(self.name)
            message+=". "
            self.reputation+=16
            self.gold-=200
            self.hunger=104

        else:
            message="Bog off, someone has a to pay for the food "

        self.__pass_time()
        lb_tasks.delete(0.0, END)
        lb_tasks.insert(0.0, message)


    def room(self):
        
        window.destroy()       
        if self.gold>=120:
            message="A soft cosy bed and a hot wormy dinner for your belly. "
            message+="What more can a grot ask for ?"
            self.gold-=120
            self.hunger=104
            self.health=100

        else:
            message="Bog off, no gold, no room ! "
    
        self.__pass_time()
        lb_tasks.delete(0.0, END)
        lb_tasks.insert(0.0, message)

            
        

    
        
            

    def add_task(self):
        pass


    def end_game(Self):

            
        if ("Fish Bone Spear") in goal and ("Straw Bed")in goal and("Shoe Hut") in goal and ("Stone Pot")in goal and ("Grub Net") in goal:
            messagebox.showinfo("Congratulations","You have built your home and proven you are a survivor !!")
            messagebox.showinfo("Congratulations","But is there more to life than just surviving ??")
           

    def end_game1(self):    # The reason why used gob not self was because Self hence why self did not work

        
        if ("the statue of Mog") in inventory and ("the statue of Gog")in inventory and("the statue of Krog") in inventory and gob.end == False:
            messagebox.showinfo("Congratulations","You have retrieved the stolen statues of the Grot Gods !!")
            messagebox.showinfo("Congratulations","You are rewarded with 500 gold and your reputation has increased.")
            self.reputation+=70
            self.gold+=500
            messagebox.showinfo("Congratulations","You can continue to play to find the secret endings")
            messagebox.showinfo("Congratulations","or retire your grot(Quit). Thank you for playing")
            self.end = True
            inventory.remove("the statue of Mog")
            inventory.remove("the statue of Gog")
            inventory.remove("the statue of Krog")
            
            self.__pass_time()
               


    def rank(self):
        ending=0

        if self.reputation >5 and self.reputation <10:
                self.ranking="Grot Simpleton"

        if self.reputation >10 and self.reputation <15:
                self.ranking="Grot Lackey"  

        if self.reputation >15 and self.reputation  <20:
                self.ranking="Grot underling"

        if self.reputation >20 and self.reputation  <30:
                self.ranking="Average Grot"

        if self.reputation >30 and self.reputation  <40:
                self.ranking="'Hard as Nails Grot"

        if self.reputation >40 and self.reputation  <60:
                self.ranking="Grot Champion"

        if self.reputation >60 and self.reputation  <150:
                self.ranking="Grot Hero"

        if self.reputation >150 and self.reputation  <250:
                self.ranking="Grot Legendary Hero"

        if self.reputation >250 and self.reputation  <500:
            self.ranking="The Grot Boss !! "

        if self.reputation >500 and self.reputation  <1000:
            self.ranking="The Grot Big Boss !! "

        if self.reputation >1000:
            self.ranking="The Grot KING !! "
            messagebox.showinfo("Congratulations","Feast after feast, drink after drink. ")
            messagebox.showinfo("Congratulations","The Grot elders decide to crown you King.")
            messagebox.showinfo("Congratulations","Long live the king !! Hail the Grot King !!")
            messagebox.showinfo("Congratulations","You live a life of luxury until your dying day.")
            messagebox.showinfo("Congratulations","Congrats you have found one of the secret endings.")
            messagebox.showinfo("Congratulations","  The End ( Game Written by Tommy Kwong )    " )
            quit()
            quit()
            
            


        rank= "Grot Ranking: "
        rank+= self.ranking


        lbl_stat_lb4["text"]=rank


    def health_warning(self):

        if self.hunger<16:
            hwarning="Hungry"

            lbl_stat_lb5["text"]=hwarning

        else:
            hwarning=""
            
            lbl_stat_lb5["text"]=hwarning


        


        if self.health<40:
            lwarning="Bleeding"

            lbl_stat_lb6["text"]=lwarning

        else:
            lwarning=""
            
            lbl_stat_lb6["text"]=lwarning


        

           
    
      

gob=Goblin("",100,100,0,8,0)



lbl_title=Label(root,text="Options", bg="white")
lbl_title.grid(row=0,column=0)

lbl_stat_lbl=Label(root,text=" Hunger:100  Health:100  Provision:0  Gold:8 ")
lbl_stat_lbl.grid(row=9,column=2)

lbl_stat_lb2=Label(root,text="Craft Items",bg="white")
lbl_stat_lb2.grid(row=0,column=3)

lbl_stat_lb3=Label(root,text=" Reputation:0 Name: ")
lbl_stat_lb3.grid(row=10,column=2)


lbl_stat_lb4=Label(root,text=" Grot Ranking: Grot Cannon Fodder ")
lbl_stat_lb4.grid(row=11,column=2)

lbl_stat_lb5=Label(root,text="")
lbl_stat_lb5.grid(row=8,column=0)

lbl_stat_lb6=Label(root,text="")
lbl_stat_lb6.grid(row=8,column=3)


btn_add_task=Button(root,text="    Quit     ",fg="black",bg="white",command=gob.quit)
btn_add_task.grid(row=1,column=0)

btn_add_task=Button(root,text="     Eat      ",fg="black",bg="white",command=gob.eat)
btn_add_task.grid(row=2,column=0)

btn_add_task=Button(root,text="Scavenge",fg="black",bg="white",command=gob.scavenge)
btn_add_task.grid(row=3,column=0)



btn_add_task=Button(root,text="  Explore  ",fg="black",bg="white",command=gob.second_win)
btn_add_task.grid(row=4,column=0)


btn_add_task=Button(root,text="     Rest     ",fg="black",bg="white",command=gob.rest)
btn_add_task.grid(row=5,column=0)

btn_add_task=Button(root,text="     Inn      ",fg="black",bg="white",command=gob.third_win)
btn_add_task.grid(row=6,column=0)

btn_add_task=Button(root,text="Inventory",fg="black",bg="white",command=gob.inventory)
btn_add_task.grid(row=7,column=0)

btn_add_task=Button(root,text="Fish Bone Spear",fg="black",bg="white",command=gob.craft_spear)
btn_add_task.grid(row=1,column=3)    

btn_add_task=Button(root,text="    Straw Bed    ",fg="black",bg="white",command=gob.straw_bed)
btn_add_task.grid(row=2,column=3)

btn_add_task=Button(root,text="     Grub Net    ",fg="black",bg="white",command=gob.grub_net)
btn_add_task.grid(row=3,column=3)

btn_add_task=Button(root,text="Purse Snatcher",fg="black",bg="white",command=gob.purse_snatcher)
btn_add_task.grid(row=4,column=3)

btn_add_task=Button(root,text="    Stone Pot    ",fg="black",bg="white",command=gob.stone_pot)
btn_add_task.grid(row=5,column=3)

btn_add_task=Button(root,text="     Shoe Hut    ",fg="black",bg="white",command=gob.shoe_hut)
btn_add_task.grid(row=6,column=3)

btn_add_task=Button(root,text="    Grotonaut   ",fg="black",bg="white",command=gob.grotonaut)
btn_add_task.grid(row=7,column=3)


eatphoto = PhotoImage(file=".\\art\\eat.gif")
normalphoto = PhotoImage(file=".\\art\\normal.gif")
huntphoto = PhotoImage(file=".\\art\\hunt.gif")
restphoto = PhotoImage(file=".\\art\\rest.gif")
explorephoto = PhotoImage(file=".\\art\\explore.gif")
pubphoto = PhotoImage(file=".\\art\\pub.gif")
inventphoto = PhotoImage(file=".\\art\\invent.gif")
bedphoto = PhotoImage(file=".\\art\\bed.gif")
housephoto = PhotoImage(file=".\\art\\house.gif")
netphoto = PhotoImage(file=".\\art\\net.gif")
potphoto = PhotoImage(file=".\\art\\pot.gif")
snatcherphoto = PhotoImage(file=".\\art\\snatcher.gif")
spearphoto = PhotoImage(file=".\\art\\spear.gif")
ripphoto = PhotoImage(file=".\\art\\rip.gif")
robotphoto = PhotoImage(file=".\\art\\robot.gif")
questionphoto = PhotoImage(file=".\\art\\question.gif")

grotPic = Label(root, image=normalphoto)
grotPic.grid(row=8,column=2)

lb_tasks=Text(root, width =30, height=15, wrap=WORD)
lb_tasks.grid(row=0,column=2,rowspan=8,columnspan=1,sticky= W) 




gob.message()
root.mainloop()




   
        









    

    




