#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 16:24:37 2020

@author: arjun
"""

import csv
import sys

def dictionary_read(filename):
    """ Reads the input data file in csv format and returns a list of dictionaries.
    
    Arguments:
        filename : The csv file containing consumer complaint data.

    Returns:
        List of dictionaries. 
    """
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)                    
        data = list(reader)
    return data

def parse_date_for_year(complaint):
    """ Reads the input data, parses the year data and makes a key of year.

    Arguments:
    complaint : List of dictionaries of complaints.

    Returns:
    List of dictionaries containing year key.
    """
    complaint['year'] = int(complaint['Date received'].split('-')[0])
    return complaint

def get_unique_year(data):
    """ Reads the input data, and gets unique years in data.

    Arguments:
    data : List of dictionaries of complaints.

    Returns:
    Unique years in data.
    """    
    unique_years = sorted(set([d['year'] for d in data]))
    return unique_years
    
def get_unique_product(data):
    """ Reads the input data, and gets unique products in data.

    Arguments:
    data : List of dictionaries of complaints.

    Returns:
    Unique products in data.
    """ 
    unique_product = sorted(set([d['Product'] for d in data]))
    return unique_product

def get_unique_companies(data):
    """ Reads the input data, and gets unique companies in data.

    Arguments:
    data : List of dictionaries of complaints.

    Returns:
    Unique products in data.
    """
    unique_companies = sorted(set([d['Company'] for d in data]))
    return unique_companies

def get_data_for_company(company, data):
    """ Reads the input data and unique companies and returns number of companies in data.

    Arguments:
    data : List of dictionaries of complaints and unique companies.

    Returns:
    Number of complaints per company per product per year.
    """
    company_data = [d for d in data if d['Company'] == company]
    return company_data

def write_file(data, filename):
    """ Reads the input data and unique companies and returns number of companies in data.

    Arguments:
    data : List of dictionaries of complaints and unique companies.

    Returns:
    Companies in data.
    """
    data_to_write = [[d['Product'], d['Year'], d['Num_complaints'], d['Num_companies_with_complaints'], d['Percent_complaints'] ] for d in data]
    with open(filename, 'w') as write_it:
        writer = csv.writer(write_it)
        writer.writerows(data_to_write)

def process_complaints(data, years, products):
    """ Reads the input data, unique years and products .

    Arguments:
    data : List of dictionaries of containing complaint data, unique years and products in data .

    Returns:
    List of dictionaries containing financial product and year, the total number of complaints, number of companies 
    receiving a complaint, and the highest percentage of complaints directed at a single company.
    """
    output = []
    for p in products_in_data:
        product_data = [d for d in complaints_with_year if d['Product']==p]
        for y in years_in_data:
            product_year_data = [d for d in product_data if d['year']==y]
            num_complaints = len(product_year_data)
            companies = get_unique_companies(product_year_data)
            num_companies_with_complaints = len(companies)
            company_complaints = [len(get_data_for_company(c, product_year_data)) for c in companies]
            if num_complaints != 0:
                max_num_complaints = max(company_complaints)
                percent_complaints = 100 * max_num_complaints / num_complaints
            else:
                continue
            output_by_year = [{
                'Product': p.lower(),
                'Year': y,
                'Num_complaints': num_complaints,
                'Num_companies_with_complaints': num_companies_with_complaints,
                'Percent_complaints': percent_complaints,
                }] 
            output.extend(output_by_year)
    return output
     
if __name__ == '__main__':
    inputfile = sys.argv[1]
    outputfile =  sys.argv[2]
    complaints = dictionary_read(inputfile) #'complaints.csv')
    complaints_with_year = [parse_date_for_year(complaint) for complaint in complaints]
    years_in_data = get_unique_year(complaints_with_year)
    products_in_data = get_unique_product(complaints_with_year)
    results = process_complaints(complaints_with_year, years_in_data, products_in_data)
    write_file(results, outputfile) # 'report.csv')


 
