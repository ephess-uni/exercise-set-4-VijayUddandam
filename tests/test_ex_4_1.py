import pytest
from src.ex_4_1 import num_shutdowns
from textwrap import dedent


@pytest.mark.parametrize(
    'logfile,expected_length',
    [
        ('default_messages', 2),
        ('test_messages', 4),
    ]
)
def test___num_shutdowns___returns_correct_number_of_lines(logfile, expected_length, feedback, request):
    md = dedent(
        """
        # Feedback
        This tests checks to see if your function returns the correct number of shutdowns. For the 
        default log file, this should be 2. This test does pass a separate log file to your function
        as a secondary test however. 
        """
    )
    feedback(md)
    assert num_shutdowns(request.getfixturevalue(logfile)) == expected_length
