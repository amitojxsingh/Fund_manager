# load_data.py

import pandas as pd
from models import session, Member
import os

def load_members_from_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    if file_extension == '.csv':
        df = pd.read_csv(file_path)
    elif file_extension in ['.xls', '.xlsx']:
        df = pd.read_excel(file_path)
    elif file_extension == '.json':
        df = pd.read_json(file_path)
    else:
        raise ValueError("Unsupported file format")

    # Check for required columns and unique member names
    required_columns = {'name', 'total_pool_amount', 'effective_contribution'}
    if not required_columns.issubset(df.columns):
        raise ValueError("Missing required columns in the data file")

    for _, row in df.iterrows():
        member = Member(
            name=row['name'],
            total_pool_amount=row.get('total_pool_amount', 400_000),
            effective_contribution=row.get('effective_contribution', 20_000)
        )
        session.add(member)
    
    session.commit()
    print("Members loaded successfully from file.")
