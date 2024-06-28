file=open("basic.txt","r")
number_of_lines=0
number_of_words=0
number_of_characters=0
for line in file:
    number_of_lines=number_of_lines+1
    line=line.strip("/n")
    print(line)
    word=line.split()
    number_of_words+=len(words)
    number_of_character+=len(line)
    file.close()
    print("lines:",number_of_lines,"words:",number_of_words,"character:",number_of_characters)
  





