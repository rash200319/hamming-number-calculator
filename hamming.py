user_input=input("Enter your number range(example:1 6): ") #getting user input(with instructions)
def if_hamming(number):                  #a function to check wheather a number is hamming or not.
    dup_num=number              #making a duplicate of the number 
    while number%2==0:          #checking if the number can be devided by two and do it until mod is not zero
        number=number//2
    while number%3==0:          #checking if the number can be devided by three and do it until mod is not zero
        number=number//3
    while number%5==0:          #checking if the number can be devided by five and do it until mod is not zero
        number=number//5 
    if number==1:               #after deviding if the number=1 returning true
        return True 
    else:
        return False

try:
    first_num,second_num=user_input.split() #splitting input by space
    f_num=int(first_num)              #converting str to int
    s_num=int(second_num)
    if f_num> s_num:
        print("The range is invalid.first number should be less than the second.")  #if first number is more than 2nd printing error message
    else:
        sums=0
        for i in range(f_num,s_num+1):   #calculating the sum of hamming numbers
            if if_hamming(i):
                sums+=i
        print("Sum of the hamming numbers: ",sums) #printing the output
except ValueError:
    print("Input the range seperated by a space and ensure both are integers.") #if input is not following the format printing the error message

    
