#a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.


user_first_input = str(input("Enter first string : "))
user_second_input = str(input("Enter second string : "))

first_input_list = []
second_input_list = []

for letter in user_first_input:
    first_input_list.append(letter)

for letter in user_second_input:
    second_input_list.append(letter)

first_input_list.sort()
second_input_list.sort()

if first_input_list == second_input_list:
    print("They are an example of an ANAGRAM")

else:
    print('They are not ANAGRAMS')