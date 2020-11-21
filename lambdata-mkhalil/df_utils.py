import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

def add_state_names__columns(my_df):
    """
    Add a column of corresponding names to a dataframe

    Params: (my_df) a Dataframe with a column called abbrev that has state abbreviation.
    
    return: a copy of the original dataframe, but with an extra column
    """

    new_df = my_df.copy()
    names_map = {"CA":"Cali","CO":"Colo","CT":"Conn"}

    # breakpoint()
    new_df["name"] = new_df["abbrev"].map(names_map)

    return new_df

if __name__ == '__main__':
    df = pd.DataFrame({"abbrev": ["CA","CO","CT","DC","TX"]})
    print(df.head())
    mapped_df = add_state_names__columns(df)
    print(mapped_df.head())