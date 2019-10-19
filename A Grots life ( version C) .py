from tkinter import *

from tkinter import messagebox, simpledialog

import random

import time 

root=Tk()

root.title("Grots life")

root.geometry("400x400+400+400")




lootlist=["Fist Full of Straws","Fish Bone","Old Stick","Dirty Potato Sack","Crumbling Stones","Rusty Umbrella","Rope"]
enemylist=("Rat","Hobbit","Tiny Dragon","Drunk Human","Killer Bee")
inventory=[]
food=("Mushrooms","Meaty Bones","Rotten Apples","Spoiled Meat")
larder=[]
goal=[]



                  


class Goblin(object):

    
    def __init__(self, name, hunger,health,provision,gold ):
        self.name = name
        self.hunger = hunger
        self.health= health
        self.provision= provision
        self.gold=gold

    def __pass_time(self):
        self.hunger -= 2
        self.stats()
        self.fight_death()
        self.hunger_death()
        

    def message(self):
        answer = simpledialog.askstring("Input", "What is your name?")

        if answer is None:
            answer="Snikrick"
        if answer =="":
            answer="Gutrot"

        self.name=answer 

        
        message=("This is a survival game where you play a grot called ")
        message+=str(self.name)
        message+=(". Do what grots do... Kill, eat sleep till your heart explode")
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

    def scavenge(self,stash=2):
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


    def eat(self, eat = 5):
     
        if self.hunger >98:
            message="You are not hungry"
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
       
        loot=random.choice(lootlist)
        enemy=random.choice(enemylist)
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

        
         
            
        message2="You came across a "
        message2+=str(enemy)
        message2+=" After an epic fight you took "
        message2+=str(damage)
        message2+=" damage "
        

        if loot in inventory:
            message3= "You see nothing of interest"
            
            
        else:
            inventory.append(loot)
            message3=" But you find "
            message3+=str(loot)
            
            
        coin=random.randint(1,5)
        self.gold+=coin
        message4=" and "
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
                message=("You rest better in your Straw Bed")
                lb_tasks.delete(0.0, END)
                
                sleep=random.randint(10,30)
                

            else:
                message=("Sleeping on the rough floor... ")
                lb_tasks.delete(0.0, END)
               
                sleep=random.randint(5,20)
             

            bob=self.health
            self.health+=sleep

            if self.health>=100:
                self.health=100

            recover= self.health-bob   
            message1="You have recovered "
            message1+=str(recover)
            message1+=" health"
            lb_tasks.insert(0.0, message1)


        lb_tasks.insert(0.0, message)
        self.__pass_time()



 
    def craft_spear(self):
        if ("Fish Bone Spear") in goal:
            message="You only need one"
        elif "Fish Bone" and "Old Stick" in inventory:
            inventory.remove("Fish Bone")
            inventory.remove("Old Stick")
            goal.append("Fish Bone Spear")
            message="You have crafted a Fish Bone Spear"

        else:
            message="You do not have the crafting material"

        lb_tasks.delete(0.0, END)
        lb_tasks.insert(0.0, message)
        gob.end_game()
        



    def straw_bed(self):
        if ("Straw Bed") in goal:
            message="You only need one"
            
        elif "Fist Full of Straws" and "Dirty Potato Sack" in inventory:
            inventory.remove("Fist Full of Straws")
            inventory.remove("Dirty Potato Sack")
            goal.append("Straw Bed")    
            message=("You have crafted Straw Bed")

        else:
            message="You do not have the crafting material"

        lb_tasks.delete(0.0, END)
        lb_tasks.insert(0.0, message)
        gob.end_game()
        



    def shoe_hut(self):
        if ("Shoe Hut") in goal:
            message="You only need one"
            
        elif "Crumbling Stones" and "Rusty Umbrella" and "Rope" in inventory:
            inventory.remove("Crumbling Stones")
            inventory.remove("Rusty Umbrella")
            inventory.remove("Rope")
            goal.append("Shoe Hut")    
            message= "You have crafted a Shoe Hut" 

        else:
            message="You do not have the crafting material"

        lb_tasks.delete(0.0, END)
        lb_tasks.insert(0.0, message)
        gob.end_game()
        

        
    
    def inventory(self):
        message="You have"
        message+=str(inventory)
        message+=" in your bag"
        
        lb_tasks.delete(0.0, END)
        lb_tasks.insert(0.0, message)
        


    def add_task(self):
        pass


    def end_game(Self):
        if ("Fish Bone Spear") in goal and ("Straw Bed")in goal and("Shoe Hut") in goal:
            messagebox.showinfo("Congratulations","You have built your home and prove you are a survivor,YOU WIN !!")
            messagebox.showinfo("Congratulations","You can continue to play or quit the game,thank you for playing")                   





    

gob=Goblin("Bob",100,100,0,20)



lbl_title=Label(root,text="Options", bg="white")
lbl_title.grid(row=0,column=0)

lbl_stat_lbl=Label(root,text=" Hunger:0  Health:100  Provisions:0  Gold:20 ")
lbl_stat_lbl.grid(row=8,column=2)

lbl_stat_lb2=Label(root,text="Craft Items",bg="white")
lbl_stat_lb2.grid(row=0,column=3)

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

btn_add_task=Button(root,text="Craft",fg="black",bg="white",command=gob.add_task)
btn_add_task.grid(row=6,column=0)

btn_add_task=Button(root,text="Inventory",fg="black",bg="white",command=gob.inventory)
btn_add_task.grid(row=7,column=0)

btn_add_task=Button(root,text="Fish Bone Spear",fg="black",bg="white",command=gob.craft_spear)
btn_add_task.grid(row=1,column=3)

btn_add_task=Button(root,text="Straw Bed",fg="black",bg="white",command=gob.straw_bed)
btn_add_task.grid(row=2,column=3)

btn_add_task=Button(root,text="Shoe Hut",fg="black",bg="white",command=gob.shoe_hut)
btn_add_task.grid(row=3,column=3)



lb_tasks=Text(root, width =27, height=15, wrap=WORD)
lb_tasks.grid(row=0,column=2,rowspan=8,columnspan=8,sticky= W) 

gob.message()


root.mainloop()


   
        









    

    




