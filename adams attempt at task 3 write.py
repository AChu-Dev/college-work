file_words=open("output_words.txt","r")
words_list=file_words.readlines()
file_words.close()
#this will read the file as a list and allows me to check

for wordnumber in range(len(words_list)):
    words_list[wordnumber]=words_list[wordnumber].strip()
#This will read the list and find out the amount of numbers
#range makes the len the entire list

print(words_list)

file_id=open("output_numbers.txt")
output_numbers=file_id.read()
file_id.close()
#as its a string you do not use readlines
#by making it a variable it does not need to be open

numbers_array=output_numbers.split()
print(numbers_array)
#This will make the string into an array meaning all the numbers
#are different

sentence=""
for i in numbers_array:
    index=int(i)-1
    sentence=sentence + words_list[index] + " "
print (sentence)
#this makes the sentence a string and changes the way the anwer looks to be more
#aestetically pleasing
#the reason why the int(i) has to be -1 as prior to this we to the enumuerate
#value and added 1 to it to stop it from thinking that 0 is the position of the
#first word.
