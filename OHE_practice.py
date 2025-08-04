import numpy as np
import pandas as pd


# Problems:


# Problem 1:

# right now new unique values in a column will break the UnicodeEncodeError
# eg if we encode the training set, and then encounter a new unique value in the test,
# then the encoder wont work

# Probelm 1 fix:
# 
# Turn the the encoder into a class, and then create a fit
# and a hadle nan feature.









###
# use this code to generate dummy categorical data
# cat_data = generate_cat_data()
###




def generate_cat_data(n_rows = 30,n_cols = 3):

    # n_cols = 10
    # n_rows = 10
    
    cat_data = pd.DataFrame(np.random.randint(5,size = (n_rows,n_cols)).astype(str))
    
    
    column_names = {}
    
    for i in range(n_cols):
    
        column_names[i] = 'cat' + f'{i}'

    cat_data.rename(columns = column_names,inplace = True)
    
    
    
    return cat_data


def ohe_col(col):

    # col = 'cat'
    
    one_hot_encoder = {}
    
    
    unique_vals = cat_data[col].unique()
    
    num_unique = len(unique_vals)
    
    # enc_cat_data = np.zeros((cat_data.shape[0] , num_unique))
    
    for i in range(num_unique):
    
        a = np.zeros(num_unique)
        a[i] = 1
    
        one_hot_encoder[unique_vals[i]] = a


    # null_array = np.zeros(num_unique+1)
    # null_array[num_unique] = 1

    

    

    df = pd.DataFrame(cat_data[col].map(one_hot_encoder).iloc[:].to_list())

    col_replace_names = {}

    for i in range(num_unique+1):

        col_replace_names[i] = col + f'_{i}'
    

    df.rename( columns = col_replace_names,inplace = True)
    
    return df

def ohe_enc_df(cat_data):

    encoded_cols = []
    
    
    for col in cat_data.columns:
    
        encoded_cols.append(ohe_col(col))
    
    
    
    
    
    return pd.concat(encoded_cols,axis = 1)

