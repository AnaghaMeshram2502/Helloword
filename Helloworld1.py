#question: answer
quesans={
    "Hi":"Hello",
    "What is your name":"Minu",
    "What is your age":"25 years",
    "Where do you live":"Amravati",
    "Which company do you work for":"Minzor",
    "What is your short term goal":"Getting placed in an IT company",
    "Whom do you admire the most":"My mother",
    "Which Hollywood actor do you love":"Robert Pattinson",
    "What do you do in your passtime":"Read and make Zentangles",
    "Which book are you reading currently":"Mindset by Dr. Carol Dweck"
       }

while True:
    qsn = input()
    
    if(qsn == "Quit"):
        break
        
    else:
        print(quesans[qsn])