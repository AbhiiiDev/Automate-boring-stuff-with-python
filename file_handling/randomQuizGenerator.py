import random

capitals={'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona':
'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado':
'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida':
'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia':'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quiz_num in range(10):
    # to-do: Create quiz and answer key files.
    quiz_file=open(f'Quiz/capitalsQuiz{quiz_num+1}.txt','w',encoding='UTF-8')
    answer_file=open(f'Quiz/capitalsquiz_answers{quiz_num+1}.txt','w',encoding='UTF-8')

    # to-do: Write out the header of the quiz.
    quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quiz_file.write((' ' * 20) + f'State Capitals Quiz (Form{quiz_num + 1})')
    quiz_file.write('\n\n')


    # to-do: Shuffle the order of state.
    states=list(capitals.keys())
    random.shuffle(states)


    # to-do: Loop through all states and make question for each
    for num in range(50):
        correct_a=capitals[states[num]]
        wrong_a=list(capitals.values())
        del wrong_a[wrong_a.index(correct_a)]   
        wrong_a=random.sample(wrong_a,3)  
        answer_opt=wrong_a+[correct_a] 
        random.shuffle(answer_opt)
    
        # Write the question and the answer options to the quiz file.
        quiz_file.write(f'{num + 1}. Capital of {states[num]}:\n')
        for i in range(4):
          quiz_file.write(f"    {'ABCD'[i]}. {answer_opt[i]}\n") 
        quiz_file.write('\n')

        answer_file.write(f"{num + 1}.{'ABCD'[answer_opt.index(correct_a)]}")
    quiz_file.close()
    answer_file.close()




