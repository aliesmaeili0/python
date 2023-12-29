#می‌توان اعضای منحصر به فرد یک لیست را استخراج کرد
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_elements = []

for item in my_list:
    if item not in unique_elements:
        unique_elements.append(item)

print(unique_elements)
