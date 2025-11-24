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
        notebook_path (str): Path to the .ipynb file
    
    Returns:
        str: Path to the created .py file
    """
    # Validate input file
    if not os.path.exists(notebook_path):
        raise FileNotFoundError(f"Notebook file not found: {notebook_path}")
    
    if not notebook_path.endswith('.ipynb'):
        raise ValueError("Input file must be a .ipynb file")
    
    # Create output file path
    notebook_path = Path(notebook_path)
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
                code_lines.append(line)

            # Add empty line between cells
            code_lines.append('')

    # Write to Python file
    with open(output_path, 'w', encoding='utf-8') as f:
        for line in code_lines:
            f.write(line + '\n')

    print(f"Successfully converted {notebook_path} to {output_path}")



def main():

    """Main function to handle command line arguments."""
    parser = argparse.ArgumentParser(
        description="Convert Jupyter notebook (.ipynb) to Python (.py) file")
    parser.add_argument(
        'notebook_file',
        help='Path to the .ipynb file to convert'
    )
    
    args = parser.parse_args()
    convert_notebook_to_python(args.notebook_file)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(100)
