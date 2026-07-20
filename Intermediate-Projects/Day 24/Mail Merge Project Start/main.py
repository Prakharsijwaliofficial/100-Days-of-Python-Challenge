#TODO: Create a letter using starting_letter.txt

#for each name in invited_names.txt
with open("./Mail Merge Project Start/Input/Names/invited_names.txt") as file:
    name = [name.strip() for name in file.readlines()]

for n in name:
    with open("./Mail Merge Project Start/Input/Letters/starting_letter.txt") as file2:
        draft_mail = file2.read()
        #Replace the [name] placeholder with the actual name.
        mail = draft_mail.replace("[name]" , n)
        #Save the letters in the folder "ReadyToSend".
        with open(f"./Mail Merge Project Start/Output/ReadyToSend/letter_for_{n}.docx", mode = "w") as file3:
            file3.write(mail)









