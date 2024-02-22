import json
import csv


class Item:
    def __init__(self, name, description, price, availability=True):
        self.name = name
        self.description = description
        self.price = price
        self.availability = availability


class ItemService:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def find_item(self, keyword):
        found_items = []
        for item in self.items:
            if keyword.lower() in item.name.lower() or keyword.lower() in item.description.lower():
                found_items.append(item)
        return found_items

    def delete_item(self, item_name):
        self.items = [item for item in self.items if item.name != item_name]

    def save_items_to_json(self, filename):
        items_data = []
        for item in self.items:
            items_data.append({"name": item.name, "description": item.description, "price": item.price,
                               "availability": item.availability})
        with open(filename, "w") as json_file:
            json.dump(items_data, json_file, indent=4)

    def save_items_to_csv(self, filename):
        with open(filename, "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Name", "Description", "Price", "Availability"])
            for item in self.items:
                writer.writerow([item.name, item.description, item.price, item.availability])


def display_menu():
    print("\n1. Add item")
    print("2. Search for items")
    print("3. Delete an item")
    print("4. Exit")


def item_giver_menu(item_service):
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter item name: ")
            description = input("Enter item description: ")
            price = float(input("Enter item price: "))
            availability = input("Is the item available? (yes/no): ").lower() == 'yes'
            item = Item(name, description, price, availability)
            item_service.add_item(item)
            print("Item added successfully!")
        elif choice == '2':
            keyword = input("Enter keyword to search for items: ")
            found_items = item_service.find_item(keyword)
            if found_items:
                print("Found items matching your search:")
                for item in found_items:
                    print(f"Name: {item.name}, Description: {item.description}, Price: ${item.price}, "
                          f"Availability: {'Available' if item.availability else 'Not Available'}")
            else:
                print("No items found matching your search.")
        elif choice == '3':
            item_name = input("Enter the name of the item you want to delete: ")
            item_service.delete_item(item_name)
            print(f"Item '{item_name}' deleted successfully!")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")


def main():
    item_service = ItemService()
    item_giver_menu(item_service)
    item_service.save_items_to_json("items.json")
    item_service.save_items_to_csv("items.csv")


if __name__ == "__main__":
    main()
if __name__ == "__main__":
    main()
