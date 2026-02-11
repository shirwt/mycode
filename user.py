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
      print(f"Country: {self.country}\n")
  
  
  def user_phone(self):
      if len(self.phone) != 10:
          print("Invalid phone number")
          return False
      return True
          

people = []
while True: 
    user_ID = input("ID: ")
    user_name = input("Name: ")
    user_passwd = input("Password: ")
    user_phone = input("Phone: ")
    user_dob= input("DOB: ")
    user_address = input("Address: ")
    user_country = input("Country: ")
    
    p = Person( user_ID, user_name, user_passwd, user_phone, user_dob, user_address, user_country)
    people.append(p)
    
    que = input("Do you want to add more data? Yes or no: ").lower()
    if que == "no" or que == "yes":
        if que == "no":
            break
    else: 
        print("---WRONG INPUT, TRY AGAIN!!!---")
     

    
print("---USER'S DATA---")        
for i in people:
    
    if not i.user_phone():
        break
    i.display()
    print("-----------")







