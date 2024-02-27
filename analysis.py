#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 16:27:18 2023

@author: denizaycan
"""
#Part 4: Analysis 
import os
import json
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
from mpl_toolkits.axes_grid1 import make_axes_locatable
from datetime import datetime
import wbdata
from country_converter import CountryConverter
import requests
import xml.etree.ElementTree as ET
import pycountry
from pypdf import PdfReader
import re
import statsmodels.api as sm
from linearmodels.panel import PanelOLS
import sklearn
from sklearn.feature_extraction.text import TfidfTransformer
from wordcloud import WordCloud
import nltk
from matplotlib.ticker import ScalarFormatter

original_data_path = r'/users/denizaycan/Documents/GitHub/final-project-deniz/data/unmodified'
final_data_path = r'/users/denizaycan/Documents/GitHub/final-project-deniz/data/final'

def load_andprep_excel_data(base_path, file_name):
    '''
    This function loads and prepares the excel file by removing extra lines.
    Arguments: base_path (str)
               file_name (str) 
    Returns the df.           
    '''
    full_path = os.path.join(base_path, file_name)
    df = pd.read_excel(full_path)
    return df

plot_merge = load_andprep_excel_data(final_data_path, 'plot_merge_final.xlsx')
OECD = load_andprep_excel_data(final_data_path, 'OECD_final.xlsx')
panel3 = load_andprep_excel_data(final_data_path, 'panel3_final.xlsx')
panel3.rename(columns={'Colonial Total/GtCO2': 'Colonial_Total_GtCO2'}, inplace=True)

def run_panel_regression(data, dependent_var, independent_vars, entity_effects=True, time_effects=True):
    df = data.copy()
    
    # Convert specified columns to numeric and handle missing values
    all_vars = [dependent_var] + independent_vars
    df[all_vars] = df[all_vars].apply(pd.to_numeric, errors='coerce')
    df = df.dropna(subset=all_vars)
    print(df)
    df.reset_index(inplace=True)
    
    # Build formula string
    formula = f"{dependent_var} ~ {' + '.join([f'`{var}`' for var in independent_vars])}"
    
    # Include EntityEffects and TimeEffects if specified
    if entity_effects:
        formula += " + EntityEffects"
    if time_effects:
        formula += " + TimeEffects"
    
    try:
        # Run Panel OLS regression
        mod = PanelOLS.from_formula(formula, df.set_index(['countrycode', 'Year']))
        results = mod.fit(cov_type='clustered', cluster_entity=True)
        return results
    except ValueError as e:
        print(f"Error: {e}")
        return None

# Specify the dependent variable, independent variables, and DataFrame
dependent_variable = 'GDP_ppp'
independent_variables = ['Colonial_Total_GtCO2', 'Emissions', 'Independent', 'LEV2_INT_C_COORD',  'Empire Total/GtCO2']

results = run_panel_regression(panel3, dependent_variable, independent_variables)
print(results)
#result 1 = GDP per capita is positively associated with state's colonial emissions, independency and the international cooperation score.


dep = 'Emissions'
indep = ['Independent', 'GDP_ppp']
results2 = run_panel_regression(panel3, dep, indep)
print(results2)
#result 2 = Emissions are positively associated by independency of the state.

dep = 'LEV1_INT'
indep = ['Independent', 'GDP_ppp', 'Colonial_Total_GtCO2']
results3 = run_panel_regression(panel3, dep, indep)
print(results3)

#result 3 = nothing is significant

