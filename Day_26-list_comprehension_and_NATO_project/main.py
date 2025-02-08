import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

df = pandas.DataFrame(data)



df_dict = {row.letter: row.code for (index, row) in df.iterrows()}

word = list(input("Enter a word: ").upper())

nato_list = [df_dict[x] for x in word]

print(nato_list)
