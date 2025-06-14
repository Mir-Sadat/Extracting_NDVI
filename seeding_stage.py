import pandas as pd

# Path to your CSV file
file_path = r'C:\Users\Mir\Desktop\ndvi_all_extracted.csv'

# Load CSV
df = pd.read_csv(file_path)

# Filter rows where NDVI is in seeding stage range (0.30 to 0.45)
seeding_ndvi = df[(df['NDVI'] >= 0.30) & (df['NDVI'] <= 0.45)]

# Print the filtered NDVI values with Filename and Pixel_Index
print("NDVI values corresponding to Opium Seeding Stage (0.30 - 0.45):")
print(seeding_ndvi[['Filename', 'Pixel_Index', 'NDVI']])
