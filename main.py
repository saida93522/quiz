from Question import Question

question_prompts = [
    'what color are Apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n',
    'what color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n',
    'what color are Strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n'
]
questions = [
    Question(question_prompts[0], 'a'),
    Question(question_prompts[1], 'c'),
    Question(question_prompts[2], 'b'),
]


def run_test(question_list):
    score = 0  # keep track of user score
    for question in question_list:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(f'You got {str(score)}/{str(len(question_list))} correct!')


run_test(questions)
