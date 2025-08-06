#!/usr/bin/env python3
import csv
import sys
import os
import argparse
import math

def validate_csv(csv_file_path, arg_name='B01', expected_value=2 * math.pi, tolerance=0.3):

    if not os.path.exists(csv_file_path):
        print(f'Error: CSV file not found: {csv_file_path}')
        return False

    try:
        with open(csv_file_path, 'r') as f:
            lines = list(csv.reader(f))
            if not lines:
                print('Error: CSV file is empty')
                return False
            
            # Find B01 column index
            header = lines[0]
            b01_index = next((i for i, col in enumerate(header) if arg_name in col.strip().upper()), None)

            if b01_index is None:
                print(f'Error: {arg_name} column not found in {header}')
                return False

            # Get B01 value from last line
            b01_value = float(lines[-1][b01_index])

            print(f'{arg_name} value: {b01_value:.6f}, expected value: {expected_value:.6f} ± {tolerance}')

            if abs(b01_value - expected_value) <= tolerance:
                print(f'SUCCESS: {arg_name} value is within acceptable range')
                return True
            else:
                print(f'FAILURE: {arg_name} value is outside acceptable range')
                return False
                
    except Exception as e:
        print(f'Error processing CSV file: {e}')
        return False

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Validate CSV simulation output')
    parser.add_argument('csv_file', help='Path to the CSV file to validate')
    parser.add_argument('--arg-name', type=str, default='B01', help='Name of the argument to validate')
    parser.add_argument('--expected-value', type=float, default=2 * math.pi, help='Expected end value for B0')
    parser.add_argument('--tolerance', type=float, default=0.3, help='Tolerance for validation')

    args = parser.parse_args()

    success = validate_csv(args.csv_file, arg_name=args.arg_name, expected_value=args.expected_value, tolerance=args.tolerance)
    sys.exit(0 if success else 1)