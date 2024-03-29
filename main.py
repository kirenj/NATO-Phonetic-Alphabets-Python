import pandas

data = pandas.read_csv("./nato_phonetic_alphabet.csv")

phone_dictionary = {row["letter"]:row["code"] for (index, row) in data.iterrows()}

def func():
  user_input = input("Enter a word: ").upper()
  user_word_list = [i for i in user_input]
  
  try:   
    final_list = [phone_dictionary[i] for i in user_word_list]      
  except KeyError:
    print("Enter a valid word")
    func()
  else:
    print(final_list)
        
func()


# for (index,row) in data.iterrows():
#     key = row["letter"]
#     value = row["code"]
#     letters[key] = value