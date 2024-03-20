import pandas as pd

def clean_merged_data(input_file, output_file):
    merged_data = pd.read_csv(input_file, dtype={'name': str, 'email': str, 'phone': str, 'city': str})
    
    merged_data = merged_data[['name', 'email', 'phone', 'city']]
    
    merged_data.dropna(inplace=True)
    
    merged_data.to_csv(output_file, index=False)
    print("Cleaned data saved to", output_file)

input_file = "old_data/Paytm Mall Onlin shoping New.csv"
output_file = "new/data13.csv"

clean_merged_data(input_file, output_file)
