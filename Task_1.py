#List and its operations

List1 = [10,20,30,40,50]

#adding element at end of the list using (Append)
List1.append(60)

#adding element at specific position using (insert)
List1.insert(2,25)

#Removing element using element
List1.remove(50)

#removing element using index number
List1.pop(4)

#Change the value using index number
List1[1] = 22

print("Updated list:",List1)


#2.Set

Set1 = {10,20,30,40,50}

#Adding element using (add)
Set1.add(60)

#Removing element using element value
#note: in this remove if element is not in the set it may raise ERROR
Set1.remove(20)

#Removing element using discard
#Note: if element in the set it remove the element if not in the set it does nothing
Set1.discard(100)

print("Updated Set:",Set1)


#Dictionary

Dict1 = {1:"One",2:"Two",3:"Three",4:"Four"}

#Adding
Dict1[5] = "Five"
Dict1.update({5:"Five"})

#Remove
Dict1.pop(4)

#update
Dict1[2] = "Twoo"
Dict1.update({3:"Treee"})

print("Updated dictionary:",Dict1)






