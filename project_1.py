import pandas as pd 
import numpy as np
import seaborn as sns 
import matplotlib as plt

# Then we import all the datasets (This dataset is imported from kaggle named as "Agricultural dataset for rajasthan" owner-suraj)
price=pd.read_csv("datasets\crop_price_data.csv")
production=pd.read_csv("datasets\crop_production_data.csv")
sad=pd.read_csv("datasets\soil_analysis_data.csv")
water_usage=pd.read_csv("datasets\water_usage_data.csv")