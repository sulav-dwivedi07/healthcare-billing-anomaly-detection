import os
import pandas as pd
from src.ingestion.data_loader import load_data, split_data
from src.core.preprocessing import create_preprocessor
from src.core.model import get_model
from src.pipeline.train_pipeline import train_model


def main():
    target_column = "Treatment_Cost"

    df = load_data()

    print("Dataset columns:", df.columns.tolist())

    X_train, X_test, y_train, y_test = split_data(df, target_column)


    numerical_features = ["Age", "Severity"]
    categorical_features = ["Gender", "Diagnosis", "Procedure"]

    preprocessor = create_preprocessor(numerical_features, categorical_features)

    model = get_model()

    trained_pipeline = train_model(
        preprocessor,
        model,
        X_train,
        y_train,
        X_test,
        y_test
    )

   
    sample_input = [[45, 3, "Male", "Cancer", "Surgery"]]

    sample_df = pd.DataFrame(
        sample_input,
        columns=["Age", "Severity", "Gender", "Diagnosis", "Procedure"]
    )

    prediction = trained_pipeline.predict(sample_df)
    print("Predicted Treatment Cost:", prediction[0])


if __name__ == "__main__":
    main()
