from Question import Question

question_prompts = [
   "Är Szymon idiot?\n(a) Fet jevla ja\n(b) Nej verkligen inte\n(c) Typ\n\n",
    "Är Szymon sämst?\n(a) Nej han är kung!\n(b) Ja lite asså\n(c) Kingeling\n\n",
    "Är Szymon kelb?\n(a) Ja som fan!\n(b) Nej han är människa!\n(c) Vad är kelb?\n\n",
    "Är Love kelb?\n(a) Ja som fan!\n(b) Nej han är människa!\n(c) Vem är Love?\n\n",
    "Rasmus är bäst\n(a) Ja som fan!\n(b) Ja!\n(c) Han är alltid bäst!\n\n",

]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "c"),
    Question(question_prompts[4], "a"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("Du fick jevligt " + str(score) + "/" + str(len(questions)) + " rätt")

run_test(questions)



