import pandas as pd
import numpy as np

def get_distance(row, target):
    rsl = row['sl']
    rsw = row['sw']
    rpl = row['pl']
    rpw = row['pw']
    
    tsl = target['sl']
    tsw = target['sw']
    tpl = target['pl']
    tpw = target['pw']

    return np.sqrt( (rsl-tsl)**2 + (rsw-tsw)**2 + (rpl-tpl)**2 + (rpw-tpw)**2)

if __name__ == "__main__":
    data = pd.read_csv('iris.data', sep=",", names=("sl", "sw", "pl", "pw", "species"), header=None)

    target_i = np.random.randint(0,len(data))
    target = data.take([target_i])


    data['distance'] = data.apply(lambda x : get_distance(x,target), axis=1)
    data = data.drop(target_i)
    data = data.sort_values(by=["distance"])

    k = 3

    neighbours_species = data.head(k)['species'].value_counts().to_dict()
    predicted_species,total_neighbours= max(neighbours_species.items(), key=lambda x : x[-1])

    actual_species = target["species"].values[0]

    print(f"predicted species: {predicted_species}; with {total_neighbours} neighbours")
    print(f"actual species: {actual_species}")
    
