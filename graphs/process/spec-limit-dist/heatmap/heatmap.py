import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sborn

sborn.set(font_scale=2.0)


work_dir = "~/Documents/papers/yzu-18-atm_cloud/graphs/spec-limit-dist/heatmap/"

all_info = pd.read_csv(work_dir +  "app_summary.csv", sep="\t")
all_info = all_info[::-1]

row_labels = all_info['application'].tolist()

all_info = all_info.drop(['application'], axis = 1)
column_labels = all_info.columns.values.tolist()

print row_labels
print column_labels

try:
	# sborn.heatmap(all_info.values, cmap="YlGnBu", linewidths=0.5, 
	# 	xticklabels=column_labels, yticklabels = row_labels)
	sborn.heatmap(all_info.values, cmap="YlOrRd", linewidths=0.5, 
		xticklabels=column_labels, yticklabels = row_labels)

except:
	pass

plt.xticks(rotation=90) 
plt.yticks(rotation=0) 
plt.show()

# flights = sborn.load_dataset(work_dir +  "app_summary.csv")
# flights = flights.pivot("Application", "Core", "Rollback")
# ax = sborn.heatmap(flights)