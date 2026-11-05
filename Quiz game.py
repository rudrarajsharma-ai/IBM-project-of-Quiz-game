class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.right = 0
        self.wrong = 0

    def add_right(self):
        self.right = self.right + 1
        self.score = self.score + 10

    def add_wrong(self):
        self.wrong = self.wrong + 1


topics = {"Basics", "Loops", "Data Structures", "Files", "OOP"}

questions = [
    {
        "q": "1. Which function takes input from the user?",
        "opts": ("A. input()", "B. print()", "C. get()", "D. read()"),
        "ans": "A"
    },
    {
        "q": "2. Which data type is immutable?",
        "opts": ("A. List", "B. Set", "C. Tuple", "D. Dictionary"),
        "ans": "C"
    },
    {
        "q": "3. Which keyword defines a function in Python?",
        "opts": ("A. func", "B. def", "C. create", "D. function"),
        "ans": "B"
    },
    {
        "q": "4. Which mode adds data to the end of a file?",
        "opts": ("A. r", "B. w", "C. a", "D. x"),
        "ans": "C"
    },
    {
        "q": "5. Which operator is used for exponentiation (power)?",
        "opts": ("A. ^", "B. **", "C. //", "D. %"),
        "ans": "B"
    },
    {
        "q": "6. Which statement is used to stop a loop early?",
        "opts": ("A. stop", "B. exit", "C. break", "D. pass"),
        "ans": "C"
    },
    {
        "q": "7. How do you insert an item at the end of a list?",
        "opts": ("A. .add()", "B. .append()", "C. .insert()", "D. .push()"),
        "ans": "B"
    },
    {
        "q": "8. Which collection stores data as key-value pairs?",
        "opts": ("A. Tuple", "B. List", "C. Set", "D. Dictionary"),
        "ans": "D"
    },
    {
        "q": "9. Which block catches errors in Python?",
        "opts": ("A. catch", "B. error", "C. except", "D. handle"),
        "ans": "C"
    },
    {
        "q": "10. What is the constructor method inside a Python class?",
        "opts": ("A. __init__()", "B. __main__()", "C. __start__()", "D. __new__()"),
        "ans": "A"
    }
]


def save_score(name, score, right, wrong):
    try:
        with open("scores.txt", "a") as f:
            f.write(f"Name: {name} | Score: {score} | Right: {right} | Wrong: {wrong}\n")
    except Exception:
        pass


def start_quiz():
    print("\n==============================")
    print("      PYTHON QUIZ PORTAL      ")
    print("==============================")
    name = input("Enter your name: ").strip()
    if name == "":
        name = "Player"
    player = Player(name)

    print("\nWelcome,", player.name)
    print("Topics covered:", topics)

    for item in questions:
        print("\n------------------------------------------")
        print(item["q"])
        for opt in item["opts"]:
            print("  ", opt)

        ans = input("\nYour answer (A/B/C/D): ").strip().upper()
        if ans == item["ans"]:
            print("-> Correct! (+10 pts)")
            player.add_right()
        else:
            print("-> Wrong! Correct answer was", item["ans"])
            player.add_wrong()

    total = len(questions) * 10
    percent = (player.score / total) * 100

    print("\n==========================================")
    print("       QUIZ REPORT -", player.name)
    print("==========================================")
    print(f"Total Questions : {len(questions)}")
    print(f"Right Answers   : {player.right}")
    print(f"Wrong Answers   : {player.wrong}")
    print(f"Final Score     : {player.score} / {total} ({percent}%)")
    print("==========================================")

    save_score(player.name, player.score, player.right, player.wrong)

    while True:
        cmd = input("\nType 'exit' to close the window: ").strip().lower()
        if cmd == "exit":
            break


start_quiz()