from collections import defaultdict


def hospital_frequency_check(bills):
    hospital_count = defaultdict(int)

    for bill in bills:
        hospital_count[bill["hospital"]] += 1

    suspicious = []

    for hospital, count in hospital_count.items():
        if count > 10:
            suspicious.append((hospital, count))

    return suspicious


def recommend_cheapest_hospital(bills):
    """
    Compare cost of same treatment across hospitals
    and recommend lowest cost option.
    """

    treatment_costs = defaultdict(list)

    # Group by treatment
    for bill in bills:
        treatment_costs[bill["treatment"]].append(
            (bill["hospital"], bill["amount"])
        )

    recommendations = {}

    for treatment, records in treatment_costs.items():
        cheapest = min(records, key=lambda x: x[1])
        recommendations[treatment] = {
            "recommended_hospital": cheapest[0],
            "cost": cheapest[1]
        }

    return recommendations
