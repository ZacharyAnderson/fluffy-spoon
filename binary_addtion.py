def binary_add(string1, string2):
    carry = 0
    answer = ''

    if len(string1) > len(string2):
        string2 = (len(string1)- len(string2)) * "0" + string2
    elif len(string2) > len(string1):
        string1 = (len(string2) - len(string1)) * "0" + string1
    
    for i in range(len(string1)-1, -1, -1):
        str1 = int(string1[i])
        str2 = int(string2[i])

        if carry + str1 + str2 == 0:
            carry = 0
            answer = "0" + answer
        elif carry + str1 + str2 == 1:
            carry = 0
            answer = "1" + answer
        elif carry + str1 + str2 == 2:
            carry = 1
            answer = "0" + answer
        elif carry + str1 +str2 == 3:
            carry =1 
            answer = "1" + answer

    return answer

string1="10110"
string2="0101"

print(binary_add(string1, string2))