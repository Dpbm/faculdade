import jax
import jax.numpy as jnp
import polars as pl

FILE = "titanic.csv"

df = pl.scan_csv(FILE).collect()

n_rows = len(df)

p_train = 0.8

total_train = int(p_train*n_rows)
total_test = n_rows - total_train

train = df.head(total_train)
test = df.tail(total_test)

print(test.describe())

label = 
classes = ("")
