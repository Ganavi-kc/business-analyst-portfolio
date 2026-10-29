"""Run: streamlit run app.py"""
from pathlib import Path
import pandas as pd
import streamlit as st
from analytics import sla_metrics, score_fraud, process_metrics, portfolio_metrics

st.set_page_config(page_title="Business Analyst Portfolio",page_icon="📊",layout="wide")
st.markdown("""<style>.block-container{padding-top:2rem}h1,h2,h3{color:#113a5d}div[data-testid="stMetric"]{background:#eef5f9;border-radius:12px;padding:14px}</style>""",unsafe_allow_html=True)
st.title("Business Analyst | Analytics & Operational Excellence")
st.caption("Four reproducible case studies using synthetic data — not real banking or employer information.")
options={"Banking Operations":"01-banking-operations/data/operations.csv","Fraud Analytics":"02-fraud-analytics/data/transactions.csv","Process Improvement":"03-process-improvement/data/requests.csv","Project Portfolio":"04-project-portfolio/data/projects.csv"}
choice=st.sidebar.radio("Explore a project",list(options))
df=pd.read_csv(Path(__file__).parent/options[choice])
if choice=="Banking Operations":
    st.header("Banking Operations & SLA Intelligence")
    selected=st.multiselect("Channel",sorted(df.channel.unique()),default=sorted(df.channel.unique()))
    x=df[df.channel.isin(selected)];m=sla_metrics(x)
    a,b,c=st.columns(3);a.metric("Cases",m["cases"]);b.metric("SLA compliance",f'{m["sla_rate"]:.1%}');c.metric("Avg resolution",f'{m["avg_resolution_hours"]:.1f} h')
    st.subheader("SLA compliance by priority");st.bar_chart(x.groupby("priority").sla_met.mean().sort_values())
    st.subheader("Volume by channel");st.bar_chart(x.channel.value_counts())
elif choice=="Fraud Analytics":
    st.header("Fraud Risk & Transaction Analytics")
    x=score_fraud(df);tier=st.multiselect("Risk tier",["Low","Medium","High"],default=["Low","Medium","High"]);x=x[x.risk_tier.astype(str).isin(tier)]
    a,b,c=st.columns(3);a.metric("Transactions",len(x));b.metric("High-risk flags",int((x.risk_tier=="High").sum()));c.metric("Flagged amount",f'${x.loc[x.risk_tier=="High","amount_cad"].sum():,.0f}')
    st.bar_chart(x.risk_tier.value_counts());st.dataframe(x.sort_values("risk_score",ascending=False).head(30),use_container_width=True)
    st.caption("Rule-based risk flags are illustrative and are not confirmed fraud labels.")
elif choice=="Process Improvement":
    st.header("Process Improvement & Requirements")
    team=st.selectbox("Team",["All"]+sorted(df.team.unique()));x=df if team=="All" else df[df.team==team]
    m=process_metrics(x);a,b,c=st.columns(3);a.metric("AS-IS average",f'{m["before"]:.1f} h');b.metric("TO-BE average",f'{m["after"]:.1f} h');c.metric("Modeled reduction",f'{m["reduction_pct"]:.1f}%')
    st.bar_chart(pd.DataFrame({"Hours":[m["before"],m["after"]]},index=["AS-IS","TO-BE"]))
    st.caption("TO-BE times are simulated scenarios, not realized production outcomes.")
else:
    st.header("Project Portfolio & RAID Analytics")
    workstream=st.multiselect("Workstream",sorted(df.workstream.unique()),default=sorted(df.workstream.unique()));x=df[df.workstream.isin(workstream)];m=portfolio_metrics(x)
    a,b,c=st.columns(3);a.metric("Projects",m["projects"]);b.metric("At risk / delayed",m["at_risk"]);c.metric("Budget variance",f'${m["budget_variance"]:,.0f}')
    st.bar_chart(x.status.value_counts());st.bar_chart(x.groupby("workstream").open_high_risks.sum())
    st.dataframe(x.sort_values("open_high_risks",ascending=False).head(25),use_container_width=True)
