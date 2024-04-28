from datetime import timedelta
from textwrap import dedent
import pytest
from src.ex_4_3 import time_between_shutdowns


@pytest.mark.parametrize(
    'logfile',
    [
        'default_messages',
        'test_messages',
    ]
)
def test___time_between_shutdowns___returns_timedelta_type(logfile, feedback, request):
    md = dedent(
        """
        # Feedback
        Make sure that your function returns a datetime.timedelta object.
        """
    )
    feedback(md)
    assert isinstance(time_between_shutdowns(request.getfixturevalue(logfile)), timedelta)


@pytest.mark.parametrize(
    'logfile,expected',
    [
        ('default_messages', 'timedelta(seconds=211)'),
        ('test_messages', 'timedelta(days=1, seconds=211)'),
    ]
)
def test___time_between_shutdowns___returns_correct_timedelta(logfile, expected, feedback, request):
    md = dedent(
        """
        # Feedback
        Make sure that the value of the timedelta object is correct.  For the default logfile, 
        this is 211 seconds.  
        
        Keep in mind that your function is tested with different inputs. 
        """
    )
    feedback(md)
    assert time_between_shutdowns(request.getfixturevalue(logfile)) == eval(expected)
