import pandas as pd 
from PIL import Image
import json

if __name__ == "__main__":
    df = pd.read_csv("dataset.csv")
    print(df.head())

    print(df.loc[0][-2][0])