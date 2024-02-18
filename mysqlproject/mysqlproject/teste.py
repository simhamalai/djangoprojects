from faker import Faker

fakegen=Faker()
for i in range(10):
    print('Name : ',fakegen.name())
