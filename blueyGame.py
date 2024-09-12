# My sister wanted me to make this for a while now and you know I'm not exactly an expert at coding at the moment. Matter of fact, I'll come clean and tell you that I've been asking ChatGPT some questions regarding the code because obviously it all doesn't work on the first try. With that said, bear with me.

def intro():
        print("Bluey and Bingo are at home with their parents. Bluey asks Chili and Bandit to play with them, but they are busy doing house chores.")
        ans1 = input("Bingo asks Bluey to play with her. What does Bluey say? ")
        print()
        if ans1.lower() == 'yes':
            print("Great, let's play Zoo!")
        elif ans1.lower() == 'no':
            print("Bingo shrugs and goes to play with her plushies.")
            print()
            intro()
        else:
            print("Answer YES or NO. Let's try that again.")
            print()
            intro()
print()
intro()
# So like apparantly "lower.()" makes input easier cuz now I don't have to worry about the case sensitive shit. Yippee
# Also MAKE VARIABLES.. I NEED THEM

def part1():
    global toy
    print("After a quick run to their room, Bingo comes back with a few plushies: a lion, a zebra, a monkey, and a lizard. She offers Bluey to pick the one she wants to play with.")
    print()
    toy = input("Which toy does she pick? ").lower()
    if toy.lower() == 'lion':
        print("Bluey picks up the lion. She roars at Bingo who had picked the zebra and chases after her.")
    elif toy.lower() == 'zebra':
        print("Bluey picks up the zebra and walks around the living room. Bingo, who had picked up the lizard, does the same but at a slower pace.")
    elif toy.lower() == 'monkey':
        print("Bluey picks up the monkey and quickly climbs on the couch, pretending it was a tree. Bingo grabs the lion and roars at her sister.")
    elif toy.lower() == 'lizard':
        print("Bluey picks up the lizard and begins to walk slower (perhaps confusing lizards and turtles). Bingo grabs the monkey and makes funny noises as she climbs on the couch.")
    else:
        print("Bluey can't decide on which toy and tells Bingo she'd rather draw. Bingo shrugs and plays by herself.")
        print()
        intro()
print()
part1()
# Random tip: always make sure that everything is under what it needs to be, for example that "else" statement I keep messing up = MAKE SURE ITS UNDER THE "while True:" otherwise I get the syntax error. I DONT NEED WHILE TRUE HERE, BUT STILL KEEP IT IN MIND
# I only have to add "intro()" under whatever option I want, and it will take the user back to the intro
# AND OK... add "break" after each if statement to avoid the modules to repeat after answering

def part2():
    print(f"After playing for a few minutes. Bluey puts her {toy} plushie down, catching her breath.")
    print("Bluey and Bingo are hungry after all that playing and want to grab something to eat.")
    loca1 = input("Where should they go? ").lower()
    if loca1 == 'kitchen':
        print("The girls walk to the kitchen and find their mum cooking diner.")
    else:
        print("This isn't where they wanted to go. Try again.")
        print()
        part2()
print()
part2()
# not muched learned beside that i can use ChatGPT for clean up when i'm unsure. Also maybe dont use ".lower()" for everything according to it, just use it on the question and leave the options as is.
