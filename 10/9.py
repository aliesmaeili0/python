#چگونه می‌توان یک دیکشنری از دو لیست ایجاد کرد
keys = ['name', 'age', 'city']
values = ['John', 25, 'New York']

# ایجاد دیکشنری با استفاده از تابع zip()
my_dict = dict(zip(keys, values))

print(my_dict)
