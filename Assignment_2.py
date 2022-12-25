'''1. What are the two values of the Boolean data type? How do you write them?
=> The two values of Boolean type is True and False.
    always write them as True = (t in capital letter rest in small letter),
    False = (f in capital letter rest in small letter)
    
2. What are the three different types of Boolean operators?
=> 1. AND = If both argument are True then only result is True.
   2. OR = If any argument is True then result is True.
   3  NOT = If complement reverse - not True = False, not False = True.

3. Make a list of each Boolean operator&#39;s truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).
=> 1. AND  =>   True AND True = True
                True AND False = False
                False AND True = False
                False AND False = False
   
   2. OR  =>    True OR True = True
                True OR False = True
                False OR True = True
                False OR False = False
                
   3.NOT =>    NOT True = False
               NOT False = True


4. What are the values of the following expressions?
=>  (5>4) and (3==5) = False
    
    not (5>4) = False
   
   (5>4) or (3==5) = True
   
    not ((5>4) or (3==5)) = False
    
    (True and True) and (True == False) = False
    
    (not False) or (not True) = True
    
    
5. What are the six comparison operators?
=> <  Less than           ex- 10<20
   >  Greater than          ex- 20>10
   <= Less than or Equal      ex- 10<=20
   >= Greater than or Equal   ex -> 20>=10
   == Equality operators        ex -> l,m=10,10 -> l==m 
   !=  Non-Equality operator    ex -> l,m=10,20 -> l!=m
   
   
6. How do you tell the difference between the equal to and assignment operators?Describe a cgondition and when you would use one.   
=> we use assigment opeerators to assign a variable(=). ex-> x=10
   But Equality operator use to check the object has same content or not. ex -> l,m=10,10 -> l==m 
    

7. Identify the three blocks in this code:
   spam = 0
   if spam == 10:
   print(eggs')
   if spam>5:
   print(bacon') 
   else:
   print('ham')
   print('spam')
   print('spam') 
    
==> 1st block--> if spam == 10:
                      print(eggs')        
   2nd block --> if spam>5:
                      print(bacon')
     
   3rd block -->  else:
                      print('ham')
                      print('spam')
                      print('spam') 
					  
					  '''
    
#8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

spam = int(input("Enter any value: "))
if spam==1:
	print("Hello")
elif spam==2:
	print("Howdy")
else:
	print("Greetings!")

'''
#9.If your programme is stuck in an endless loop, what keys you’ll press?
==> # ctrl + c

10. How can you tell the difference between break and continue?
==>  The difference between both the statements is that when break keyword comes,it terminates the execution of the current loop 
     But when continue keyword is comes,it skips the current iteration and executes the very next iteration in the loop.


11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?      
==>  range(n) = 0 to n-1
     range(m,n) = m to n-1
	 range(m,n,increment/decrement) = m to n-1 with increment or decrement
     here range(10) , range(0,10) and range(0,10,1) gives same value from 0 to 9.
	 '''
	 
 #12.Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
 #        program that prints the numbers 1 to 10 using a while loop.  
		 
# ==> FOR LOOP
for x in range(1,11):
	print(x)

# ==> WHILE LOOP
n = 1
while n<=10:
	print(n)
	n=n+1

'''
13. If you had a function named bacon() inside a module named spam, how would you call it after
importing spam?

==> spam.bacon()

'''







   
	   
   