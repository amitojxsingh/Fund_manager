# test_data.py
members_test_data = [
    {
        "name": "Alice",
        "total_pool_amount": 400000,
        "loss": 5000,
        "profit": 15000,
        "effective_contribution": 20000,
        "committee_value": 400000,
    },
    {
        "name": "Bob",
        "total_pool_amount": 1_000_000,  # Edge case with high value
        "loss": 100000,
        "profit": 200000,
        "effective_contribution": 50000,
        "committee_value": 1_000_000,
    },
    {
        "name": "",  # Invalid case with empty name
        "total_pool_amount": 300000,
        "loss": 0,
        "profit": 0,
        "effective_contribution": 15000,
        "committee_value": 300000,
    },
]

monthly_allocations_test_data = [
    {
        "month": 1,  # Valid input for January
        "winning_member_id": 1,  # Assuming member ID 1 exists
        "bid_loss": 10000,
        "total_pool_amount": 400000,
    },
    {
        "month": 12,  # Valid input for December
        "winning_member_id": 2,  # Assuming member ID 2 exists
        "bid_loss": 5000,
        "total_pool_amount": 400000,
    },
    {
        "month": 0,  # Edge case with invalid month
        "winning_member_id": 3,  # Assuming member ID 3 does not exist
        "bid_loss": 0,
        "total_pool_amount": 400000,
    },
    {
        "month": 13,  # Edge case with invalid month
        "winning_member_id": 1,  # Assuming member ID 1 exists
        "bid_loss": 1000,
        "total_pool_amount": 400000,
    },
]
