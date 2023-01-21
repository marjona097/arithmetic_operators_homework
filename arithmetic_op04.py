#Create a variable called 'number' and assign it the three-digit number.
raqam=111
#Find the 'number' first digit and assign to x1.
x1=raqam//100
#Find the 'number' second digit and assign to x2.
x2=raqam%100
x3=raqam%10
x4=x2//10
#Find the 'number' third digit and assign to x3.

#Create a variable called 'answer' and assign it the sum of the three digits x1, x2, x3.
javob=x1+x4+x3
#Print the value of the 'answer.
print(javob)