import json
from datetime import datetime, timedelta # datetime module is timedelta,it's show difference between past and present time.
import os

file_name = "plant_info.json"

class Plant: 
    def __init__(self, category, name, water_interval, last_watered):
        self.category = category
        self.name = name
        self.water_interval = int(water_interval) # it's only take day in number.
        if isinstance(last_watered, str): # If it is a string, 
            try:
                self.last_watered = datetime.strptime(last_watered, "%d-%m-%Y") # the code tries to convert it into a datetime object.
            except ValueError:
                self.last_watered = datetime.now() # or give it defaults to current date.
        else:
            self.last_watered = last_watered # If last_watered is already a datetime object (not a string), it is stored as-is.

    def need_water(self):
        next_due = self.last_watered + timedelta(days=self.water_interval) # it's say next water needed (last watar date + water interval) day.
        return datetime.now().date() >= next_due.date() # it's compare today's date to water needed date and return True or False.

    def mark_watered(self):
        self.last_watered = datetime.now() # This method run whene you give water,it rewrite last watered.

    def to_dict(self): # obj to dict 
        return {
            "category": self.category,
            "name": self.name,
            "water_interval": self.water_interval,
            "last_watered": self.last_watered.strftime("%d-%m-%Y") # self.last watered is datetime obj,strftime("%d-%m-%Y") datetime -> string.
        }

class Flower(Plant):
    pass

class Vegetable(Plant):
    pass

class Indoor_plant(Plant):
    pass

def load_plants():
    plants = []
    if not os.path.exists(file_name): # if file was eptry then it will run without showing error for this line 
        return plants

    try:
        with open(file_name, "r", encoding="utf-8") as rdfi:
            data = json.load(rdfi) # json data -> python object
            
            for p in data: # json file loop and file category
                category = p.get("category") 
                obj = None
                
                if category == "Flower":
                    obj = Flower(**p) # **p means dict p send key-value arguments to constructor
                elif category == "Vegetable":
                    obj = Vegetable(**p)
                elif category == "Indoor_plant":
                    obj = Indoor_plant(**p)
                
                if obj:
                    plants.append(obj)
                    
    except (json.JSONDecodeError, ValueError):
        print("Error loading JSON file. Starting with empty list.")
        
    return plants # if everything look good then return with plants list

def save_plants(plants):
    with open(file_name, "w", encoding="utf-8") as wrfi:
        json.dump([p.to_dict() for p in plants], wrfi, indent=4) # it,s mean p object -> dict, it's called list comprehension

def add_plant(plants):
    print("\n--- Add a new Plant ---")
    name = input("Plant name: ")
    print("Select Plant Type: ")
    print("1. Flower")
    print("2. Vegetable")
    print("3. Indoor Plant")

    choice = input("Enter choice (1-3): ")
    
    category = ""
    cls = None

    if choice == "1":
        category = "Flower"
        cls = Flower
    elif choice == "2":
        category = "Vegetable"
        cls = Vegetable
    elif choice == "3":
        category = "Indoor_plant"
        cls = Indoor_plant # subclass
    else:
        print("Invalid choice")
        return

    try:
        water_interval = int(input("Water interval (days): "))
    except ValueError:
        print("Invalid number!")
        return

    last_watered = input("Last watered date (DD-MM-YYYY): ")

    try:
        datetime.strptime(last_watered, "%d-%m-%Y") # datetime convert str -> datetime obj
        
        obj = cls(category, name, water_interval, last_watered) # plant's subclass.When you call cls use plant proparty
        plants.append(obj)
        save_plants(plants)
        print("Plant added successfully!")
        
    except ValueError:
        print("Date format is wrong! Use DD-MM-YYYY")
        return

def view_plants(plants):
    print("\n--- Your plants ---")
    if not plants:
        print("No plants available!")
        return

    for i, p in enumerate(plants, start=1): # using enumerate for taking index and item, start=1 mean from index 1 start
        date_str = p.last_watered.strftime("%Y-%m-%d") # datetime obj formet,p.last_watered is datetime obj,finally gives = strftime("%Y-%m-%d") -> "2025-11-22"
        print(f"{i}. {p.name} ({p.category}) - Water every {p.water_interval} day - Last: {date_str}")

def check_plant(plants):
    print("\n--- Plants That Need Water ---")
    need = [p for p in plants if p.need_water()]

    if not need:
        print("No plant needs water today.")
        return

    for p in need:
        print(f"{p.name} ({p.category}) needs watering!")

def mark_plant_watered(plants):
    view_plants(plants)
    if not plants:
        return

    try:
        idx = int(input("\nEnter plant number to mark watered: ")) - 1
        if 0 <= idx < len(plants): # finding is this index valide or none
            plant = plants[idx] # pointing index number to category
            plant.mark_watered() # mark as watered
            save_plants(plants) # save in json file removing old watering date
            print(f"{plant.name} marked as watered!")
        else:
            print("Invalid selection")
    except ValueError:
        print("Invalid input")

def main():
    plants = load_plants() # if plants has data then load with data or load with empty list

    while True:
        print("\n========== PLANT CARE TRACKER ==========")
        print("1. Add a new plant")
        print("2. View all plants")
        print("3. Check plants needing water")
        print("4. Mark a plant as watered")
        print("5. Exit")

        choice = input("Enter a choice: ")

        if choice == "1":
            add_plant(plants)
        elif choice == "2":
            view_plants(plants)
        elif choice == "3":
            check_plant(plants)
        elif choice == "4":
            mark_plant_watered(plants)
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
