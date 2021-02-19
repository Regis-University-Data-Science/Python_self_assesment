import os
import contextlib
from inspect import isfunction
from io import StringIO

def calculate_score(variables):
    """
    Takes a dictionary of variables, most easily obtained with globals().
    Checks answers to questions from variable values.
    Prints out percent correct and if the student passed.
    Also prints out which questions were right and wrong.
    """
    correct = 0
    correct_qs = []
    incorrect_qs = []
    incorrect_explanations = []
    incorrect_template = 'The correct answer was:\n{}\nbut your answer was:\n{}'
    questions = ['Question 1 - Simple Math',
    'Question 2 - Math and strings',
    'Question 3 - Variables',
    'Question 4 - Lists',
    'Question 5 - Lists part 2',
    'Question 6 - Lists part 3',
    'Question 7 - Lists part 4',
    'Question 8 - Dictionaries',
    'Question 9 - Dictionaries part 2',
    'Question 10 - Functions',
    'Question 11 - for loops',
    'Question 12 - while loops',
    'Question 13 - if statements',
    'Question 14 - Classes',
    'Question 15 - Packages and modules'
    ]
    correct_answers = [23,
        'The number of people per US state on average is 8000000',
        11.35,
        [2.1, 3.2, 7.7, 0],
        3.2,
        4,
        [5, 11, 23, 17],
        {'Denver': 2.1, 'Boulder': 3.2, 'Nederland': 7.7, 'Phoenix': 0},
        3.2,
        7.7,
        '2.1\n3.2\n7.7\n0\n',
        10,
        'Boulder: 3.2\nNederland: 7.7\nPhoenix: No snow!\n',
        [10000, 9616.276584519474],
        os.getcwd()
        ]
    
    # correct answers for list and dict for running functions
    snowfall_list = [2.1, 3.2, 7.7, 0]
    snowfall_dict = {'Denver': 2.1, 'Boulder': 3.2, 'Nederland': 7.7, 'Phoenix': 0}
    student_answers = []
    var_strings = ['ans_1',
                'ans_2',
                'total_snowfall',
                'snowfall_list',
                'boulder',
                'num_cities',
                'sun_index',
                'snowfall_dictionary',
                'boulder_snowfall',
                'get_biggest_snowfall',
                'loop_thru_snowfall',
                'counter',
                'print_snowfall',
                'new_mortgage',
                'cwd'
                ]
    for var_str in var_strings:
        try:
            current_var = variables[var_str]
            if isfunction(current_var):
                if var_str == 'get_biggest_snowfall':
                    student_answers.append(current_var(snowfall_list))
                    continue
                
                stream = StringIO()
                write_to_stream = contextlib.redirect_stdout(stream)
                if var_str == 'print_snowfall':
                    with write_to_stream:
                        current_var(snowfall_dict)
                else:
                    with write_to_stream:
                        current_var(snowfall_list)
                
                student_answers.append(stream.getvalue())
            elif var_str == 'new_mortgage':
                student_answers.append(current_var.outstanding)
            else:
                student_answers.append(current_var)
        except KeyError:
            student_answers.append(None)

    for q in range(15):
        try:
            ans = correct_answers[q]
            student_ans = student_answers[q]
            if student_ans is None:
                incorrect_qs.append(questions[q])
                incorrect_explanations.append('Your answer was missing.')
                continue

            assert student_ans == ans
            correct_qs.append(questions[q])
            correct += 1
        except AssertionError:
            incorrect_qs.append(questions[q])
            incorrect_explanations.append(incorrect_template.format(ans, student_ans))

    if correct == 15:
        print('Great work! You aced it. You should be good to go for MSDS600.')
    else:
        pct_correct = int(correct/15 * 100)
        print(f'You got {correct} out of 15 questions right for {pct_correct}% correct.')
        if pct_correct >= 70:
            print('You should be good to go for MSDS600, but be sure to compare your answers with the solutions.')

        print('\nQuestions you got correct:')
        for q in correct_qs:
            print(q)
        print('\nQuestions you missed:')
        for q, exp in zip(incorrect_qs, incorrect_explanations):
            print(q)
            print(exp)