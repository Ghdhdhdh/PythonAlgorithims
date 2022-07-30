searchfor = "apple"

list_of_possible_matches = ["apple", "banna", "and"]
list_sorted = []

for i in range(len(searchfor)):
    for i in range(len(list_of_possible_matches)):
        if searchfor[i] == list_of_possible_matches[i]:
            list_sorted.append(list_of_possible_matches[i])
        else:
            continue
print(list_sorted)
