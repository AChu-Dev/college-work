originaltext= input("Any object that comes up twice")
originaltextlc = originaltext.lower()

#Remove punctuation
puncttext=originaltextlc.replace("."," ")

#Make the set unique
words=puncttext.split()
uniquewordsset=set(words)
uniquewords=list(uniquewordsset)

print ("The unique words are:")
#Report words
for i,thisword in enumerate(uniquewords):
   print (i+1, thisword)

print("")
#Produce the index values as a string
print("The word numbers are:")
output=""
for i,thisword in enumerate(words):
    #have each word in the input
	output=output + str(1+uniquewords.index(thisword)) + " "

print (output)

