def Main_Menu():
    print("\n===== 🏆 The Cave of the Lost Treasure 🪙  =====")
    print("\n1. Explore the Cave. 🪨 \n2. Treasure Hunt.🗺️💰 \n3. Resting State😴🏕️ \n4. Show Adventure Status 📜📊 \n5. Exit❌")

def Explore_the_cave(Health, Level):
    if Health > 0 and Health <= 100:
        Health -= 10
        Level += 1
        print(f"\n🔓Level {Level} Unlocked!🆙")
    else: print("\n🎮💀Adventure Over! No Lives Remaining!❤️❌")
    return Health, Level

def Treasure_Hunt(Health, Gold):
    if Health > 0 and Health <= 100:
        Health -= 5
        Gold += 20
        print("\n+20 Gold Coins! ✅")
    else: print("\n🎮💀Adventure Over! No Lives Remaining!❤️❌")
    return Health, Gold

def Resting_State(Health):
        if Health > 100:
            Health = 100
            print(f"\n💚 Health Restored! {Health} Health Points!⭐")
        elif Health > 0 and Health <= 100:
            Health += 15
            if Health > 100:
                Health = 100
                print(f"\n💚 Health Restored! {Health} Health Points!⭐")
        else: print("\n🎮💀Adventure Over! No Lives Remaining!❤️❌")
        return Health
        
def ShowAdventurerStatus(Name, Health, Gold, Level):
    print("\n===== 📊 Adventurer Status 📜 =====")
    print(f"\n👤 Name: {Name} \n❤️ Health: {Health} \n🪙 Gold: {Gold} \n⭐ Level:{Level}")
    
def Exit():
    print("👑 Quest Completed!🏅")

def Main():
    Adventure_Name = input("\n 🛡️ Create your adventurer: Enter a name: ")
    Health = 100
    Gold = 0
    Level = 1
    
    while True:
        Main_Menu()
        option = int(input("\n📜 Select an action:"))
        match option:
            case 1:
                Health, Level =    Explore_the_cave(Health, Level)
            case 2:
                Health, Gold = Treasure_Hunt(Health, Gold)
            case 3:
                Health = Resting_State(Health)
            case 4:
                ShowAdventurerStatus(Adventure_Name, Health, Gold, Level)
            case 5:
                Exit()
                break
            case _:
                print("\n⚠️ Invalid Option! Please try again.⚠️")
                
Main()