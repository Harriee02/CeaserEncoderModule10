import sys
def CeaserEncoder(shift):
    message = input()
    new_str = ""
    new_new = ""
    another_str = ""
    for i in message:
      if i.isalpha():
        new_str += i
    new_str = new_str.upper()
    for j in new_str:
      if ord(j) + shift > 90:
        another_str += chr(ord(j) - (26 - shift))
      else:
        another_str += chr(ord(j)+shift)
    counter = 5
    for q in range(0,len(another_str),5):
        new_new += another_str[q:counter]
        new_new += " "
        counter += 5
    return new_new
    
a = int(sys.argv[1])
print(CeaserEncoder(a))
