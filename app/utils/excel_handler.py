import pandas as pd

def load_licenses(file_path):
    df = pd.read_excel(file_path)
    return df

def save_classified_licenses(df, output_path='data/output.xlsx'):
    df.to_excel(output_path, index=False)
