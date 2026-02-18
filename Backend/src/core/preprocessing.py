from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

def create_preprocessor(numerical_features, categorical_features):
    return ColumnTransformer(
        transformers=[
            ("num", "passthrough", numerical_features),
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
        ]
    )
