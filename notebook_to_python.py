"""
Utility to convert Jupyter notebook (.ipynb) files to Python (.py) files.
Extracts only code cells and writes them to a Python file.
"""

import json
import sys
import os
import argparse
from pathlib import Path


def convert_notebook_to_python(notebook_path) -> None:
    """
    Convert a Jupyter notebook to a Python file.
    
    Args:
        notebook_path (str or Path): Path to the .ipynb file
    
    Returns:
        str: Path to the created .py file
    """
    # Convert to Path object if it's a string
    notebook_path = Path(notebook_path)
    
    # Validate input file
    if not notebook_path.exists():
        raise FileNotFoundError(f"Notebook file not found: {notebook_path}")
    
    if notebook_path.suffix != '.ipynb':
        raise ValueError("Input file must be a .ipynb file")
    
    # Create output file path
    output_path = notebook_path.with_suffix('.py')
    
    # Read and parse the notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook_data = json.load(f)

    # Extract code cells
    code_lines = []
    cells = notebook_data.get('cells', [])

    for cell in cells:
        # Filter for code cells only
        if cell.get('cell_type') == 'code':
            source = cell.get('source', [])

            # Process source lines
            for line in source:
                # Remove trailing newlines as we'll add them back
                line = line.rstrip('\n')

                #comment pip install lines
                if line.startswith('!') or line.startswith('%'):
                    line = "#" + line
                    
                code_lines.append(line)

            # Add empty line between cells
            code_lines.append('')

    # Write to Python file
    with open(output_path, 'w', encoding='utf-8') as f:
        for line in code_lines:
            f.write(line + '\n')

    print(f"Successfully converted {notebook_path} to {output_path}")


def convert_notebooks_in_folder(folder_path) -> None:
    """
    Convert all .ipynb files in a folder to Python files.
    
    Args:
        folder_path (str or Path): Path to the folder containing .ipynb files
    """
    # Convert to Path object if it's a string
    folder_path = Path(folder_path)
    
    # Validate input folder
    if not folder_path.exists():
        raise FileNotFoundError(f"Folder not found: {folder_path}")
    
    if not folder_path.is_dir():
        raise ValueError("Input must be a folder/directory")
    
    # Find all .ipynb files in the folder
    notebook_files = list(folder_path.glob('*.ipynb'))
    
    if not notebook_files:
        print(f"No .ipynb files found in {folder_path}")
        return
    
    print(f"Found {len(notebook_files)} notebook file(s) in {folder_path}")
    
    # Convert each notebook
    for notebook_file in notebook_files:
        try:
            convert_notebook_to_python(notebook_file)
        except Exception as e:
            print(f"Error processing {notebook_file}: {str(e)}")


def main():
    """Main function to handle command line arguments."""
    parser = argparse.ArgumentParser(
        description="Convert Jupyter notebook (.ipynb) to Python (.py) file. "
                    "Accepts either a single .ipynb file or a directory containing .ipynb files.")
    parser.add_argument(
        'input_path',
        help='Path to a .ipynb file or a directory containing .ipynb files'
    )
    
    args = parser.parse_args()
    input_path = Path(args.input_path)
    
    # Check if input is a directory or a file
    if input_path.is_dir():
        convert_notebooks_in_folder(input_path)
    elif input_path.is_file():
        if not input_path.suffix == '.ipynb':
            raise ValueError("Input file must be a .ipynb file")
        convert_notebook_to_python(input_path)
    else:
        raise FileNotFoundError(f"Path not found: {input_path}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(100)
