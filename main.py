import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

folder_path = '/Users/aayushkumbhare/Desktop/disease_spread/csse_covid_19_data/csse_covid_19_daily_reports_us'
all_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.csv')]
combined_data = pd.concat([pd.read_csv(file) for file in all_files], ignore_index=True)
combined_data.to_csv('combined_covid_data.csv', index=False)


print(combined_data)