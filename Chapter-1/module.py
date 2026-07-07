"""A module is a file containing code written by somebody else (usually) which can be 
imported and used in our programs."""

import pyjokes

# This prints a jokes
jokes = pyjokes.get_joke()
print(jokes)