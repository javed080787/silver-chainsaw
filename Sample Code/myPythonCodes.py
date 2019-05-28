
########## Suggestions

variables - snake case or lower case with underscore
functions - snake case or lower case with underscore
Class - Camel case with first letter alwaya caps
Object - all small letters


###########################################################


## find length of a string
def length_of_string(strng): 
    
    ctr=0
    
    for _ in strng:
        ctr += 1
    return ctr
	
## count characters and push into dict		
def count_chars(strng):
    
    ctr=0
    result={} # Empty dict
    
    for chars in strng:
        result[chars]=strng.count(chars)
    return result
	

##Count words and push into a dict
def count_words(strng):
    list1=strng.split(' ')
    result ={}
    for i in list1:
        result[i]=list1.count(i)
    return(result)
	
	

## replace each next char to $
strng='restart'
first_char=strng[0]
strng_out=strng.replace(first_char,'$')
strng_out=first_char+strng_out[1:]


## Check a string and replace it
def check_strng(strng):
    snot=strng.find('not')
    spoor=strng.find('poor')
    
    if snot<spoor and snot>0 and spoor>0:
        strng_out=strng.replace(strng[snot:],'good')
        return strng_out
    else:
        return strng
		
		
##Check max len word out of the list 
def max_len_word(word):
    result=[]
    for i in word:
        result.append((len(i),i))
    result.sort()
    return result[-1]

##check for unique words in the list
def uniq_vals(strng):
    resultset=set()
    for word in strng:
        resultset.add(word)
    return resultset

or 
    result=[]
    for word in strng:
        if strng.count(word)==1:
            result.append(word)
    return result
	

## count the total number of substrings in a word	
def number_of_substrings(str): 
	str_len = len(str); 
	return int(str_len * (str_len + 1) / 2); 

str1 = input("Input a string: ")
print("Number of substrings:") 
print(number_of_substrings(str1))

Input a string:  w3resource
Number of substrings:
55

##Count cases in a word
def count_cases(strng):
    upper_ctr,lower_ctr,no_ctr,spcl_ctr=0,0,0,0
    
    for i in range(len(strng)):
        if strng[i]>='A' and strng[i]<='Z':
            upper_ctr +=1
        elif strng[i]>='a' and strng[i]<='a':
            lower_ctr += 1
        elif strng[i]>='0' and strng[i]<='9':
            no_ctr +=1
        else:
            spcl_ctr +=1
    #return upper_ctr,lower_ctr,no_ctr,spcl_ctr
    print('upper case -- > {}'.format(upper_ctr))
    print('lower case -- > {}'.format(lower_ctr))
    print('number case -- > {}'.format(no_ctr))
    print('special case -- > {}'.format(spcl_ctr))



# program to restrict pi decimals
import math
def printpi(num):
    pi=math.pi
    print('{d:0.{}f}'.format(num,d=pi))
	
	

# program to restrict e decimals
import math
def print_e(num,dec):
    val=math.exp(num)
    print('{d:0.{}f}'.format(dec,d=val))
	
	
	
num1=0
num2=1
limit =8
while i <= limit:
    final_val=num1+num2
    num1=num2
    num2=final_val
    print(final_val)
	
	
def fibo(limit):
    num1=0
    num2=1
    print(num1,' ')
    print(num2,' ')
    #for i in range(2,limit):
    while num2<=limit:
        final_val=num1+num2
        print(final_val)
        num1=num2
        num2=final_val
		
		6,128
		
# remove duplicates

def uniq(nums):
    
    finallist=[]
    
    for i in nums:
        if i not in finallist:
            finallist.append(i)
    
    print(finallist)
	
	

def MaxNo(num):
    '''
    This program finds maximum number from a list
    Input required is a list of numbers
    '''
    
    max=0
    
    for i in num:
        if i>max:
            max = i
    return(max)
	
	

def Program_1(entry):
    
    '''
    This program takes an input of the string in a list and checks 
    string length is 2 or more and the first and last character are same from a given list of strings
    '''
    
    ctr=0
    
    for str in entry:
        if len(str)> 1 :
            if str[0].lower() == str[-1].lower():
                ctr += 1
        else:
            print('String length is less than 2')
    return ctr
	
	
def last(n):
    return n[-1]

def sort_list(nums):
    '''
    Usage of sorted sorted(iterable, /, *, key=None, reverse=False)
    '''
    return sorted(nums,key=last,reverse=False)
	
	
def compareList(l1,l2):
    
    '''
    This program checks for at least one common item in the list
    
    '''
    
    for i in l1:
        for j in l2:
            if i == j:
                return True
    return False
	
	
	compareList([1,2,3,4],[5,6,7,2,9])
	
	
for i in enumerate(['a','b','v']):
    print(i)
	
(0, 'a')
(1, 'b')
(2, 'v')


def checkduplist(lin):
    
    '''
    Remove duplicate list values from a list
    '''
    
    listout=[]
    for n in lin:
        if n not in listout:
            listout.append(n)
    return listout
	
	
	checkduplist([[10, 20], [40], [30, 56, 25], [10, 20], [30], [40],[30]])
	>> [[10, 20], [40], [30, 56, 25], [30]]
	
	
def sum_max_list(lin):
    
    '''
    program to find the list in a list of lists whose sum of elements is the highest
    '''
    
    z=0
    y=[]
    
    for i in lin:
        #print(i)
        x=sum(j for j in i )
        #print(x)
        if x>z:
            z=x
            y=i
    return y
	
	sum_max_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9],[100,200]])
	
	[100, 200]
	
	
	Dict--
	
dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60}
d={}
for i in (dic1,dic2,dic3):
    d.update(i)
	
	

list1= [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
list0=[]
for i in list1:
    i=i[:-1]+(100,)
    print(i) 
	
(10, 20, 100)
(40, 50, 100)
(70, 80, 100)


17. Write a Python program to print alphabet pattern 'A'. Go to the editor
Expected Output:

  ***                                                                   
 *   *                                                                  
 *   *                                                                  
 *****                                                                  
 *   *                                                                  
 *   *                                                                  
 *   *
 
 result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):    
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);



-- Count of set bits using list compre

def myfunc(num):
    binary=bin(num)
    print(binary)
    mylist= [x for x in binary if x=='1']
    return(mylist.count('1'))
	
myfunc(11)
0b1011
3


binary search--

def binary_search(list1,item):
    
    '''
    This is binary search algorithm to search an item in the list
    '''
    
    first=0
    last=int(len(list1)-1)
    
    while(first<last):
        mid=(first+last)//2
        
        if list1[mid]==item:
            return True
        else:
            if item <list1[mid]:
                last=mid-1
            else:
                first=mid+1
    return False
	

print(binary_search([1,2,3,5,8], 6))




def seq_search(dlist,item):
    
        '''
    This is sequential search algorithm to search an item in the list
    '''
    
    pos=0
    
    while pos<len(dlist):
        if dlist[pos]==item:
            return True,pos
        else:
            pos=pos+1
    return False,pos
	
	
	seq_search([11,23,58,31,56,77,43,12,65,19],31)
	
	
	
# Palindrome using strings

def ispalindrome(my_str):
    reversed_str = ''
    for letter in my_str:
        reversed_str = letter + reversed_str ## Appends the input string to empty string and pushes it inside
        
    if my_str == reversed_str:
        print("palindrome")
    else:
        print("not palindrome")
		
		
def is_palindrome(strng):
    length=int(len(strng)/2)
    for i in range(length):
        if strng[i]==strng[len(strng)-i-1]:
            return True
        else:
            return False
			
			
			
# Finding all non repeating character in a string
list1=[]
for i in range(len(x)):
    for j in range(i+1,len(x)):
        if  x[i] == x[j]:
            list1.append(x[i])

for j in range(len(x)):
    if x[j] not in list1:
        print(x[j])
		
		
def first_non_repeat(x):
    for index,c in enumerate(x):
        if x.count(c)<2:
            return c
    return None
	
	
	
def check_vowels(strng_input):

	'''
	This program checks whether all the vowels are there in the string or not
	'''

	vowel_Set=set('aeiou')
	result_Set=set()
	strng=strng_input.lower()

	for chars in strng:
		if chars in vowel_Set:
			result_Set.add(chars)
		else:
			pass

	if result_Set == vowel_Set:
		print('Accepted')
	else:
		print('Not Accepted')


if __name__ == '__main__':

	#string='ABeeIghiObhkUul'
	string='aeiot'

	check_vowels(string)



## Check commons items
def check_commons(ar1,ar2,ar3):

	set1=set(ar1)
	set2=set(ar2)
	set3=set(ar3)

	sub_result_set=set1.intersection(set2)

	final_result_set=sub_result_set.intersection(set3)

	print( list(final_result_set))

if __name__ == '__main__':	
	ar1 = [1, 5, 10, 20, 40, 80]
	ar2 = [6, 7, 20, 80, 100]
	ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

	check_commons(ar1,ar2,ar3)
	
	
	
def check_commons(a,b):

	s1=set(a)
	s2=set(b)
	s3=set()

	if s1.intersection(s2)==s3:  # returns only common items
		print('False')
	else:
		print('True')


if __name__ == '__main__':
	a = [1, 2, 3, 4, 5]
	b = [6, 7, 8, 9]
	check_commons(a,b)


