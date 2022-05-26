orgtxt=input("Things with punctuation in it: ")
lctxt=orgtxt.lower()
#I am taking the word and converting it to a lower case

lctxt=lctxt.replace ("."," ")
lctxt=lctxt.replace (","," ")
lctxt=lctxt.replace ("%"," ")
lctxt=lctxt.replace ("!"," ")
lctxt=lctxt.replace ("£"," ")
lctxt=lctxt.replace ("@"," ")
lctxt=lctxt.replace (":"," ")
lctxt=lctxt.replace (";"," ")
lctxt=lctxt.replace ("?"," ")
#lctxt=lctxt.replace (""," ")
lctxt=lctxt.replace ("",' ')
#This will remove punctuation

unsortedarray = lctxt.split()
unsortedset = set(unsortedarray)
# By converting to an set it will remove the doubles
sortedlist=list(unsortedset)


print (sortedlist)
for i,keyword in enumerate (sortedlist):
	print (i+1 ,keyword)

#This will make a list of the numbers and the words
print ("Output words")
output=""
for i,keyword in enumerate(unsortedarray):
        output=output +" "+ str(1+sortedlist.index(keyword))
print (output)

