'''
This code neatly divides the job into two separate tasks. The first task is to loop over all the
lines and spit out any lines that match a given regular expression. The second task is to
interact with the first task and give it guidance as to what regular expression it is supposed
to be searching for at any given time.

Look at the  match_regex  coroutine first. Remember, it doesn't execute any code when it is
constructed; rather, it just creates a coroutine object. Once constructed, someone outside the
coroutine will eventually call  next()  to start the code running. Then it stores the state of
two variables  filename  and  regex . It then reads all the lines in the file and iterates over
them in reverse. Each line is compared to the regular expression that was passed in until it
finds a match. When the match is found, the coroutine yields the first group from the
regular expression and waits.

At some point in the future, other code will send in a new regular expression to search for.
Note that the coroutine never cares what regular expression it is trying to match; it's just
looping over lines and comparing them to a regular expression. It's somebody else's
responsibility to decide what regular expression to supply.

In this case, that somebody else is the  get_serials  generator. It doesn't care about the
lines in the file; in fact, it isn't even aware of them. The first thing it does is create a
matcher  object from the  match_regex  coroutine constructor, giving it a default regular
expression to search for. It advances the coroutine to its first  yield  and stores the value it
returns. It then goes into a loop that instructs the  matcher  object to search for a bus ID
based on the stored device ID, and then a serial number based on that bus ID.
It idly yields that serial number to the outside  for  loop before instructing the matcher to
find another device ID and repeat the cycle.

Basically, the coroutine's job is to search for the next important line in the file, while the
generator's ( get_serial , which uses the  yield  syntax without assignment) job is to
decide which line is important. The generator has information about this particular
problem, such as what order lines will appear in the file. The coroutine, on the other hand,
could be plugged into any problem that required searching a file for given regular
expressions.
'''

import re

def match_regex(filename, regex):
    with open(filename) as file:
        lines = file.readlines()
    for line in reversed(lines):
        match = re.match(regex, line)
        if match:
            mth = match.groups()[0]
            print(mth)
            regex = yield mth

def get_serials(filename):
    ERROR_RE = "XFS ERROR (\[sd[a-z]\])"
    matcher = match_regex(filename, ERROR_RE)
    device = next(matcher)
    while True:
        try:
            bus = matcher.send(
                "(sd \S+) {}.*".format(re.escape(device))
            )
            serial = matcher.send("{} \(SERIAL=([^)]*)\)".format(bus))
            yield serial
            device = matcher.send(ERROR_RE)
        except StopIteration:
            matcher.close()
            return

for serial_number in get_serials("coroutine.log"):
    print(serial_number)
