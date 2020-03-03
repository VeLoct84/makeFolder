#!/usr/bin/python3.7

import os


"""
1.Set the path
2.naming folder want to generate in list
3.os.mkdir function
"""

# Main folder naming provided.
directory = [
    "01_Central_Model",
    "02_Apartment_Comp",
    "03_Podium_Comp",
    "04_Site_Facilities_Comp",
    "05_Basement_Comp",
    "06_Component",
    "Pdf",
    "Dwg"
]

# Sub-folder certain folder.
sub_folder = [
    "sample.rvt",
    "Typical Floor",
    "Typical Unit"
]

# Additional for sub-folder.
extra_folder = []


# Request path input from user.
path = input("Please insert the path: \n")

for f in directory:
    join = os.path.join(f, path)
    os.mkdir(join)
    print("Folder is created!")
