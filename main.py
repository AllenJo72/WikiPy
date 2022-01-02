import wikipedia
print("""

░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░   ░░░░░░░░   ░░░░░   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▒   ▒▒▒▒▒▒▒▒   ▒▒  ▒   ▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒   ▒▒▒  ▒▒▒   ▒▒▒▒▒   ▒▒   ▒▒▒▒▒▒▒▒▒  ▒   ▒▒▒   ▒▒▒   
▓   ▓▓   ▓▓▓   ▓   ▓   ▓   ▓▓   ▓▓▓▓▓  ▓▓   ▓▓▓   ▓   ▓
▓   ▓  ▓   ▓   ▓   ▓     ▓▓▓▓   ▓▓▓▓▓  ▓▓▓   ▓▓▓▓    ▓▓
▓  ▓  ▓▓▓▓     ▓   ▓   ▓   ▓▓   ▓▓▓▓▓   ▓   ▓▓▓▓▓▓   ▓▓
█   ████████   █   █   ██   █   █  ██   █████████   ███
█████████████████████████████████████   ████████   ████
Module Used: wikipedia
""")
user_inp = str(input("Search: "))
user_inp2 = int(input("Number of sentences to fetch: "))
try:
    load = wikipedia.summary(user_inp, sentences = user_inp2)
    print(load)
except wikipedia.exceptions.DisambiguationError as e:
    print("*"*20)
    print("Sorry, we could not find what you were searching for, instead try some suggestions given below.")
    print("*"*20)
    print(e.options)
    if wikipedia.exceptions.PageError:
        print("Sorry something went wrong :(")
       
