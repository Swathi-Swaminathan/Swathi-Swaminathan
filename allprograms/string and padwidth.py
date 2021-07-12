##this function receives a string, and a pad width, and encodes the string as a title (according to the instructions provided
##above).
##Note: for every word, the first alphabetic character has to be uppercase. For instance, if the word is ‘123abc’, then it will
##be encoded as '123Abc'.
##Examples:
##
##• encode_title ("aaaa", 4) == "Aaaa"
##• encode_title ("aaaa", 5) == "0Aaaa"
##• encode_title ("hello mY naME is iynigo Montoya", 40) == '000000000Hello My Name Is Iynigo Montoya'
##• encode_title ("000hello mY naME is iynigo Montoya", 40) == '000000000Hello My Name Is Iynigo Montoya




a=input("Enter a sentence:")
pw=int(input("Enter the padwidth:"))
b=a.title()
res = b.rjust(pw,'0')
print("The string after adding leading zeros : ",res)
