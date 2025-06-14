import pandas as pd

# Path to your CSV file
file_path = r'C:\Users\Mir\Desktop\ndvi_all_extracted.csv'

# Load the CSV file
df = pd.read_csv(file_path)

# Filter rows where NDVI is in flowering stage range (0.46 to 0.65)
flowering_ndvi = df[(df['NDVI'] >= 0.46) & (df['NDVI'] <= 0.65)]

# Print the filtered NDVI values with Filename and Pixel_Index
print("NDVI values corresponding to Opium Flowering Stage (0.46 - 0.65):")
print(flowering_ndvi[['Filename', 'Pixel_Index', 'NDVI']])
