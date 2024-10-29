# main.py

from models import load_members_from_file
from calculators import allocate_kitty
from report import save_report_to_csv

if __name__ == "__main__":
    # Load members from a file
    file_path = "members.csv"  # Example file path
    load_members_from_file(file_path)
    
    # Example allocations for each month with bids
    try:
        allocate_kitty(month=1, winning_member_name="Rana mamu", bid_loss=70_000)
        allocate_kitty(month=2, winning_member_name="mom", bid_loss=40_000)
        allocate_kitty(month=3, winning_member_name="papa", bid_loss=80_000)
    except Exception as e:
        print(f"Error in allocation: {e}")

    # Generate and save the report
    save_report_to_csv("member_summary.csv")
