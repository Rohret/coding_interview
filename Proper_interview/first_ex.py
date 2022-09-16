

def reverse_string(str1):
    answer = ""
    for i in range(len(str1)):
        answer = answer + str1[len(str1)-1-i]
    
    print(answer)

def reverse_string1(str1):
    str1 = str1[::1]
    print(str1) 

reverse_string1("Valtech arbetar med agila metoder")