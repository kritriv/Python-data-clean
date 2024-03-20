import os
def count_data_in_folder(folder_path):
    total_count = 0 
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(folder_path, filename)
            file_count = sum(1 for line in open(file_path))
            print(f"File: {filename}, Count: {file_count}")
            total_count += file_count
    
    print("Total Count:", total_count)

folder_path = "new"

count_data_in_folder(folder_path)
