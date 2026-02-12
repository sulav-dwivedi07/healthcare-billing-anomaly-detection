import csv


def parse_csv(file_path):
    bills = []

    with open(file_path, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            bills.append({
                "patient_name": row["patient_name"],
                "hospital": row["hospital"],
                "treatment": row["treatment"],
                "amount": float(row["amount"]),
                "date": row["date"]
            })

    return bills
