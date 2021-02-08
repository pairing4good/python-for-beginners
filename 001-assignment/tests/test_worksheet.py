import pytest
from helper.worksheet_helper import *

question_answer = read_parameterized_question_answer('001')
test_ids = create_ids(len(question_answer))


@pytest.mark.parametrize("question,answer", question_answer, ids=test_ids)
def test_worksheet(question, answer):
    assert question == answer, TEST_MESSAGE
