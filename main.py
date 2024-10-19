import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk
from req import *
import csv

root = tk.Tk()

def main():
    root.title('Main')
    root.geometry("1400x900")

    open_search_butt = ttk.Button(master=root, text = "Open Search Window", command=open_search_window)
    open_search_butt.grid(row = 0, column = 0, sticky = "w", padx = 0, pady = 30)

    try:
        font = ("Arial bold", 30)
        padx = 30
        pady = 100

        final_dict = return_final_dict(read_csv())

    except NotPositiveError as e:
        error = ttk.Label(root, text = e, font = font) 
        error.grid(row = 1, column = 0, sticky = "w", padx = padx, pady = pady)
    except ValueError as e:
        error = ttk.Label(root, text = e, font = font) 
        error.grid(row = 1, column = 0, sticky = "w", padx = padx, pady = pady)
    except CryptoNotFound as e:
        error = ttk.Label(root, text = e, font = font) 
        error.grid(row = 1, column = 0, sticky = "w", padx = padx, pady = pady)
    else:
        total_val_all = calculate_total_value_all(final_dict)

        padx, pady = 50, 15
        font = ("Arial bold", 25)
        name_label = ttk.Label(root, text = "Name", font= font) 
        name_label.grid(row = 1, column = 0, sticky = "w", padx = padx, pady = pady)
        name_label = ttk.Label(root, text = "Current Price", font = font) 
        name_label.grid(row = 1, column = 1, sticky = "w", padx = padx, pady = pady)
        name_label = ttk.Label(root, text = "Amount", font = font) 
        name_label.grid(row = 1, column = 2, sticky = "w", padx = padx, pady = pady)
        name_label = ttk.Label(root, text = "Total", font = font) 
        name_label.grid(row = 1, column = 3, sticky = "w", padx = padx, pady = pady)

        for i in range(4):
            divider = ttk.Label(root, text = "---------------------", font = font)
            divider.grid(row = 2, column = i,sticky = "w", padx = 0, pady = 0)


        for i, row in enumerate(final_dict):
            i += 3
            name_label = ttk.Label(root, text = row["name"], font = font) 
            name_label.grid(row = i, column = 0, sticky = "w", padx = padx, pady = pady)
        
            name_label = ttk.Label(root, text = row["priceusd"], font = font) 
            name_label.grid(row = i, column = 1, sticky = "w", padx = padx, pady = pady)

            name_label = ttk.Label(root, text = row["amount"], font = font) 
            name_label.grid(row = i, column = 2, sticky = "w", padx = padx, pady = pady)

            name_label = ttk.Label(root, text = row["total_val"], font = font)
            name_label.grid(row = i, column = 3, sticky = "w", padx = padx, pady = pady)

            if i == (len(final_dict) - 1 + 3):
                divider = ttk.Label(root, text = "---------------", font = font)
                divider.grid(row = i + 1, column = 3,sticky = "w", padx = 0, pady = 0)

                total_value = ttk.Label(root, text = f"Total Value: {round(total_val_all, 2)}$", font = font)
                total_value.grid(row = i + 2, column = 3, sticky = "w", padx = 0, pady = 0)


    root.mainloop()


def open_search_window():
    global amount, id
    search_window = tk.Toplevel(root)
    search_window.title("Search Window")
    search_window.geometry("800x600")

    label = ttk.Label(master = search_window, text = "Search", font = "Calibri 30 bold")
    label.pack(pady = 10)
    search_entry = ttk.Entry(master=search_window, width = 30)
    search_entry.pack()


    result_text = tk.StringVar()
    def search_func():
        global id, amount
        name = search_entry.get()
        print(search_req(name))

        if search_var :=search_req(name):
            result_text.set(f"----------------------------\nfound: {search_var["name"]}")
        else:
            result_text.set(f"----------------------------\nError: Could not find {name}!")
        
        
    search_button = tk.Button(master = search_window, text = "Find", command = search_func, font=("Arial", 12), padx=15, pady=15)
    search_button.pack(pady = 10)
    result_label = ttk.Label(search_window, textvariable = result_text, font = "Arial 25")
    result_label.pack()

def read_csv(path = "portfolio.csv"):
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        reader_list = []
        for row in reader:
            if not isinstance(row["name"], str):
                raise NotStringError("All id variables should be strings")
            
            try:
                row["amount"] = float(row["amount"])
            except ValueError:
                raise ValueError(f"All amount variable should be Integers or Floats:\n\nname = {row["name"]}, amount =  {row["amount"]}")
            
            if row["amount"] <= 0:
                raise NotPositiveError(f"Error: amount variables can not be zero or less:\n\n name = {row["name"]}, amount = {row["amount"]}")
            
            if search_result := search_req(row["name"]):
                new_row = search_result
                new_row["amount"] = row["amount"]
            else:
                raise CryptoNotFound(f"Could not find this Crypto: {row["name"]}")
            
            reader_list.append(new_row)
            
        return reader_list
        
def return_final_dict(reader_list):
    for row in reader_list:
        row["total_val"] = row["amount"] * float(row["priceusd"])
        row["total_val"] = f"{row["total_val"]:.2f}"
        row["priceusd"] = "{:.4f}".format(float(row["priceusd"]))
    return reader_list
        
def calculate_total_value_all(final_dict):
    total_value_all = 0
    for row in final_dict:
        total_value_all += float(row["total_val"])
    return total_value_all

class CryptoNotFound(Exception):
    pass
class NotPositiveError(Exception):
    pass
class NotStringError(Exception):
    pass
if __name__ == "__main__":
    main()

