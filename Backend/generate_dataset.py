import pandas as pd
import numpy as np
import random

np.random.seed(42)

num_records = 2000


diagnoses = ["Flu", "Fracture", "Infection", "Diabetes", "Hypertension", "Surgery", "Cancer"]
procedures = ["Medication", "X-Ray", "MRI", "CT Scan", "Blood Test", "Surgery", "Therapy"]
genders = ["Male", "Female"]

data = []

for _ in range(num_records):
    age = np.random.randint(1, 90)
    gender = random.choice(genders)
    diagnosis = random.choice(diagnoses)
    procedure = random.choice(procedures)
    severity = np.random.randint(1, 6)

    base_cost = 5000
    age_factor = age * 50
    severity_factor = severity * 10000
    procedure_factor = procedures.index(procedure) * 8000
    diagnosis_factor = diagnoses.index(diagnosis) * 12000

    treatment_cost = base_cost + age_factor + severity_factor + procedure_factor + diagnosis_factor
    treatment_cost += np.random.normal(0, 5000)  # noise

    data.append([
        age,
        gender,
        diagnosis,
        procedure,
        severity,
        round(treatment_cost, 2)
    ])

df = pd.DataFrame(data, columns=[
    "Age",
    "Gender",
    "Diagnosis",
    "Procedure",
    "Severity",
    "Treatment_Cost"
])


df.to_csv("src/data/hospital_data.csv", index=False)

print("Dataset generated successfully with", num_records, "records.")
