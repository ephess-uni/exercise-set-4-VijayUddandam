import pytest
from src.ex_4_0 import get_shutdown_events
from textwrap import dedent


@pytest.mark.parametrize(
    'logfile',
    [
        'default_messages',
        'test_messages',
    ]
)
def test___get_shutdown_events___returns_list(logfile,feedback, request):
    md = dedent("""
    # Feedback
    Assure that get_shutdown_events() returns a *list* type.
    """
    )
    feedback(md)

    assert isinstance(get_shutdown_events(request.getfixturevalue(logfile)), list)


@pytest.mark.parametrize(
    'logfile,expected_length',
    [
        ('default_messages', 2),
        ('test_messages', 4),
    ]
)
def test___get_shutdown_events___returns_correct_number_of_lines(logfile, expected_length, feedback, request):
    md = dedent(
        """
        # Feedback
        get_shutdown_events should only collect log events where shutdowns were initiated.
        
        This tests the number of events returned by your function.  For the default logfile, 
        this should be 2.
        """
    )
    feedback(md)
    assert len(get_shutdown_events(request.getfixturevalue(logfile))) == expected_length


@pytest.mark.parametrize(
    'logfile',
    [
        'default_messages',
        'test_messages',
    ]
)
def test___get_shutdown_events___collects_only_shutdown_initiated(logfile, feedback, request):
    md = dedent(
        """
        # Feedback
        get_shutdown_events should only collect log events where shutdowns were initiated.

        This tests the content of each list and asserts that *Shutdown initiated* is present.
        """
    )
    feedback(md)
    actual = get_shutdown_events(request.getfixturevalue(logfile))
    assert all(['Shutdown initiated'.lower() in s.lower() for s in actual])