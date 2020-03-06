#!/usr/bin/python3.7

import pathlib


"""
1.Set the path
2.naming folder want to generate in list
3.os.mkdir function
"""

# Main folder naming provided.
directory = {
    "00_Design_Stage": {"Typical Floor": None,
                        "Typical Unit": None},
    "01_Central_Model": {"sample.rvt": None},
    "02_Apartment_Comp": {"Typical Floor": None,
                          "Typical Unit": None},
    "03_Podium_Comp": {"sample.rvt": None},
    "04_Site_Facilities_Comp": {"GuardHouse": None,
                                "SalesGallery": None,
                                "ShopLot": None},
    "05_Basement_Comp": {"sample.rvt": None},
    "06_Component": {"sample.rvt": None},
    "Pdf": {"sample.pdf": None},
    "Dwg": {"sample.dwg": None}
}


def create_folders(root_path, folders):
    for folder, subfolders in folders.items():
        (root_path / folder).mkdir(parents=True, exist_ok=True)
        if subfolders is not None:
            create_folders(root_path / folder, subfolders)


# Request path input from user.
root = input("Please key in the file path: \n")
root_path = pathlib.Path(root)
create_folders(root_path, directory)

print("Folder is created!")
