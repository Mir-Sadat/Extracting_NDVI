import os
import rasterio
import pandas as pd
import numpy as np

# Path to the directory containing NDVI .tif images
images_dir = r'C:\Users\your user name\Desktop\images'

# Prepare a list to collect NDVI data
ndvi_data = []

# Loop through all .tif files in the directory
for filename in os.listdir(images_dir):
    if filename.lower().endswith('.tif'):
        file_path = os.path.join(images_dir, filename)
        
        with rasterio.open(file_path) as src:
            ndvi_array = src.read(1)  # Assuming single-band NDVI image
            
            # Flatten array and filter out no-data values (e.g. nan or -9999)
            ndvi_flat = ndvi_array.flatten()
            mask = np.isfinite(ndvi_flat)
            valid_ndvi = ndvi_flat[mask]

            for idx, value in enumerate(valid_ndvi):
                ndvi_data.append({
                    'Filename': filename,
                    'Pixel_Index': idx,
                    'NDVI': value
                })

# Convert to DataFrame
df = pd.DataFrame(ndvi_data)

# Save to CSV
output_csv = r'C:\Users\Mir\Desktop\ndvi_values.csv'
df.to_csv(output_csv, index=False)

print(f"NDVI values extracted and saved to: {output_csv}")
