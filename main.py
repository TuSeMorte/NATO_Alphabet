import pandas
data = pandas.read_csv('nato_phonetic_alphabet.csv')
#TODO 1. Create a dictionary in this format:
nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input('Enter a word: ').upper()
result = [nato_dict[letter] for letter in user_input if letter in nato_dict.keys() ]
print(result)