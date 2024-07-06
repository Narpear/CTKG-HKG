import os

def delete_file(nct):
    # Specify the file path using f-string
    file_path = f"{nct}.html"

    # Check if the file exists
    if os.path.exists(file_path):
        # Delete the file
        os.remove(file_path)
        print(f"The file '{file_path}' has been deleted.")
    else:
        print(f"The file '{file_path}' does not exist.")

# delete_file('NCT03003143')
