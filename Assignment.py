#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json

class SATResultsSystem:
    def __init__(self):
        self.data = []

    def insert_data(self, name, address, city, country, pincode, sat_score):
        passed = "Pass" if sat_score > 30 else "Fail"
        record = {
            "Name": name,
            "Address": address,
            "City": city,
            "Country": country,
            "Pincode": pincode,
            "SAT Score": sat_score,
            "Passed": passed
        }
        self.data.append(record)
        print(f"Data for {name} inserted successfully.")

    def view_all_data(self):
        print(json.dumps(self.data, indent=2))

    def get_rank(self, name):
        sorted_data = sorted(self.data, key=lambda x: x["SAT Score"], reverse=True)
        for i, record in enumerate(sorted_data, 1):
            if record["Name"] == name:
                print(f"{name} has rank {i}.")
                return
        print(f"No record found for {name}.")

    def update_score(self, name, new_score):
        for record in self.data:
            if record["Name"] == name:
                record["SAT Score"] = new_score
                record["Passed"] = "Pass" if new_score > 30 else "Fail"
                print(f"SAT score updated for {name}.")
                return
        print(f"No record found for {name}.")

    def delete_record(self, name):
        for record in self.data:
            if record["Name"] == name:
                self.data.remove(record)
                print(f"Record for {name} deleted successfully.")
                return
        print(f"No record found for {name}.")

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            json.dump(self.data, file, indent=2)
        print(f"Data saved to {filename}.")

def main():
    sat_system = SATResultsSystem()

    while True:
        print("\nMenu:")
        print("1. Insert data")
        print("2. View all data")
        print("3. Get rank")
        print("4. Update score")
        print("5. Delete one record")
        print("6. Save to JSON file")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Name: ")
            address = input("Enter Address: ")
            city = input("Enter City: ")
            country = input("Enter Country: ")
            pincode = input("Enter Pincode: ")
            sat_score = int(input("Enter SAT Score: "))
            sat_system.insert_data(name, address, city, country, pincode, sat_score)
        elif choice == "2":
            sat_system.view_all_data()
        elif choice == "3":
            name = input("Enter Name: ")
            sat_system.get_rank(name)
        elif choice == "4":
            name = input("Enter Name: ")
            new_score = int(input("Enter new SAT Score: "))
            sat_system.update_score(name, new_score)
        elif choice == "5":
            name = input("Enter Name: ")
            sat_system.delete_record(name)
        elif choice == "6":
            filename = input("Enter the filename to save: ")
            sat_system.save_to_file(filename)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




