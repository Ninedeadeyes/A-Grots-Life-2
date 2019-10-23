from tkinter import *

from tkinter import messagebox, simpledialog

import random

import time 

root=Tk()

root.title("Grots life")

root.geometry("400x400+400+400")



area_list=("Forest of the Chaos Harlequins ","Forgotten Graveyard of Endal","Castle of the Blackest Knight","Haunted Farm of Yondor","Deathtrap Dungeon of Borgon"," Mysterious Swampland of Kuluth",
         "Swamp of the Slimy Hobbits", "Darkest Dungeons", "Ruins of the Fallen Gods", "Forlorn Islands of Lost Souls","Hidden Hideout of Nine dead eyes", "Wildlands of Lady L Moore"," Woods of Ypres","Heart of Darkness"
         ,"Doomville", "Red Jester's Torture Chamber","Goblins Fortress of Snikrik,","Temple of Apshai","Dungeons of Doom", "Mountains of the Wild Berserker","Stronghold of Daggerfall","Walking Hills of Cthulhu" )

action_list=("an epic fight,","a desperate struggle,","a violent accident,","a surprise attack,","completing a quest given,","a one sided wrestling match,","a deadly game of tag,","an unfortunate misunderstanding,")

loot_list=["a fist full of straws","a fish bone","an old stick","a dirty potato sack","some crumbling stones","a rusty umbrella","a rope","a blunt hook"]


description_list=("a stupid","a horny","a heart broken","a deranged","a morbid","a tiny","a suicidal","a sexy","a skinny","a racist","a peaceful","a silly","a drunk","a sadistic","a young", "a shy","a talkative",
                          "a lovestruck","a sarcastic","a homophobic","a forelorn","a happy","a friendly","a psychopathic","an optimistic","a mysterious","a beautiful","a malnourish","a zealous","a hot-headed")

enemy_list= ("orc","goblin","dragon","demon","kobold","blob","hobbit","zombie","gnome","vampire","beholder","troll","hill giant","ettin","mimic",
            "succubus","bone devil","clay golem","drow","gnoll","swamp hag"," night goblin","half-ogre","hobgoblin","bog imp","owlbear","pony","winter wolf","harlequin","abomination")
inventory=[]
food=("psychedelic mushrooms","meaty bones","rotten apples","spoiled meat","mouldy bread","dead rats","foul smelling eggs","nutritious cow poo","teeth breaking nuts",)
larder=[]
goal=[]



                  


class Goblin(object):

    
    def __init__(self, name, hunger,health,provision,gold,reputation ):
        self.name = name
        self.hunger = hunger
        self.health= health
        self.provision= provision
        self.gold=gold
        self.reputation=reputation
        self.ranking= "Grot Cannon Fodder "




    def __pass_time(self):
        self.hunger -= 2
        self.stats()
        self.fight_death()
        self.hunger_death()
        self.rep()
        self.rank()

        

    def message(self):
        answer = simpledialog.askstring("Input", "What is your name, You filthy Grot ?")

        if answer is None:
            answer="Snikrick"
        if answer =="":
            answer="Gutrot"

        self.name=answer 

        message=str(self.name)
        message+=(" ??? What a stupid name !! ")
        message+=("It suits you")
        message+=(". Now do what grots do... Kill, eat sleep till your heart explode")
        message+=(" and maybe find a place where your grubby face can call home")


        lb_tasks.insert(0.0, message)
       

        

    def fight_death(self):
    
        if gob.health<=0:
            messagebox.showinfo("RIP", "You have been wounded too many times, You have bled to death ")
            quit()

    def hunger_death(self):
     
        if gob.hunger<=0:
            messagebox.showinfo("RIP", "You have starved to death")
            quit()
            
        

    def quit(self):
        quit()


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


        if ("Grub Net") in goal :
            
            grub=random.choice(food)
            self.provision+=4
            larder.append(grub)
            larder.append(grub)
            message="Using your Grub Net,"
            message+=" you scavenge alot of "
            message+=str(grub)
            message+=" You gain "
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
            message+=" You have gained "
            message+=str(stash)
            message+=" provisions"
            lb_tasks.delete(0.0, END)
            lb_tasks.insert(0.0, message)
            self.__pass_time()


    def eat(self, eat = 5,stew=10):
     
        if self.hunger >90:
            message="You are not hungry"
            lb_tasks.delete(0.0, END)
            lb_tasks.insert(0.0, message)

        elif self.provision>0 and ("Stone Pot") in goal :            
            mep=random.choice(larder)
            larder.remove(mep)
            self.hunger += stew
            self.provision-=2

            message= "You make some comforting stew with your"          
            message+=str(mep)
            message+=" in your stone pot. "
            message+="You gobble it up like a good grot"
        

            lb_tasks.delete(0.0, END)
            lb_tasks.insert(0.0, message)

        elif self.provision>0:            
            mep=random.choice(larder)
            larder.remove(mep)
            self.hunger += eat
            self.provision-=2
           
            message="You eat some "
            message+=str(mep)
            message+=" It was a tasty treat"          

            lb_tasks.delete(0.0, END)
            lb_tasks.insert(0.0, message)
                   
      
        else:
            message=("You do not have any food")
            lb_tasks.delete(0.0, END)
            lb_tasks.insert(0.0, message)

        self.__pass_time()
        

    def explore(self):
        adventure=random.choice(area_list)
        description=random.choice(description_list)
        loot=random.choice(loot_list)
        action=random.choice(action_list)
        enemy=random.choice(enemy_list)
        if ("Fish Bone Spear") in goal:
            message1=(" Armed with your Fish Bone Spear... ")
            lb_tasks.delete(0.0, END)
            damage=random.randint(1,10)
            self.health-=damage
            
        else:
            message1=("Armed with your arms...")
            damage=random.randint(11,30)
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
            message4=". You manage to steal "
            message4+=str(coin)
            message4+=" gold"

        lb_tasks.insert(0.0, message4)
        lb_tasks.insert(0.0, message3)
        lb_tasks.insert(0.0, message2)
        lb_tasks.insert(0.0, message1)
        self.stats()
        
        self.__pass_time()



    def rest(self):
     
        if self.health>=100:
            message=("You do not need rest")
            lb_tasks.delete(0.0, END)
            

        else:
      

            if("Straw Bed") in goal:
                message=("You rest better in your Straw Bed.")
                lb_tasks.delete(0.0, END)
                
                sleep=random.randint(10,30)
                

            else:
                message=("Sleeping on the rough floor...")
                lb_tasks.delete(0.0, END)
               
                sleep=random.randint(5,20)
             

            bob=self.health
            self.health+=sleep

            if self.health>=100:
                self.health=100

            recover= self.health-bob   
            message1=" You have recovered "
            message1+=str(recover)
            message1+=" health"
            lb_tasks.insert(0.0, message1)


        lb_tasks.insert(0.0, message)
        self.__pass_time()



 
    def craft_spear(self):
        if ("Fish Bone Spear") in goal:
            message="You only need one"
        elif "a fish bone" in inventory and "an old stick" in inventory:
            inventory.remove("a fish bone")
            inventory.remove("an old stick")
            goal.append("Fish Bone Spear")
            message="You have crafted a Fish Bone Spear"

        else:
            message="You do not have the crafting material (Clue: Stick and ??? )" 

        lb_tasks.delete(0.0, END)
        lb_tasks.insert(0.0, message)
        gob.end_game()
        



    def straw_bed(self):
        if ("Straw Bed") in goal:
            message="You only need one"
            
        elif "a fist full of straws" in inventory and "a dirty potato sack" in inventory:
            inventory.remove("a fist full of straws")
            inventory.remove("a dirty potato sack")
            goal.append("Straw Bed")    
            message=("You have crafted Straw Bed")

        else:
            message="You do not have the crafting material (Clue: Straw and ???)"

        lb_tasks.delete(0.0, END)
        lb_tasks.insert(0.0, message)
        gob.end_game()
        



    def shoe_hut(self):
        if ("Shoe Hut") in goal:
            message="You only need one"
            
        elif "some crumbling stones" in inventory and "a rusty umbrella" in inventory and "a rope" in inventory:
            inventory.remove("some crumbling stones")
            inventory.remove("a rusty umbrella")
            inventory.remove("a rope")
            goal.append("Shoe Hut")    
            message= "You have crafted a Shoe Hut" 

        else:
            message="You do not have the crafting material (Clue: Umbrella, Stone and ???)"

        lb_tasks.delete(0.0, END)
        lb_tasks.insert(0.0, message)
        gob.end_game()


    def purse_snatcher(self):
        if ("Purse Snatcher") in goal:
            message="You only need one"

        elif "a blunt hook" in inventory and  "a rope" in inventory:
            inventory.remove("a blunt hook")
            inventory.remove("a rope")
            goal.append("Purse Snatcher")    
            message= "You have crafted a Purse Snatcher" 

        else:
            message="You do not have the crafting material( Clue: Hook and ???)"

        lb_tasks.delete(0.0, END)
        lb_tasks.insert(0.0, message)
        gob.end_game()


    def stone_pot(self):
        if ("Stone Pot") in goal:
            message="You only need one"

        elif "some crumbling stones" in inventory and "a rope" in inventory:
            inventory.remove("some crumbling stones")
            inventory.remove("a rope")
            goal.append("Stone Pot")    
            message= "You have crafted a Stone Pot" 

        else:
            message="You do not have the crafting material (Clue: ??? and Rope)"


        lb_tasks.delete(0.0, END)
        lb_tasks.insert(0.0, message)
        gob.end_game()
        
    def grub_net(self):

        if ("Grub Net") in goal:
            message="You only need one"

        elif "a dirty potato sack" in inventory and "an old stick" in inventory:
            inventory.remove("a dirty potato sack")
            inventory.remove("an old stick")
            goal.append("Grub Net")    
            message= "You have crafted a Grub Net " 

        else:
            message="You do not have the crafting material(Clue : Sack and ???) "

        lb_tasks.delete(0.0, END)
        lb_tasks.insert(0.0, message)
        gob.end_game()
        
        
    
    def inventory(self):
        message="You have"
        message+=str(inventory)
        message+=" in your chest."
        message+="                     "
        message+="------------------------"
        message+="                      crafted"
        message+=str(goal)
        
        
        lb_tasks.delete(0.0, END)
        lb_tasks.insert(0.0, message)
        
    def pub(self):
        if self.gold >=1 and self.gold <10:
            message="You drink by yourself, alone so alone "
            self.gold-=1
            self.hunger+=2

        elif self.gold >=10 and self.gold <50:
            message="A round on you !! Your grot mates cheer you on"
            self.gold-=10
            self.hunger+=2
            self.reputation+=1
            
        elif self.gold >=50:
            message="free drinks all night !! Tonight it is King "
            message+= str(self.name)
            
            self.gold-=50
            self.hunger+=2
            self.reputation+=6

        
            

        else:
            message="bog off, you can't even afford one drink"

        lb_tasks.delete(0.0, END)
        lb_tasks.insert(0.0, message)
        self.__pass_time()
        
            

    def add_task(self):
        pass


    def end_game(Self):
        if ("Fish Bone Spear") in goal and ("Straw Bed")in goal and("Shoe Hut") in goal and ("Stone Pot")in goal and ("Grub Net") in goal and ("Purse Snatcher") in goal :
            messagebox.showinfo("Congratulations","You have built your home and prove you are a survivor,YOU WIN !!")
            messagebox.showinfo("Congratulations","You can continue to play or quit the game,thank you for playing")                   


    def rank(self):

        if self.reputation >10 and self.reputation <20:
                self.ranking="Grot Lackey "  

        if self.reputation >20 and self.reputation  <40:
                self.ranking="Grot Rogue"

        if self.reputation >40 and self.reputation  <60:
                self.ranking="Grot Champion"

        if self.reputation >60 and self.reputation  <80:
                self.ranking="Grot Hero"

        if self.reputation >80 and self.reputation  <100:
                self.ranking="Grot Legendary Hero"

        if self.reputation >100 :
            self.ranking="Grot King "


        rank= "Grot Ranking: "
        rank+= self.ranking


        lbl_stat_lb4["text"]=rank


    

gob=Goblin("",100,100,0,20,0)



lbl_title=Label(root,text="Options", bg="white")
lbl_title.grid(row=0,column=0)

lbl_stat_lbl=Label(root,text=" Hunger:100  Health:100  Provision:0  Gold:20 ")
lbl_stat_lbl.grid(row=8,column=2)

lbl_stat_lb2=Label(root,text="Craft Items",bg="white")
lbl_stat_lb2.grid(row=0,column=3)

lbl_stat_lb3=Label(root,text=" Reputation:0 Name: ")
lbl_stat_lb3.grid(row=9,column=2)


lbl_stat_lb4=Label(root,text=" Grot Ranking: Cannon Fodder ")
lbl_stat_lb4.grid(row=10,column=2)


btn_add_task=Button(root,text="Quit",fg="black",bg="white",command=gob.quit)
btn_add_task.grid(row=1,column=0)

btn_add_task=Button(root,text="Eat",fg="black",bg="white",command=gob.eat)
btn_add_task.grid(row=2,column=0)

btn_add_task=Button(root,text="Scavenge",fg="black",bg="white",command=gob.scavenge)
btn_add_task.grid(row=3,column=0)

btn_add_task=Button(root,text="Explore",fg="black",bg="white",command=gob.explore)
btn_add_task.grid(row=4,column=0)

btn_add_task=Button(root,text="Rest",fg="black",bg="white",command=gob.rest)
btn_add_task.grid(row=5,column=0)

btn_add_task=Button(root,text="Pub",fg="black",bg="white",command=gob.pub)
btn_add_task.grid(row=6,column=0)

btn_add_task=Button(root,text="Inventory",fg="black",bg="white",command=gob.inventory)
btn_add_task.grid(row=7,column=0)

btn_add_task=Button(root,text="Fish Bone Spear",fg="black",bg="white",command=gob.craft_spear)
btn_add_task.grid(row=1,column=3)

btn_add_task=Button(root,text="Straw Bed",fg="black",bg="white",command=gob.straw_bed)
btn_add_task.grid(row=2,column=3)

btn_add_task=Button(root,text="Grub Net",fg="black",bg="white",command=gob.grub_net)
btn_add_task.grid(row=3,column=3)

btn_add_task=Button(root,text="Purse Snatcher",fg="black",bg="white",command=gob.purse_snatcher)
btn_add_task.grid(row=4,column=3)

btn_add_task=Button(root,text="Stone Pot",fg="black",bg="white",command=gob.stone_pot)
btn_add_task.grid(row=5,column=3)

btn_add_task=Button(root,text="Shoe Hut",fg="black",bg="white",command=gob.shoe_hut)
btn_add_task.grid(row=6,column=3)

lb_tasks=Text(root, width =27, height=15, wrap=WORD)
lb_tasks.grid(row=0,column=2,rowspan=8,columnspan=1,sticky= W) 

gob.message()
gob.rep()


root.mainloop()


   
        









    

    




