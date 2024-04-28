## Introduction
This exercise set focuses on the use of `datetime` module functions and a review of 
previous course topics such as file reading and string operations. Many of the 
exercises here will operate on the messages.log file which is included in the `data` 
directory of your repository.

## Caution
The template code included in this repository contains a number of imports that are 
required in order for your code to run and for tests to run within GitHub classroom. 
**Do NOT remove any of these required imports as it will cause problems.**  If you 
run into an issue where imports are not working for you, contact your instructor 
as soon as possible.

The `FILENAME` variables present in the template must also be preserved.  This is 
pre-defined for you to avoid any confusion about what the path should be during your 
test runs and the classroom grading tests. **Leave code defining the `FILENAME` 
variable as-is.**

## ex_4_0.py
In this exercise you will work with the `messages.log` file located in the `data` 
directory of your repository. In the module`src/ex_4_0.py`, complete the function stub `get_shutdown_events(logfile)`. The 
function should return log entries where shutdowns were initiated. Here's an example of the lines of interest.  Note that other log entries are also included in the file.

Here is an example snippet from `message.log`. Note that the log entries are 
timestamped.  The earliest timestamp is at the beginning of the file and the latest is 
at the end of the file.

```
INFO 2014-07-03T23:27:51 supybot Shutdown initiated.
INFO 2014-07-03T23:27:51 supybot Killing Driver objects.
...
INFO 2014-07-03T23:31:22 supybot Total CPU time taken: 1.12 seconds.
INFO 2014-07-03T23:31:22 supybot No more Irc objects, exiting.
...
INFO 2014-07-03T23:31:22 supybot Shutdown initiated.
```

Your `get_shutdown_events()` function should implement the following:

- open the filename argument `logfile`.
- read in all lines from the file, keeping only those a shutdown was initiated.
- returns a list of lines where a shutdown was initiated.
- If no shutdown lines are found in the list, your function should return an empty 
  list.

## ex_4_1.py
In a module called `ex_4_1.py` create a function called `num_shutdowns(logfile)` that uses your function from `ex_4_0.py` to count and return the number of shutdowns present in the file with name `logfile`.

Your function should *return* the integer count of shutdowns present in the file.  *Note: a single shutdown event will have two entries: "Shutdown initiated" and "Shutdown complete"*

## ex_4_2.py
In a module called `ex_4_2.py` create a function called `logstamp_to_datetime(datestr)` that takes in an input date string of the following format (note that date fields are largest to smallest).

```
2014-07-03T23:31:22
```

Here:
- 2014 is the year
- 07 is the month
- 03 is the day
- 23 is the hour
- 31 is the minute
- 22 is the second

Your function should parse the `datestr` argument and return a `datetime.datetime` object.

## ex_4_3.py
Write a function `time_between_shutdowns(logfile)` that takes in a filename for a log file such as `messages.log` and returns the amount of time between the *first* and *last* shutdowns as a `datetime.timedelta` object.

Your function should:

- pass the `logfile` argument to `get_shutdown_events()` from `ex_4_1.py` to get the shutdown entries.
- for the first and last shutdown entries, convert the date field to a `datetime.datetime` object using `logstamp_to_datetime()` from `ex_4_2.py`.
- Compute the difference in time between the two events using the appropriate order (the value should be positive).
- return the resulting `datetime.timedelta` object.
