import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# LOAD DATA
# -----------------------------
# Change file paths as per your system
shootings = pd.read_csv("police_shootings.csv")
census = pd.read_csv("us_census.csv")

# -----------------------------
# CLEAN DATA
# -----------------------------
shootings["date"] = pd.to_datetime(shootings["date"], errors='coerce')
shootings["year"] = shootings["date"].dt.year

# Drop missing values
shootings = shootings.dropna(subset=["race", "state"])

# -----------------------------
# 1. SHOOTINGS PER YEAR
# -----------------------------
shootings_per_year = shootings.groupby("year").size()

plt.figure()
shootings_per_year.plot()
plt.title("Police Shootings Per Year")
plt.xlabel("Year")
plt.ylabel("Number of Shootings")
plt.show()

# -----------------------------
# 2. SHOOTINGS BY RACE
# -----------------------------
plt.figure()
shootings["race"].value_counts().plot(kind="bar")
plt.title("Police Shootings by Race")
plt.xlabel("Race")
plt.ylabel("Count")
plt.show()

# -----------------------------
# 3. SHOOTINGS BY STATE
# -----------------------------
plt.figure()
shootings["state"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 States with Most Shootings")
plt.xlabel("State")
plt.ylabel("Count")
plt.show()

# -----------------------------
# 4. MERGE WITH CENSUS DATA
# -----------------------------
# Assuming both have 'state' column
merged = shootings.merge(census, on="state", how="left")

# -----------------------------
# 5. POVERTY VS SHOOTINGS
# -----------------------------
if "poverty_rate" in merged.columns:
    poverty_shootings = merged.groupby("poverty_rate").size()

    plt.figure()
    poverty_shootings.plot()
    plt.title("Poverty Rate vs Shootings")
    plt.xlabel("Poverty Rate")
    plt.ylabel("Shootings")
    plt.show()

# -----------------------------
# PRINT INSIGHTS
# -----------------------------
print("\n--- KEY INSIGHTS ---")

print("Total Shootings:", len(shootings))

print("\nMost Affected Race:")
print(shootings["race"].value_counts().idxmax())

print("\nState with Most Shootings:")
print(shootings["state"].value_counts().idxmax())

if "poverty_rate" in merged.columns:
    print("\nHigher poverty areas tend to show more incidents.")