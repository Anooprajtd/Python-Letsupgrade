inp = eval(input("Enter the limit"))
count=0

while inp != 0:
    count+=inp
    print(inp)
    inp=inp-1
    
print (f"\nTotal number count {count}")


inp = eval(input("Enter a number to check if its prime number or not :"))
if inp > 1:  
   for i in range(2, inp//2): 
       if (inp % i) == 0: 
           print(inp, "is not a prime number") 
           break
   else: 
       print(inp, "is a prime number") 
  
else: 
   print(inp, "is not a prime number") 
            
