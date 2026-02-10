class Person:
  def __init__(self, ID, name, password, phone, DOB, address, country):
    self.ID = ID
    self.name = name
    self.passwd = password
    self.phone = phone
    self.DOB = DOB
    self.address = address 
    self.country = country
    
  def display(self):
      print(f"ID: {self.ID}")
      print(f"Name: {self.name}")
      print(f"Password: {self.passwd}")
      print(f"Phone: {self.phone}")
      print(f"DOB: {self.DOB}")
      print(f"Address: {self.address}")
      print(f"Country: {self.country}")


people = []
while True: 
    user_ID = input("enter ID: ")
    user_name = input("Enter Name: ")
    user_passwd = input("Enter Password: ")
    user_phone = input("Enter Phone: ")
    user_dob= input("Enter DOB: ")
    user_address = input("Enter Address: ")
    user_country = input("Enter Country: ")
    
    p = Person( user_ID, user_name, user_passwd, user_phone, user_dob, user_address, user_country)
    people.append(p)
    
    que = input("Do you want to add more data? Yes or no: ").lower()
    if que == "no":
        break

print("---USER'S DATA---")        
for i in people:
    i.display()
    print("-----------")







