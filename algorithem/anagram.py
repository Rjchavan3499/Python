def check(s1, s2):

    if (sorted(s1) == sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")



s1 = "listen"
s2 = "silent"
check(s1, s2)





#from collections import Counter

#def check(s1, s2):

	# implementing counter function
	#if(Counter(s1) == Counter(s2)):
		#print("The strings are anagrams.")
	#else:
		#print("The strings aren't anagrams.")


# driver code
#s1 = "listen"
#s2 = "silent"
#check(s1, s2)






#Counter is a container that will hold the count of each of the elements present in the container.
# Counter is a sub-class available inside the dictionary class.
# Using the Python Counter tool, you can count the key-value pairs in an object,
# also called a hashtable object