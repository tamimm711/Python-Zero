text = input("Text: ")
ch_dict: dict[str, int] = {}

for i in text:
    if i in ch_dict:
        ch_dict[i] += 1
    else:
        ch_dict[i] = 1

print(ch_dict)