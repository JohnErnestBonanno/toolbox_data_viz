# %% [markdown]
# # Seaborn + Interactive Window proof of concept
# Run each cell with Shift+Enter (or click "Run Cell" above the `# %%` line).

# %%
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")
tips = sns.load_dataset("tips")  # needs internet on first run
tips.head()

# %%
# Tip amount vs. total bill, colored by time of day, sized by party size
plt.figure(figsize=(8, 5))
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time", size="size")
plt.title("Tip vs. Total Bill")
plt.show()

# %%
# Average tip percentage by day and smoker status
tips["tip_pct"] = tips["tip"] / tips["total_bill"] * 100

plt.figure(figsize=(8, 5))
sns.barplot(data=tips, x="day", y="tip_pct", hue="smoker")
plt.title("Average Tip % by Day")
plt.ylabel("Tip (%)")
plt.show()

# %%
# Variables persist between cells, so you can keep exploring interactively
tips.groupby("day")["tip_pct"].describe()