"""
Utility to enrich Jupyter notebook (.ipynb) files by adding cell number comments.
For each code cell, adds a comment like '#CELL-NO: 1', '#CELL-NO: 2', etc. as the first line.
"""

import json
import sys
import os
import argparse
from pathlib import Path


def enrich_notebook(notebook_path) -> None:
    """
    Enrich a Jupyter notebook by adding cell number comments to code cells.
    
    Args:
        notebook_path (str): Path to the .ipynb file
    """
    # Validate input file
    if not os.path.exists(notebook_path):
        raise FileNotFoundError(f"Notebook file not found: {notebook_path}")
    
    notebook_path = Path(notebook_path)
    
    # Read and parse the notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook_data = json.load(f)

    # Process cells
    cells = notebook_data.get('cells', [])
    cell_counter = 1
    modified = False

    for cell in cells:
        # Process only code cells
        if cell.get('cell_type') == 'code':
            source = cell.get('source', [])
            
            # Check if the cell already has a cell number comment at the start
            # Skip if it already starts with a cell number comment
            if source and isinstance(source[0], str):
                first_line = source[0].strip()
                if first_line.startswith('#CELL-NO: '):
                    # Already has a cell number comment, skip this cell
                    cell_counter += 1
                    continue
            
            # Add cell number comment as the first line
            comment = f"#CELL-NO: {cell_counter}\n"
            
            # Insert the comment at the beginning of the source
            if isinstance(source, list):
                source.insert(0, comment)
            else:
                # If source is a string, convert to list
                source = [comment] + [source] if source else [comment]
            
            cell['source'] = source
            cell_counter += 1
            modified = True

    # Write back to the notebook file if modified
    if modified:
        with open(notebook_path, 'w', encoding='utf-8') as f:
            json.dump(notebook_data, f, indent=1, ensure_ascii=False)
        print(f"Successfully enriched {notebook_path}")
    else:
        print(f"No code cells found or already enriched: {notebook_path}")


def enrich_notebooks_in_folder(folder_path) -> None:
    """
    Enrich all .ipynb files in a folder.
    
    Args:
        folder_path (str): Path to the folder containing .ipynb files
    """
    # Validate input folder
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Folder not found: {folder_path}")
    
    if not os.path.isdir(folder_path):
        raise ValueError("Input must be a folder/directory")
    
    folder_path = Path(folder_path)
    
    # Find all .ipynb files in the folder
    notebook_files = list(folder_path.glob('*.ipynb'))
    
    if not notebook_files:
        print(f"No .ipynb files found in {folder_path}")
        return
    
    print(f"Found {len(notebook_files)} notebook file(s) in {folder_path}")
    
    # Enrich each notebook
    for notebook_file in notebook_files:
        try:
            enrich_notebook(notebook_file)
        except Exception as e:
            print(f"Error processing {notebook_file}: {str(e)}")


def main():
    """Main function to handle command line arguments."""
    parser = argparse.ArgumentParser(
        description="Enrich Jupyter notebook (.ipynb) files by adding cell number comments to code cells")
    parser.add_argument(
        'folder',
        help='Path to the folder containing .ipynb files to enrich'
    )
    
    args = parser.parse_args()
    enrich_notebooks_in_folder(args.folder)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(100)

