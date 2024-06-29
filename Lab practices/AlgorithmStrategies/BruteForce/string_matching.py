def string_matching(string1: str, string2):
    str1_length = len(string1)
    str2_length = len(string2)
    for i in range(0, str1_length-str2_length+1):
        j = 0
        while j < str2_length and string1[j+i] == string2[j]:
            j = j+1
        if j == str2_length:
            return i
    return -1


if __name__ == "__main__":
    print(string_matching("Prashant", "ras"))
