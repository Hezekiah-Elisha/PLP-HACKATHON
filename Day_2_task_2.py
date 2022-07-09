#!/usr/bin/python3
import random

advices = [
    'Find out what you like doing best, and get someone to pay you for doing it.” – Katharine Whitehorn',
    'If opportunity doesn’t knock, build a door.” – Milton Berle',
    'The future depends on what you do today.” – Mahatma Gandhi',
    'Opportunities don’t happen, you create them.” – Chris Grosser',
    'The only way to do great work is to love what you do. If you haven’t found it yet, keep looking. Don’t settle.” – Steve Jobs',
    'Whatever you decide to do, make sure it makes you happy.” – Paulo Coelho',
    'If you’re offered a seat on a rocket ship, don’t ask what seat! Just get on.” – Sheryl Sandberg',
    'A mind that is stretched by new experiences can never go back to its old dimensions.” – Oliver Wendell Holmes, JR.',
    'When the grass looks greener on the other side of the fence, it may be that they take better care of it there.” – Cecil Selig',
    'Luck is what happens when preparation meets opportunity.” – Seneca']
careers = [
    "doctor", "lawyer",
    "teacher", "carpenter",
    "veterinary", "electrician",
    "cashier", "hairstylist",
    "analyst", "softaware engineer"
]
questions = [
    'Is treating people your passion?',
    'Is criminal justice your pride?',
    'Is teaching kids your pride?',
    'Does creative wood work excite you?',
    'Is working with animals your interest?',
    'Do you find pride in working with electricity and in appreciating the power of science?',
    'Does working with money, balancing business sheets seem like an area you would like to handle?',
    'Do you enjoy working with hair models and hair creatives?',
    'Are you fascinated with data collection, analysis and presentation?',
    'Does creation of computer programs make you feel thrilled?']


def career_choices():
    for index, career in enumerate(careers):
        print(f"{index}: {career}")


def career_advice():
    return random.choices(advices)


def career_questions():
    for index, question in enumerate(questions):
        print(index + 1, question)
        answer_string = input(' -> ')
        if answer_string == 'yes' or answer_string == 'no':
            if answer_string == 'yes':
                return careers[index]
        else:
            print('Question passed, Kindly Answer yes or no!')
    return 'Please retake the Test'


def program():
    print("********Welcome to the Career chooser*******\n")
    print('****The following are career options available: ')
    career_choices()
    print('****Kindly and with yes or no')
    print(f'Remember: \n{career_advice()}')
    career = career_questions()
    retake_answer = int(
        input('Retake test? Choose 1 or 2\n1. Yes\n2. No\n-->'))
    if retake_answer == 1 or retake_answer == 2:
        if retake_answer == 2:
            if career == 'Please retake the Test':
                print(career)
            else:
                print(
                    f'Congratulations! You can pursue a career as a {career}')
        else:
            career = career_questions()
            if career == 'Please retake the Test':
                print(career)
            else:
                print(
                    f'Congratulations! You can pursue a career as a {career}')

    else:
        print('You did not enter a valid choice')
    print("Thank you\nBye")


if __name__ == '__main__':
    program()
