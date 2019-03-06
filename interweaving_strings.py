#Given 3 strings A B C, return true if C is a valid interweaving of strings A and B. 
#Return false otherwise. Example: A=zzxy, B=xwv, C=zxzxywv Answer = True

#3 Cases, 1 when strings are equal, 2 when string 1 is greater, 3 when string 2 is greater
string1 = "zzxyy"
string2 = "xwv"

string3 = "zxzwxvy"

def interweave_strings(string1, string2):
    output_string = ""
    if len(string1) == len(string2):
        for i in range(len(string1)):
            output_string+= string1[i]+string2[i]
    elif len(string1) > len(string2):
        string_dif = len(string1)-len(string2)
        for i in range(len(string1)-string_dif):
            output_string += string1[i]+string2[i]
        output_string += string1[len(string1)-string_dif:len(string1)]
    elif len(string1) < len(string2):
        string_dif = len(string2) - len(string1)
        for i in range(len(string2)- string_dif):
            output_string += string1[i] + string2[i]
        output_string += string2[len(string2)- string_dif:len(string2)]
    return output_string
print(interweave_strings(string1, string2))