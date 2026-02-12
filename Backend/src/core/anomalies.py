from src.config import ANOMALY_THRESHOLD


def detect_amount_anomaly(bill):
    if bill["amount"] > ANOMALY_THRESHOLD:
        return True
    return False


def detect_duplicate_bills(bills):
    seen = set()
    duplicates = []

    for bill in bills:
        key = (bill["patient_name"], bill["treatment"], bill["date"])
        if key in seen:
            duplicates.append(bill)
        else:
            seen.add(key)

    return duplicates


def analyze_bills(bills):
    anomalies = []

    for bill in bills:
        if detect_amount_anomaly(bill):
            anomalies.append(("High Amount", bill))

    duplicates = detect_duplicate_bills(bills)

    for dup in duplicates:
        anomalies.append(("Duplicate Bill", dup))

    return anomalies
