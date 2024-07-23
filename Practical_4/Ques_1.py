#Ques.1:

file_name=input("Enter the name of file you want to work with (eg:file.txt) : ")

with open(file_name, 'r') as file:
    content=file.read()
    without_spaces=content.replace(" ", "")
    without_lines=without_spaces.replace("\n", "")
    without_lines=without_lines.lower()
    character_count=len(without_lines)
    print(f"The number of chracters in the file is {character_count}")
    
    words=content.split()
    words_count=len(words)
    print(f"The total number of words in file is {words_count}")
    
    no_of_lines=content.split("\n")
    list_count=len(no_of_lines)
    print(f"The number of lines in the file is {list_count}")
    
    characters=[]
    for char in without_lines:
        if char not in characters:
            characters.append(char)
    count_dict={}
    for i in range (0, (len(characters))):
        count_dict.update({characters[i]:without_lines.count(characters[i])})
    print(count_dict)
    
    without_new_lines=content.replace("\n", " ")
    ls_words=without_new_lines.split()
    for i in range (len(ls_words), 0, -1):
        print(ls_words[i-1], end=" ")