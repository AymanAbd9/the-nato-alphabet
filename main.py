from unittest import result
import pandas

phonetic_df = pandas.read_csv('./nato_phonetic_alphabet.csv')
# print(phonetic_df)

phonetic_dict = {row['letter']:row['code'] for (index, row) in phonetic_df.iterrows()}
# print(phonetic_dict)

word = input('Enter a word: ').upper()
result = [phonetic_dict[letter] for letter in word]

print(result)