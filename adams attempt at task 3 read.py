sentence=input("Please write the paragraph that you would like to be zipped.\n")
#inputs a sentence

unsortedarray = sentence.split()
unsortedset = set(unsortedarray)
sortedlist=list(unsortedset)
#Allows you to index the list

file_words=open("output_words.txt","w")
print ("output words")
#This means I do not have to open it later

for i,keyword in enumerate (sortedlist):
    print (i+1 , keyword)
    file_words.write(keyword)
    file_words.write("\n")
file_words.close()
#this is creating a new file which is a string with all
#of the words are seperated by a new line

output=""
for i,keyword in enumerate(unsortedarray):
    output=output+" "+str(1+sortedlist.index(keyword))

file_id=open("output_numbers.txt", "w")
file_id.write(output)
file_id.close()
#this is writing the output numbers to the file
