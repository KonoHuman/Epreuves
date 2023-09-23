def accum(s):
    if s.isalpha() == False:
        return "Not a string"
    elif s.isalpha() == True:
        result = ""
        for i in range(len(s)):
            result += s[i].upper() + s[i].lower() * i
            if i != len(s) - 1:
                result += "-"
        return result

# Testing the function
print(accum("abcd"))
print(accum("ZpglnRxqenU"))
print(accum("NyffsGeyylB"))
print(accum("MjtkuBovqrU"))
print(accum("EvidjUnokmM"))
print(accum("HbideVbxncC"))
