def main():
    file_name = input("Enter name of text file: ")
    f = open(file_name,"rt")
    content = f.read().lstrip().rstrip()
    chars,spaces,uppers,lowers,digits = 0,0,0,0,0
    for char in content:
        if (char.isascii() == True):
            chars += 1
        if (char.isspace() == True):
            spaces += 1
        if (char.isupper() == True):
            uppers += 1
        if (char.islower() == True):
            lowers += 1
        if (char.isdigit() == True):
            digits += 1
    vlist = ["a","e","i","o","u"]
    vowels = {}
    for v in vlist:
        vowels[v] = content.count(v) + content.count(v.upper())
    voweltotal = 0
    for item in vowels:
        voweltotal += vowels[item]
    sentances = content.count(".")
    print()
    print("Statistics for file ", file_name)
    print()
    print("Characters:", chars)
    print("Upper case:", uppers)
    print("Lower case: ",lowers)
    print("Digits:",digits)
    print("White space:",spaces)
    print("Vowels:",vowels)
    print("consonants:",((uppers+lowers)-voweltotal))
    print("sentances:",sentances)
    print("Average words per sentence:",((spaces-1)/sentances).__round__(1))
    f.close()
if __name__ == "__main__":
    main()