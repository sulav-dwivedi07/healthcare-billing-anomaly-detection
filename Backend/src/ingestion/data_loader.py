import pandas as pd
from sklearn.model_selection import train_test_split
import os
def load_data():
    # Get Backend directory
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    
    # Correct dataset location
    file_path = os.path.join(base_path, "src", "data", "hospital_data.csv")

    df = pd.read_csv(file_path)
    print("Dataset loaded successfully:", df.shape)
    return df



def split_data(df, target_column):
    X = df.drop(columns=[target_column])
    y = df[target_column]

    return train_test_split(X, y, test_size=0.2, random_state=42)
