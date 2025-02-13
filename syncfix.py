import os

def hide_folder(folder_path):
    """
    Hides the specified folder to make it invisible to other users on Windows.

    :param folder_path: The full path to the folder to be hidden.
    """
    try:
        # Check if the folder exists
        if not os.path.exists(folder_path):
            raise FileNotFoundError(f"The folder '{folder_path}' does not exist.")
        
        # Using attrib command to set the hidden and system attributes
        os.system(f'attrib +h +s "{folder_path}"')
        print(f"'{folder_path}' is now hidden.")
    except Exception as e:
        print(f"An error occurred: {e}")

def unhide_folder(folder_path):
    """
    Unhides the specified folder to make it visible again.

    :param folder_path: The full path to the folder to be unhidden.
    """
    try:
        # Check if the folder exists
        if not os.path.exists(folder_path):
            raise FileNotFoundError(f"The folder '{folder_path}' does not exist.")
        
        # Using attrib command to remove the hidden and system attributes
        os.system(f'attrib -h -s "{folder_path}"')
        print(f"'{folder_path}' is now visible.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="SyncFix: Hide or unhide folders on Windows.")
    parser.add_argument("action", choices=["hide", "unhide"], help="Action to perform: hide or unhide a folder.")
    parser.add_argument("folder_path", help="The full path of the folder to hide or unhide.")

    args = parser.parse_args()

    if args.action == "hide":
        hide_folder(args.folder_path)
    elif args.action == "unhide":
        unhide_folder(args.folder_path)