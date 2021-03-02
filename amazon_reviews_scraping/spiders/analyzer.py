import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("reviews.csv")
summarised_results = df["stars"].value_counts()
plt.bar(summarised_results.keys(), summarised_results.values)
plt.show()