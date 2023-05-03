import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

#load the CSV file into a dataframe
df = pd.read_csv('image_data.csv')

#calculate the aspect ratio of the original image
num_rows, num_cols = df.shape
aspect_ratio= num_cols/num_rows

#set the figure size with the original aspect ratio
fig, ax = plt.subplots(figsize=(10, 10 / aspect_ratio), dpi=300)

#create the heatmap plot using seaborn
heatmap = sns.heatmap(df, cmap='gray', cbar=False)

#remove the ticks and tick labels on the side of the heatmap
heatmap.set_yticks([])
heatmap.set_xticks([])
heatmap.set_yticklabels([])
heatmap.set_xticklabels([])

#save the plot with high quality
heatmap.figure.savefig('heatmap_high_quality2.png', bbox_inches='tight', dpi=300)