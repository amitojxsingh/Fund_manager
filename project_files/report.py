# generate_report.py

from models import session, Member
import pandas as pd

def generate_member_summary():
    members = session.query(Member).all()
    summary = []
    for member in members:
        summary.append({
            "Name": member.name,
            "Total Pool Amount": member.total_pool_amount,
            "Loss": member.loss,
            "Profit": member.profit,
            "Effective Contribution": member.effective_contribution,
            "Committee Value": member.committee_value
        })
    return pd.DataFrame(summary)

def save_report_to_csv(file_path):
    summary_df = generate_member_summary()
    summary_df.to_csv(file_path, index=False)
    print(f"Report saved to {file_path}")
