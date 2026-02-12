from src.data.database import initialize_database, get_connection
from src.core.parser import parse_csv
from src.core.anomalies import analyze_bills
from src.core.graph_rules import (
    hospital_frequency_check,
    recommend_cheapest_hospital
)


def store_bills(bills):
    """
    Store parsed bills into SQLite database
    """
    conn = get_connection()
    cursor = conn.cursor()

    for bill in bills:
        cursor.execute("""
        INSERT INTO bills (patient_name, hospital, treatment, amount, date)
        VALUES (?, ?, ?, ?, ?)
        """, (
            bill["patient_name"],
            bill["hospital"],
            bill["treatment"],
            bill["amount"],
            bill["date"]
        ))

    conn.commit()
    conn.close()


def run_pipeline(csv_path):
    

    # Step 1: Initialize Database
    print(" Initializing database")
    initialize_database()

    # Step 2: Parse CSV
    print(" Parsing bills")
    bills = parse_csv(csv_path)

    if not bills:
        print(" No bills found")
        return

    # Step 3: Store in DB
    print(" Storing bills in database")
    store_bills(bills)

    # Step 4: Run Anomaly Detection
    print("\n Running anomaly detection")
    anomalies = analyze_bills(bills)

    if anomalies:
        print("\n⚠ Anomalies Found:")
        for anomaly_type, bill in anomalies:
            print(f"\nType: {anomaly_type}")
            print(f"Patient: {bill['patient_name']}")
            print(f"Hospital: {bill['hospital']}")
            print(f"Treatment: {bill['treatment']}")
            print(f"Amount: ₹{bill['amount']}")
            print(f"Date: {bill['date']}")
    else:
        print(" No anomalies detected.")

    # Step 5: Graph-Based Hospital Frequency Check
    print("\n Checking hospital frequency patterns...")
    suspicious_hospitals = hospital_frequency_check(bills)

    if suspicious_hospitals:
        print("\n Suspicious Hospitals (High Billing Volume):")
        for hospital, count in suspicious_hospitals:
            print(f"{hospital} -> {count} bills")
    else:
        print(" No suspicious hospital frequency detected.")

    # Step 6: Cost Optimization Recommendation
    print("\n Cost Optimization Recommendations:")
    recommendations = recommend_cheapest_hospital(bills)

    for treatment, info in recommendations.items():
        print(f"For {treatment}, choose {info['recommended_hospital']} "
              f"(Cost: ₹{info['cost']})")

  
