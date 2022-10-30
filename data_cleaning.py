import pandas as pd
import numpy as np
from ast import literal_eval


def clean_tabular_data(df):
    return (df.rename(columns=dict(zip(df.columns, df.columns.str.lower())))
                .assign(category = lambda df_: df_.category.astype('category'),
                        description = lambda df_: df_.description.str.replace("\'\', ", '')
                                                        .apply(lambda x: ' '.join(literal_eval(x)[1:]) if str(x) != 'nan' else x))
                .dropna(axis=0, subset=['cleanliness_rate', 'description'])
                .assign(guests = lambda df_: df_.guests.fillna(1),
                        beds = lambda df_: df_.beds.fillna(1),
                        bathrooms = lambda df_: df_.bathrooms.fillna(1),
                        bedrooms = lambda df_: df_.bedrooms.fillna(1))
    )