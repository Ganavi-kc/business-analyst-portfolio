import pandas as pd
from analytics import sla_metrics,score_fraud,process_metrics,portfolio_metrics

def test_sla():
    assert sla_metrics(pd.DataFrame({"sla_met":[True,False],"resolution_hours":[2,4]}))["sla_rate"]==0.5

def test_fraud():
    x=pd.DataFrame({"amount_cad":[3000],"international":[1],"new_payee":[1],"velocity_24h":[6],"hour":[2]})
    assert int(score_fraud(x).risk_score.iloc[0])==100

def test_process():
    assert process_metrics(pd.DataFrame({"as_is_hours":[10],"to_be_hours":[5]}))["reduction_pct"]==50

def test_portfolio():
    x=pd.DataFrame({"status":["On Track","At Risk"],"actual_cad":[120,100],"budget_cad":[100,100]})
    assert portfolio_metrics(x)["budget_variance"]==20
