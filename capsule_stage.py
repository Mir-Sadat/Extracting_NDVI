import pandas as pd

# Path to your extracted NDVI CSV
file_path = r'C:\Users\Mir\Desktop\ndvi_all_extracted.csv'

# Load the CSV
df = pd.read_csv(file_path)

# Filter rows where NDVI is in capsule stage range (0.65 to 0.75)
capsule_ndvi = df[(df['NDVI'] >= 0.65) & (df['NDVI'] <= 0.75)]

# Print the filtered NDVI values (with Filename and Pixel_Index)
print("NDVI values corresponding to Opium Capsule Stage (0.65 - 0.75):")
print(capsule_ndvi[['Filename', 'Pixel_Index', 'NDVI']])
