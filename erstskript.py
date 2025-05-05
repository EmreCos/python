name = "emre"
print(name)
zahl1 = 1.4 # das ist zahl 1
zahl2 = 2.3 # das ist zahl 2
zahlergebnis = zahl1 + zahl2 
print(zahlergebnis)
alter= int (input("gib das alter ein"))
# das ist ein if statment was das alter überprüft 
if alter<18:
  print("du bist zu jung")

a=3        
        
elif alter>=18:
  print ("dein alter passt")
else:
  print ("kein alter")           
for i in range(1,6):
  print(i)
fruechte=["bannane","apfel","erdbeer","Kiwi","Bierne", "bannane","apfel","erdbeer","Kiwi","Bierne"] 
print(fruechte[0]) 


for frucht in fruechte:
  print("-"+frucht+"-")
for i in range(0,11, 2):
  print(i) 
x=30  
for frucht in fruechte:
  if frucht=="erdbeer":
      continue
  else:
      print( frucht)

i=0;

while len(fruechte)<=i:
  print(fruechte[i])  
  i+=1      

enter = input("gib etwas ein")
print (enter)                      
