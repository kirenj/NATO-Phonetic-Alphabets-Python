import pandas

data = pandas.read_csv("./nato_phonetic_alphabet.csv")

user_input = input("Enter a word: ").upper()
user_word_list = [i for i in user_input]
phone_dictionary = {row["letter"]:row["code"] for (index, row) in data.iterrows()}

# for (index,row) in data.iterrows():
#     key = row["letter"]
#     value = row["code"]
#     letters[key] = value

final_list = [phone_dictionary[i] for i in user_word_list for j in phone_dictionary if i == j]
print(final_list)