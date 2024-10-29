# calculations.py

from models import session, Member, MonthlyAllocation

def allocate_kitty(month: int, winning_member_name: str, bid_loss: float = 0):
    winner = session.query(Member).filter_by(name=winning_member_name).first()
    if not winner:
        raise ValueError(f"No member named '{winning_member_name}' found.")

    # Apply bid loss and distribute among other members
    if bid_loss < 0:
        raise ValueError("Bid loss cannot be negative.")
    
    winner.loss += bid_loss
    winner.committee_value -= bid_loss
    shared_loss = bid_loss / session.query(Member).count()
    
    for member in session.query(Member):
        if member.name != winning_member_name:
            member.profit += shared_loss
            member.effective_contribution -= shared_loss
    
    allocation = MonthlyAllocation(
        month=month,
        winning_member_id=winner.id,
        bid_loss=bid_loss,
        total_pool_amount=400_000 - bid_loss
    )
    session.add(allocation)
    session.commit()
    
    print(f"Month {month}: {winner.name} received {winner.committee_value} with a loss of {bid_loss}.")
