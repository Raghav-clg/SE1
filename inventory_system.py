"""
A simple inventory management module.

This module manages an in-memory stock inventory and can
load/save it to a JSON file.
"""
import json
from datetime import datetime

# Global variable
stock_data = {}

def add_item(item="default", qty=0, logs=[]):
    """
    Adds a specified quantity of an item to the stock.

    Args:
        item (str): The name of the item to add.
        qty (int): The quantity to add.
    """
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty


def remove_item(item, qty):
    """
    Removes a specified quantity of an item from the stock.

    If the resulting quantity is zero or less, the item is
    removed completely from the stock.

    Args:
        item (str): The name of the item to remove.
        qty (int): The quantity to subtract.
    """
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"ERR: Item '{item}' not found in stock.")
    except TypeError:
        print(f"ERR: Invalid quantity type for item '{item}'.")

def get_qty(item):
    """
    Retrieves the current quantity of a specific item.

    Args:
        item (str): The name of the item to query.

    Returns:
        int: The quantity of the item in stock.
             Raises KeyError if the item is not found.
    """
    return stock_data[item]

def load_data(file="inventory.json"):
    """
    Loads the stock inventory from a JSON file.

    Note: This function has a bug and only updates a local
    variable, not the global 'stock_data'.

    Args:
        file (str): The name of the JSON file to read from.
                    Defaults to "inventory.json".
    """
    global stock_data
    with open(file, "r", encoding="utf-8") as f:                
        stock_data = json.loads(f.read())

def save_data(file="inventory.json"):
    """
    Saves the current stock inventory to a JSON file.

    Args:
        file (str): The name of the JSON file to write to.
                    Defaults to "inventory.json".
    """
    with open(file, "w", encoding="utf-8") as f:
        f.write(json.dumps(stock_data))

def print_data():
    """Prints a formatted report of all items and their quantities."""
    print("Items Report")
    for i in stock_data:
        print(f"{i} -> {stock_data[i]}")

def check_low_items(threshold=5):
    """
    Finds all items with a quantity below a specified threshold.

    Args:
        threshold (int): The stock level to check against.
                         Defaults to 5.

    Returns:
        list: A list of item names that are below the threshold.
    """
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result

def main():
    global stock_data
    """
    Main function to demonstrate and test the inventory system.

    Runs a sequence of operations: adding items, removing items,
    checking quantities, checking low stock, saving, and loading.
    """
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")  # invalid types, no check
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()
    eval("print('eval used')")  # dangerous

main()