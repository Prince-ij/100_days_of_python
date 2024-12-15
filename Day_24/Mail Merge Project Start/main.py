with open("Mail Merge Project Start\\Input\\Letters\\starting_letter.txt", "r") as letter:
    template = letter.read()

with open("Mail Merge Project Start\\Input\\Names\\invited_names.txt", "r") as s_names:
    names = s_names.readlines()

for name in names:
    new_template = template.replace("[name]", name.strip())
    with open(f"Mail Merge Project Start\\Output\\ReadyToSend\\letter_for_{name.strip()}.txt", "w") as sent:
        sent.write(new_template)
