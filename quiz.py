from time import sleep


class query:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

#Här är frågor i en list
query_prompt = [
    "What is the name of the founder of Python?\n(1) Leonardo Davinci\n(2) Max\n(3) Guido Van Rossum\n> ",
    "What year was Python made?\n(1) 1987\n(2) 1991\n(3) 2004\n> ",
    "What happens if you type 'import this' into Python Idle?\n(1) A poem is printed\n(2) Nothing happens\n(3) You get an error message\n> ",
    "What is the origin behind the name Python?\n(1) It is the creators favorite animal\n(2) The comedy group Monty Python\n(3) No reason, creator thought it sounded cool\n> ",
    "What happens if you type 'import antigravity' into Python Idle?\n(1) Your computer loses gravity\n(2) A webcomic is opened\n(3) Nothing happens\n> ",
    "If you type 'Hello' 'World' '!' how will Python print it?\n(1) Hello World !\n(2) Hello_World_!\n(3) HelloWorld!\n> ",
    "What language processor does Python use?\n(1) Compiler\n(2) Interpreter\n(3) Assembler\n> ",
    "What Programming language level is Python?\n(1) Low level\n(2) Medium level\n(3) High level\n> ",
    "What is the most recent stable version of Python?\n(1) 1.5\n(2) 3.10\n(3) 2.8\n> ",
    "What is pip used for?\n(1) Compile\n(2) Find bugs\n(3) Install packages\n> "
]

#Ange vilket svar som är rätt till alla frågor
queries = [
    query(query_prompt[0], 3),
    query(query_prompt[1], 2),
    query(query_prompt[2], 1),
    query(query_prompt[3], 2),
    query(query_prompt[4], 2),
    query(query_prompt[5], 3),
    query(query_prompt[6], 2),
    query(query_prompt[7], 3),
    query(query_prompt[8], 2),
    query(query_prompt[9], 3), 
]

#Kollar om man har svarat rätt
def run_test(queries):
    score = 0
    for query in queries:
        while True:
            try:
                answer = int(input(query.prompt))
            except ValueError:
                print("Please enter 1, 2 or 3")
                sleep(0.5)
                continue
            if answer < 1 or answer > 3:
                print("Please enter 1, 2 or 3")
                sleep(0.5)
                continue
            elif answer == query.answer:
                print("Correct")
                score += 1
            else:
                print("Wrong")
            sleep(0.5)
            break
        
    print("You got " + str(score) + " out of " + str(len(queries)) + (" answers right."))

run_test(queries)