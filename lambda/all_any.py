given_list = [20,10,4,5,6,7]
#all
print(all(i for i in given_list if i%2==0))  #i have a question
print(all(i%2==0 for i in given_list ))
#any
print(any(i%2==0 for i in given_list )) #all are truthy except empty
print(any(i%2==2 for i in given_list ))