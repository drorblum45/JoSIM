#!/usr/bin/env python3
import csv
import sys
import os
import argparse
import math

def validate_B0_end_value(csv_file_path, expected_value=2 * math.pi, tolerance=0.3):

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
            b01_index = next((i for i, col in enumerate(header) if col.strip().upper() == 'B01'), None)

            if b01_index is None:
                print(f'Error: B01 column not found in {header}')
                return False

            # Get B01 value from last line
            b01_value = float(lines[-1][b01_index])

            print(f'B01 value: {b01_value:.6f}, expected value: {expected_value:.6f} ± {tolerance}')

            if abs(b01_value - expected_value) <= tolerance:
                print('SUCCESS: B01 value is within acceptable range')
                return True
            else:
                print('FAILURE: B01 value is outside acceptable range')
                return False
                
    except Exception as e:
        print(f'Error processing CSV file: {e}')
        return False

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Validate CSV simulation output')
    parser.add_argument('csv_file', help='Path to the CSV file to validate')
    parser.add_argument('--expected-value', type=float, default=2 * math.pi, help='Expected end value for B0')
    parser.add_argument('--tolerance', type=float, default=0.3, help='Tolerance for validation')

    args = parser.parse_args()

    success = validate_B0_end_value(args.csv_file, args.expected_value, args.tolerance)
    sys.exit(0 if success else 1)