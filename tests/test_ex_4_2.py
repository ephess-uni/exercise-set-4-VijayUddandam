from textwrap import dedent
import pytest
from datetime import datetime
from src.ex_4_2 import logstamp_to_datetime


@pytest.mark.parametrize(
    'arg',
    [
        '2000-01-01T01:01:01',
        '2001-02-03T04:05:06',
    ]
)
def test___logstamp_to_datetime___returns_datetime_type(arg, feedback):
    md = dedent(
        """
        # Feedback
        This function passes multiple timestamps to your function and checks to make
        sure that your function returns a datetime type. 
        
        If this test is failing, make sure that your function is correctly returning
        a datetime type.
        """
    )
    feedback(md)
    assert isinstance(logstamp_to_datetime(arg), datetime)


@pytest.mark.parametrize(
    'arg,expected',
    [
        ('2000-01-01T01:01:01', 'datetime(2000, 1, 1, 1, 1, 1)'),
        ('2001-02-03T04:05:06', 'datetime(2001, 2, 3, 4, 5, 6)'),
    ]
)
def test___logstamp_to_datetime___returns_correct_datetime_object(arg, expected, feedback):
    md = dedent(
        """
        # Feedback
        If your function is failing this test, consult the datetime.strptime examples found
        at https://docs.python.org/3/library/datetime.html#examples-of-usage-datetime.
        
        Make sure that your function returns a datetime(2000, 1, 1, 1, 1, 1) for '2000-01-01T01:01:01'.
        """
    )
    feedback(md)
    assert logstamp_to_datetime(arg) == eval(expected)
