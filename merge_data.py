import pandas as pd
import numpy as np

# Read in the two CSV files
houses_df = pd.read_csv('house_data_final.csv')
houses_df['ZIP'] = houses_df['ZIP'].astype(float)
shootings_df = pd.read_csv('los_angeles_shootings.csv')
shootings_df = shootings_df.drop_duplicates(subset=['ZIP'])
shootings_df['ZIP'] = shootings_df['ZIP'] .replace([np.inf, -np.inf], np.nan)
shootings_df['ZIP'] = shootings_df['ZIP'].astype(float)

# Merge the two dataframes on the 'ZIP' field
merged_df = pd.merge(shootings_df, houses_df, on='ZIP',how='inner')
# Only keep the specified columns
merged_df = merged_df[['X', 'Y', 'ZIP', 'shooting_num','Price']]
# Increment the 'shooting_num' column by the number of duplicates minus 1
duplicates = merged_df.duplicated(subset='ZIP', keep=False)
# import pdb; pdb.set_trace()
merged_df.loc[duplicates, 'shooting_num'] += duplicates.groupby(merged_df['ZIP']).cumsum() - 1

# Drop duplicates based on the 'postal_code' field
merged_df.drop_duplicates(subset='ZIP', keep='last', inplace=True)

# Save the merged dataframe as a new CSV file
merged_df.to_csv('los_angeles_house_shooting.csv', index=False)
