#!/usr/bin/env python3
"""
Module for converting CSV data to JSON format
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert CSV data to JSON and write to data.json
    
    Args:
        csv_filename: name of the CSV file to convert
        
    Returns:
        bool: True if conversion was successful, False otherwise
    """
    try:
        # Read CSV file and convert to list of dictionaries
        with open(csv_filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]
        
        # Serialize to JSON and write to file
        with open('data.json', mode='w') as json_file:
            json.dump(data, json_file, indent=4)
        
        return True
    except FileNotFoundError:
        return False
