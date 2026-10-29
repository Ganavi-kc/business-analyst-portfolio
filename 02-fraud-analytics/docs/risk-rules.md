# Fraud rules — demonstration only

This is a **triage exercise**, not a fraud detection system or a trained model. Rules are intentionally explainable. A high risk score means *review first*, not *fraud confirmed*.

Risk weights: amount > CAD 2,000: 30; international: 20; new payee: 20; velocity ≥5: 20; overnight hour 0–5: 10.

Scores 0–19: Low; 20–49: Medium; 50–100: High.

Before production, evaluate false positives, class imbalance, bias, security, and regulatory requirements using approved data.
