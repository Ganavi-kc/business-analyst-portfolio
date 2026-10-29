"""Reusable, deterministic analytics for four synthetic BA case studies."""
import pandas as pd

def sla_metrics(df):
    if df.empty: return {"cases":0,"sla_rate":0.0,"avg_resolution_hours":0.0}
    return {"cases":len(df),"sla_rate":float(df["sla_met"].mean()),"avg_resolution_hours":float(df["resolution_hours"].mean())}

def score_fraud(df):
    x=df.copy()
    x["risk_score"]=(x["amount_cad"].gt(2000).astype(int)*30 + x["international"].astype(int)*20 + x["new_payee"].astype(int)*20 + x["velocity_24h"].ge(5).astype(int)*20 + x["hour"].between(0,5).astype(int)*10)
    x["risk_tier"]=pd.cut(x["risk_score"],bins=[-1,19,49,100],labels=["Low","Medium","High"])
    return x

def process_metrics(df):
    if df.empty: return {"before":0.0,"after":0.0,"reduction_pct":0.0}
    a=float(df["as_is_hours"].mean());b=float(df["to_be_hours"].mean())
    return {"before":a,"after":b,"reduction_pct":(a-b)/a*100 if a else 0.0}

def portfolio_metrics(df):
    if df.empty: return {"projects":0,"at_risk":0,"budget_variance":0}
    return {"projects":len(df),"at_risk":int(df["status"].isin(["At Risk","Delayed"]).sum()),"budget_variance":int((df["actual_cad"]-df["budget_cad"]).sum())}
