import pandas as pd
import matplotlib.pyplot as plt
import os
from load_data import load_combined_data

# Load a sample of data for performance
df_all = load_combined_data(nrows=200000)

# Keep only required columns
df = df_all[['user_session', 'event_type']].drop_duplicates()

# Group events per session
session_events = df.groupby('user_session')['event_type'].apply(set).reset_index()

# Classify each session into funnel stage
def classify_session(events):
    if 'purchase' in events and 'cart' in events:
        return 'View + Cart + Purchase'
    elif 'purchase' in events and 'cart' not in events:
        return 'View + Purchase (No Cart)'
    elif 'cart' in events and 'purchase' not in events:
        return 'View + Cart (No Purchase)'
    else:
        return 'Only View'

session_events['session_type'] = session_events['event_type'].apply(classify_session)

# Count number of sessions in each category
funnel_counts = session_events['session_type'].value_counts()

print("\n--- Session Classification Breakdown ---")
print(funnel_counts)

# Define funnel stages
total_sessions = funnel_counts.sum()
view_sessions = total_sessions

# Count users who added to cart (regardless of purchase)
cart_sessions = (
    funnel_counts.get('View + Cart + Purchase', 0) +
    funnel_counts.get('View + Cart (No Purchase)', 0)
)

# Count users who completed a purchase through cart
purchase_sessions = funnel_counts.get('View + Cart + Purchase', 0)

# Calculate conversion rates
view_to_cart_rate = cart_sessions / view_sessions * 100
cart_to_purchase_rate = purchase_sessions / cart_sessions * 100 if cart_sessions else 0
view_to_purchase_rate = purchase_sessions / view_sessions * 100

print(f"\n--- Conversion Rates ---")
print(f"View to Cart Rate: {view_to_cart_rate:.2f}%")
print(f"Cart to Purchase Rate: {cart_to_purchase_rate:.2f}%")
print(f"View to Purchase Rate: {view_to_purchase_rate:.2f}%")

# Create charts directory if it doesn't exist
os.makedirs("charts", exist_ok=True)

# Prepare funnel data for plotting
stages = ['View', 'Cart', 'Purchase']
counts = [view_sessions, cart_sessions, purchase_sessions]

plt.figure(figsize=(8, 5))
bars = plt.barh(stages, counts, color='skyblue')

# Annotate each bar with actual count
for bar in bars:
    width = bar.get_width()
    plt.text(width + 1000, bar.get_y() + bar.get_height() / 2,
             f'{int(width):,}', va='center', fontsize=10)

plt.title("User Funnel: View → Cart → Purchase")
plt.xlabel("Number of Sessions")
plt.tight_layout()
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.savefig("charts/funnel_bar_horizontal.png")
plt.show()

# Calculate drop-off percentages
view_to_cart_drop = (view_sessions - cart_sessions) / view_sessions * 100
cart_to_purchase_drop = (cart_sessions - purchase_sessions) / cart_sessions * 100 if cart_sessions else 0

print("\n--- Drop-off Analysis ---")
print(f"Drop-off after View (did not add to cart): {view_to_cart_drop:.2f}%")
print(f"Drop-off after Cart (did not purchase): {cart_to_purchase_drop:.2f}%")
