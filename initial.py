# import the necessary libraries
import pandas as pd 


df = pd.read_excel(
    io='supermarkt_sales.xlsx',
    engine='openpyxl',
    sheetName = 'Sales',
    skiprows=3,
    usecols='B:R',
    nrows=1000,
)

