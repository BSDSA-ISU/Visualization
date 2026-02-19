import pandas as pd

df = pd.read_csv("data cleaning/Lab Activity 2.csv")

df["author"] = (
    df["author"]
    .str.replace(r"^Writtenby:", "", regex=True)
    .str.replace(r"([a-z])([A-Z])", r"\1 \2", regex=True)
)

df["narrator"] = (
    df["narrator"]
    .str.replace(r"^Narratedby:", "", regex=True)
    .str.replace(r"([a-z])([A-Z])", r"\1 \2", regex=True)
)

time_parts = df["time"].str.extract(r"(?:(\d+)\s*hr)?s?\s*(?:and\s*)?(?:(\d+)\s*min)?s?")

time_parts = time_parts.astype(float).fillna(0)

df["time_minutes"] = time_parts[0]*60 + time_parts[1]

df["time"] = df["time_minutes"].astype(int)

df["Stars"] = (
    df["stars"]
    .str.extract(r"^\s*(\d+(?:\.\d+)?)") 
    .astype(float)
    .fillna(0)
)

df["ratings"] = (
    df["stars"]
    .str.extract(r"(\d+)\s*ratings") 
    .astype(float)
    .fillna(0)
    .astype(int)
)

print(df["stars"])

df = df.drop("stars", axis=1)

print(df.head(8))

df.to_csv("./cleanedLabactivity2.csv", index=False)
df.to_excel("./cleanedLabactivity2.xlsx", index=False)