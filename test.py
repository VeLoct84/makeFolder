#!/usr/bin/python3.7

main_folder = {
    "00_Design_Stage": {"Typical Floor": None,
                        "Typical Unit": None},
    "01_Central_Model": {"sample.rvt": None},
}


def create_folders(root_path, folders):
    for folder, subfolders in folders.items():
        (root_path / folder).mkdir(parents=True, exist_ok=True)
        if subfolders is not None:
            create_folders(root_path / folder, subfolders)
