# AI Risk Manager - Razorpay Buildathon

## Problem
Merchants lose ₹XX monthly to returns, chargebacks, and fraud. No way to predict which orders will be problematic.

## Solution
AI model that scores return risk in real-time, enabling merchants to take action before loss occurs.

## Results
- **Precision**: 62% (of flagged orders, 62% actually returned)
- **Recall**: 75% (caught 75% of actual returns)
- **False-Positive Rate**: 5%
- **Net Benefit**: ₹1,355,000/month per merchant

## Live Demo
```bash
# Terminal 1: Run API
python app.py

# Terminal 2: Test
python simple_test.py
```

## API Endpoints

### Score Single Transaction
```bash
POST /score
{
  "transaction_id": "TXN-001",
  "account_age_days": 5,
  "order_amount": 25000,
  "product_category": "electronics",
  "lifetime_orders": 1,
  "previous_returns_count": 0,
  "order_velocity_24h": 2,
  "payment_method": "credit_card",
  "ip_country_match": 1
}
```

### Score Batch
```bash
POST /batch
{ "transactions": [ {...}, {...} ] }
```

### Get Metrics
```bash
GET /metrics
```

### Audit Log
```bash
GET /audit
```

## How It Works
1. Customer data enters → 12 features engineered
2. XGBoost model scores return probability
3. If high-risk: recommend ID verification (FRICTION policy)
4. If low-risk: process normally
5. Log audit trail for compliance

## Key Signals
- New customer (age < 30 days) = higher risk
- High-value orders (> ₹10K) = higher risk
- Electronics/apparel categories = higher risk
- Serial returners = higher risk
- Bulk purchases = higher risk

## Files
- `app.py` - Flask API
- `return_risk_model.pkl` - Trained model
- `synthetic_transactions.csv` - Training data
- `evaluation_report.txt` - Full metrics

## Defense-Only
✅ Only detects risk (doesn't execute)
✅ Merchants make final decision
✅ Full audit trail for compliance
❌ No offensive capabilities

## Tech Stack
- Model: XGBoost
- API: Flask
- Data: 10,000 synthetic transactions
- Testing: Postman verified