from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, r2_score
import numpy as np
import joblib
import os


def train_model(preprocessor, model, X_train, y_train, X_test, y_test):
    # Create pipeline
    pipeline = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ])

    # Train
    pipeline.fit(X_train, y_train)

    # Predict
    predictions = pipeline.predict(X_test)

    # Metrics
    mae = mean_absolute_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    rmse = np.sqrt(((y_test - predictions) ** 2).mean())

    print("Model Evaluation:")
    print("MAE:", mae)
    print("RMSE:", rmse)
    print("R2 Score:", r2)

    # -------------------------
    # Save trained model
    # -------------------------

    # Get Backend root directory safely
    base_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../")
    )

    # Create folder if it doesn't exist
    model_dir = os.path.join(base_dir, "saved_models")
    os.makedirs(model_dir, exist_ok=True)

    # Model file path
    model_path = os.path.join(model_dir, "treatment_cost_model.pkl")

    # Save model
    joblib.dump(pipeline, model_path)

    print("Model saved at:", model_path)

    return pipeline
