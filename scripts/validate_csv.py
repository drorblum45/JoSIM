#!/usr/bin/env python3
"""
CSV validation script for JoSIM simulation output.
Checks if the last line of the CSV file contains only positive numeric values.
"""

import csv
import sys
import os
import argparse

def validate_csv_last_line(csv_file_path):
    """
    Validate that the last line of a CSV file contains only positive numeric values.
    
    Args:
        csv_file_path (str): Path to the CSV file to validate
        
    Returns:
        bool: True if validation passes, False otherwise
    """
    if not os.path.exists(csv_file_path):
        print(f'Error: CSV file not found: {csv_file_path}')
        return False

    try:
        with open(csv_file_path, 'r') as f:
            lines = list(csv.reader(f))
            if not lines:
                print('Error: CSV file is empty')
                return False
            
            last_line = lines[-1]
            print(f'Last line values: {last_line}')
            
            # Extract numeric values from last line
            numeric_values = []
            for value in last_line:
                try:
                    num_val = float(value)
                    numeric_values.append(num_val)
                except ValueError:
                    continue  # Skip non-numeric values
            
            if not numeric_values:
                print('Error: No numeric values found in last line')
                return False
            
            positive_values = [v for v in numeric_values if v > 0]
            print(f'Found {len(positive_values)} positive values out of {len(numeric_values)} numeric values')
            
            if len(positive_values) == len(numeric_values):
                print('SUCCESS: All numeric values in last line are positive')
                return True
            else:
                print(f'FAILURE: Only {len(positive_values)}/{len(numeric_values)} values are positive')
                negative_values = [v for v in numeric_values if v <= 0]
                print(f'Non-positive values: {negative_values}')
                return False
                
    except Exception as e:
        print(f'Error processing CSV file: {e}')
        return False

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Validate CSV simulation output')
    parser.add_argument('csv_file', help='Path to the CSV file to validate')
    
    args = parser.parse_args()
    
    success = validate_csv_last_line(args.csv_file)
    sys.exit(0 if success else 1)