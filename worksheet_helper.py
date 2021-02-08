import os

TEST_MESSAGE = 'Please fill in each blank with answers provided in your lesson.'


def read_parameterized_question_answer(number):
    questions = read(number, 'worksheet')
    answers = read(number, 'answers')
    assert len(questions) == len(answers)

    parameter_pairs = []

    for question, answer in zip(questions, answers):
        parameter_pairs.append((question.lower(), answer.lower()))

    return parameter_pairs


def read(number, file_name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + '/' + number + "-assignment/tests/resources/" + file_name + '.txt', 'r') as file:
        worksheet = file.read()
    return worksheet.splitlines()


def create_ids(count):
    ids = []
    for number in range(count):
        ids.append("question_" + str(number + 1))

    return ids
