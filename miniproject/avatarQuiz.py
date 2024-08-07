#!/usr/bin/env python3


def main():
    #variables for our 4 nations, we'll add points to each based on the user answers and then see which has the most points to see which nations they belong to
    airNomads = 0;
    waterTribes = 0;
    fireNation = 0;
    earthKingdom = 0;

    #nation descripts for end of quiz
    airNomadDescription = "You're an Air Nomad! You like to take it easy and make friends along the way. But even though you're on the relaxed side of things, you're also incredibly resilient and will do whatever it takes to protect your friends."
    waterTribeDescription = "You belong to the Water Tribes! You like to go with the flow most of the time, and you're the one your friends turn to when they need advice. But as kind as you are, if something threatens your friends or family, you become a serious force to be reckoned with."
    fireNationDescription = "You're in the Fire Nation! You may have a hot temper at times, but it's just because you're so passionate. You sometimes react strongly to things, but it's because you care deeply."
    earthKingdomDescription = "You're a part of the Earth Kingdom! You're an unstoppable force! You don't let things get in your way when it comes to getting what you want, and when they do, you go right through them. But even though you're strong-willed, you have a fun and silly side, too."
    
    #questions and choices (thanks ChatGPT!)
    questions = [
    {
        "question": "1. You need to go into town, but there's a platypus bear on the only road. You...",
        "choices": [
            "A. Try to befriend it. Animals usually love you.",  # Air Nomads
            "B. Find another way, even if it means making your own path",  # Earth Kingdom
            "C. Convince some other travelers to confront the animal",  # Water Tribes
            "D. Barge right through. Nothing's gonna stop you."  # Fire Nation
        ]
    },
    {
        "question": "2. You accidentally destroy a cabbage seller's cart. What do you do?",
        "choices": [
            "A. Apologize profusely and ask what you can do to make it up.",  # Air Nomads
            "B. Offer him all the money in your pocket...even if it's not much",  # Earth Kingdom
            "C. Simply continue on your way",  # Water Tribes
            "D. Yell at him. Why is his cart parked in the middle of the street?!"  # Fire Nation
        ]
    },
    {
        "question": "3. You're in Ba Sing Se for vacation. What do you do first?",
        "choices": [
            "A. Go to Aang's zoo",  # Air Nomads
            "B. Visit the palace.",  # Earth Kingdom
            "C. Head over to the spa.",  # Water Tribes
            "D. Look for Lake Laogai."  # Fire Nation
        ]
    },
    {
        "question": "4. Which animal companion would you pick?",
        "choices": [
            "A. Flying bison",  # Air Nomads
            "B. Polar bear dog",  # Earth Kingdom
            "C. Dragon",  # Water Tribes
            "D. Bear...just a bear"  # Fire Nation
        ]
    },
    {
        "question": "5. You get an appointment with fortune teller Aunt Wu. You ask her to predict...",
        "choices": [
            "A. Nothing. There's only one big surprise in life, and you'd rather not know",  # Air Nomads
            "B. How successful you'll be",  # Earth Kingdom
            "C. Your love life",  # Water Tribes
            "D. Your most epic battle"  # Fire Nation
        ]
    },
    {
        "question": "6. Which baddie is your favorite?",
        "choices": [
            "A. Zaheer",             # Air Nomads
            "B. Sparky Sparky Boom Man",  # Earth Kingdom
            "C. Zuko",               # Water Tribes
            "D. Azula"               # Fire Nation
        ]
    },
    {
        "question": "7. You're granted access to the Knowledge Spirit's library. What information do you seek?",
        "choices": [
            "A. What happened to Zuko's mom?",    # Air Nomads
            "B. Did Jet really die?",            # Earth Kingdom
            "C. Who did Sokka end up marrying?", # Water Tribes
            "D. Did Chong, Lily, and Moku write more bangers after 'Secret Tunnel'?" # Fire Nation
        ]
    },
    {
        "question": "8. A more powerful bender has challenged you to an Agni Kai. You:",
        "choices": [
            "A. Avoid the fight by apologizing for whatever offense you caused.",  # Air Nomads
            "B. Accept. You can't lose face.",                                    # Earth Kingdom
            "C. Ask for a 2v2 fight and bring a powerful friend.",                # Water Tribes
            "D. Refuse. Why would I sign up to fail?"                              # Fire Nation
        ]
    }
]

    #variable to increment by one after a valid answer until the end of the question list of dictionaries           
    i=0;
    print()
    print("Welcome to our quiz! I hope you're ready to find out which nation you belong to from the world of Avatar, The Last Air Bender?")
    print()
#get userName, accept numbers but not pure whitespace- use try catch if userName has a value accept it and break, if it's an empty string raise a value error
    while True:
        try:
            userName = input("Please enter your name when you're ready to start the quiz: ").strip();
            if userName:
                break
            elif userName == "":
                raise ValueError("Come on, you can't leave your name blank!")
        except ValueError as error:
            print(error)
    print()
    print(f"Great, {userName}. Let's start!")
    print()
#while loop - keep going as long as i is less than the lengthe question array, which is 8
    while i< len(questions):
        # pull out our questions and choices
        question = questions[i]["question"]
        choices = questions[i]["choices"]
        #print question
        print(question)
        print()
        #iterate over choices array with for loop and print each choice
        for choice in choices:
            print(choice)
        print()
    
        #Make sure input is an a, b, c, or d.  Make it uppercase and trim it
        #Assign points to tribe variables based on answer
        #If an answer that's not a,b,c or d is given, user will be prompted to
        #give a valid answer and kicked back to the top of the look to answer 
        #again
        answer = input("Please choose A, B, C, or D: ").upper().strip()
        if answer == "A":
            airNomads += 10
            i += 1
        elif answer == "B":
            earthKingdom += 10
            i += 1
        elif answer == "C":
            waterTribes += 10
            i += 1
        elif answer == "D":
            fireNation += 10
            i += 1
        else:
            print()
            print(f"{userName}, that wasn't a valid answer, please choose A, B, C, or D :)")
            print()
            continue
        #max() returns the value of the variable with the max value
        
    result = max(airNomads, earthKingdom, waterTribes, fireNation)
        #compare max value to each of the nation totals, this is not perfect because if two natiosn are tied, it will assign the resutl to the first one in the if elif statements, but it is what it is
    nation =""
    if result == airNomads:
            nation = airNomadDescription
    elif result == earthKingdom:
        nation = earthKingdomDescription
    elif result == waterTribes:
            nation = waterTribeDescription
    elif result == fireNation:
            nation = fireNationDescription
    print()
    print(f"Ok {userName}, {nation} Thanks for taking our quiz!")
    print()
main()


