# to open the file....by default read (r) is here
f=open('requirment.txt','r')
read=f.read()
print(read)
f.close()


#  to add more info in file
f=open('requirment1.txt','a')
append=f.write('\nsonusoiamr')
print(append)
f.close()

# when file doesn't exist 
# so python automatically create the name of file