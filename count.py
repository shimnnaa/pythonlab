names_input=input("enter first names seperated by commas:")
names_list=[name.strip() for name in names_input.split(",")]
combined_names=''. join(names_list)
count_a=combined_names.lower().count('a')
print(f"total number of 'a' characters in the list:{count_a}")
