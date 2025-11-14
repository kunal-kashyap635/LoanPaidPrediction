import joblib
import pandas as pd

# Load the saved sklearn pipeline
model_path = "model/loan_model_lgbm.pkl"
model = joblib.load(model_path)

def predict_loan_status(data_dict):
    """
    data_dict = dictionary from FastAPI form
    Convert to pandas DataFrame because sklearn Pipeline expects DataFrame columns.
    """
    # Convert dict → DataFrame
    input_df = pd.DataFrame([data_dict])

    # Predict
    prediction = model.predict(input_df)[0]

    return int(prediction)
