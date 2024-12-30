from collections import UserDict
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value: str):
            if not value.strip():
                raise ValueError("Name required field.")
            super().__init__(value.strip())
          
class Phone(Field):
    def __init__(self, phone):
        if not re.match(r'^\d{10}$', phone):
            raise ValueError("The phone number must be 10 digits.")
        super().__init__(phone)
    
    

class Record:
    def __init__(self, name = ""):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone = ""):
        self.phones.append(Phone(phone))
        return "Added mobile phone number."

    def remove_phone(self, phone: str):
        phone = self.find_phone(phone)
        if isinstance(phone, str):
            return phone
        
        self.phones.pop(self.phones.index(phone))
        return "Mobile number has been deleted."
        

    def edit_phone(self, old_phone, new_phone):
        phone = self.find_phone(old_phone)
        if isinstance(phone, str):
            return phone
        
        self.phones[self.phones.index(phone)] = Phone(new_phone)
        return "Mobile number has been changed."
       
    def find_phone(self, phone):
        for number in self.phones:
            if phone == number.value:
                return number
        return "Mobile number not found."

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        if str(record.name).lower() in self.data:
            raise ValueError(f"AddressBook already have record with name {str(record.name)}")
        self.data[str(record.name).lower()] = record
    
    def find(self, name: str):
        for name_record, record in self.data.items():
            if name_record == name.lower().strip():
                return record
        return "Record not found."
    
    def delete(self, name: str):
        return self.data.pop(name.lower().strip(), None)