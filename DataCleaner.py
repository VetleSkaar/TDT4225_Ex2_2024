import os
from pathlib import Path
import shutil

from walk_dataset import walk_dataset

# Read file, reads from line 6 then write it without the 6 first lines
def remove_lines(output_file_path: Path, remove_line: int):
    with open(output_file_path, 'r') as file:
        lines = file.readlines()[remove_line:]
    with open(output_file_path, 'w') as file:
        file.writelines(lines)


# Read file, split it into lines, then by coulmn
def remove_columns(output_file_path: Path):        
    with open(output_file_path, 'r') as file:
        lines = file.readlines()

    modified_lines = []

    for line in lines:
        coulmn = line.strip().split(',')
        # Index error, delete 5 first
        del coulmn[4]  
        del coulmn[2]
        
        modified_line = ','.join(coulmn)
        modified_lines.append(modified_line)

    with open(output_file_path, 'w') as file:
        file.writelines('\n'.join(modified_lines))


# Merge field 3 and 4 (old 6&7) then delete 4 (old 7)
def column_merger(output_file_path: Path):
    with open(output_file_path, 'r') as file:
        lines = file.readlines()

    modified_lines = []

    for line in lines:
        coulmn = line.strip().split(',')
        
        coulmn[3] = coulmn[3] + " " + coulmn[4]
        del coulmn[4]
        
        modified_line = ','.join(coulmn)
        modified_lines.append(modified_line)

    with open(output_file_path, 'w') as file:
        file.writelines('\n'.join(modified_lines))


# returns the length of file
def check_length(output_file_path: Path) -> int:
    with open(output_file_path, 'r') as file:
        lines = file.readlines()    
    
    return len(lines)

# Delete 
def delete_file(output_file_path: Path):
    output_file_path.unlink()


# Process Func, Delete if more that 2500 entries
def process_file(input_file_path: Path, output_file_path: Path):
    print(f"Current: {input_file_path} -> {output_file_path}")

    output_file_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(input_file_path, output_file_path)
    
    if input_file_path.suffix != ".plt":
        print("Got invaid file:", input_file_path, "not processing")
        return
    
    remove_lines(output_file_path, 6)
    
    if check_length(output_file_path) >= 2500:
        delete_file(output_file_path)
        return
    
    remove_columns(output_file_path)
    column_merger(output_file_path)


# Function to process all files in a folder
def process_folder(input_folder: Path, output_folder: Path):
    os.makedirs(output_folder, exist_ok=True)
    
    for file, _ in walk_dataset(input_folder):
        input_file_path = Path(input_folder, file)
        output_file_path = output_folder / file
        print(input_file_path.exists(), output_file_path)
        process_file(input_file_path, output_file_path)

if __name__ == "__main__":
    # WARN
    # Hard Coded path, should work if cloned from Repo
    process_folder(Path("TDT4225_Ex2_2024\dataset\dataset\Data"), Path("TDT4225_Ex2_2024\dataset\out\Data"))