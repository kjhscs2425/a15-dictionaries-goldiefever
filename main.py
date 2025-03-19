import string
text = """
Everyone counts.
Everyone has access to great learning.
Every person's unique talents are valued equally.
Everyone takes responsibility for themselves and their community.
"""

# Make a dictionary where the keys are characters and the values are the number of times that character appears in the `text` print the dicitonary

character_values = {}

for letter in text:
    if not letter in string.ascii_letters:
        pass
    elif letter.lower() in character_values:
        character_values[letter.lower()] += 1
    else:
        character_values[letter.lower()] = 1

print(character_values)