# test_api.py
import requests
import json

BASE_URL = "http://localhost:5000"

print("=" * 70)
print("AI RISK MANAGER - API TEST")
print("=" * 70)

# Test 1: Health check
print("\n1️⃣ Health Check:")
resp = requests.get(f"{BASE_URL}/health")
print(json.dumps(resp.json(), indent=2))

# Test 2: Metrics
print("\n2️⃣ Model Metrics:")
resp = requests.get(f"{BASE_URL}/metrics")
print(json.dumps(resp.json(), indent=2))

# Test 3: Score HIGH-RISK transaction
print("\n3️⃣ Score HIGH-RISK Transaction:")
high_risk = {
    "transaction_id": "TXN-DEMO-001",
    "account_age_days": 5,
    "lifetime_orders": 1,
    "order_amount": 25000,
    "product_category": "electronics",
    "order_velocity_24h": 2,
    "previous_returns_count": 0,
    "payment_method": "credit_card",
    "ip_country_match": 1,
    "merchant_id": "razorpay_test"
}
resp = requests.post(f"{BASE_URL}/score", json=high_risk)
print(json.dumps(resp.json(), indent=2))

# Test 4: Score LOW-RISK transaction
print("\n4️⃣ Score LOW-RISK Transaction:")
low_risk = {
    "transaction_id": "TXN-DEMO-002",
    "account_age_days": 340,
    "lifetime_orders": 15,
    "order_amount": 850,
    "product_category": "books",
    "order_velocity_24h": 0,
    "previous_returns_count": 0,
    "payment_method": "credit_card",
    "ip_country_match": 1,
    "merchant_id": "razorpay_test"
}
resp = requests.post(f"{BASE_URL}/score", json=low_risk)
print(json.dumps(resp.json(), indent=2))

# Test 5: Batch scoring
print("\n5️⃣ Score BATCH of Transactions:")
batch = {
    "transactions": [high_risk, low_risk]
}
resp = requests.post(f"{BASE_URL}/batch", json=batch)
print(json.dumps(resp.json(), indent=2))

print("\n" + "=" * 70)
print("✅ All tests complete!")
print("=" * 70)