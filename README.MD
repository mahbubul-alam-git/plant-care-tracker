Plant Care Tracker
A console-based Python application for managing plant watering schedules. This project uses object-oriented programming, inheritance, and file persistence (JSON/CSV) to let users add plants, track their last-watered dates, and determine when watering is due. All interactions occur through a simple text-based menu without any GUI or external APIs.
---
Features

Core Functionality
Add plants with attributes such as name, type, watering interval, and last-watered date
Store plants using Python classes to encapsulate behavior
Subclasses (e.g., Flower, Vegetable, Indoor plant) inherit from a Plant base class
Mark a plant as watered and automatically update its last-watered date
Check which plants need watering based on interval calculations

List all plants in a clean console output
Technical Highlights

OOP Principles: Encapsulation, inheritance, method overriding

File Persistence: Save and load plant data from a file (JSON or CSV)

Console UI: Menu-driven program using input() and print()

Datetime Logic: Uses Python's datetime module to compute water deadlines

Error Handling: Validates dates, numbers, and menu inputs to avoid crashes
---
Project Structure (Example)

project/
│
├── plant.py              # Base Plant class + subclasses
├── manager.py            # File handling + plant list operations
├── main.py               # Console menu loop
└── plants.json           # Stored data (auto-created)


---

How to Run

1. Clone the repository:

git clone https://github.com/<your-username>/plant-care-tracker.git


2. Navigate to the project folder:

cd plant-care-tracker


3. Run the app:

python main.py

---

How It Works (Conceptual Overview)

1. OOP and Inheritance

A Plant class stores common attributes like:

Name

Watering interval (days)

Last-watered date


Subclasses extend or override these based on plant type, for example:

class Cactus(Plant):
    def __init__(...):
        super().__init__(...)
        self.water_interval = 14  # Indoor plant needs less water

2. File Persistence

Plant data is stored in a JSON file:

Saved automatically after each update

Loaded on startup to restore plant list


3. Menu-Driven Console Interface

The program displays a text menu with actions such as:

Add new plant

View all plants

Mark plant as watered

Show plants needing water



---

Future Improvements (Optional)

Sorting by next watering date

Search/filter by name or type

Sunlight and location attributes

Automatic notifications (terminal-based)

Unit tests for classes and file handlers

Packaging as an installable Python module



---

License

This project is open-source and free to use.


---

If you want, I can also generate the full project folder with all Python files (main.py, plant.py, manager.py, JSON template) ready to copy and paste.
