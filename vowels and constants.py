char=input("enter the alphabet")
char=char.lower()
if len(char)==1 and char in ['a', 'e', 'i', 'o', 'u']:
        print("vowel")
else:
    print("constant")


