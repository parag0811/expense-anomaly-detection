# | Category  | Normal Range (₹) | Typical Time |
# | --------- | ---------------- | ------------ |
# | Food      | 150–800          | 12–14, 19–22 |
# | Snacks    | 50–300           | 16–20        |
# | Travel    | 500–5000         | 08–20        |
# | Movie     | 200–600          | 18–23        |
# | Groceries | 500–3000         | 10–21        |


import pandas as pd
import random
from datetime import datetime, timedelta

users = ["U1", "U2", "U3", "U4", "U5"]
groups = ["G1", "G2", "G3"]
categories = ["food", "travel", "rent", "shopping", "other"]

def generate_amount(category):
    ranges = {
         "food": (150, 800),
        "travel": (300, 4000),
        "rent": (5000, 20000),
        "shopping": (500, 8000),
        "other": (100, 5000),
    }

    return random.randint(*ranges[category])

def generate_time(category):
    hour_ranges = {
        "food": [(8,10),(11,14),(18,22)],
        "travel": [(6,22)],
        "rent": [(8,12)],
        "shopping": [(10,21)],
        "other": [(0,23)],
    }
    hr_range = random.choice(hour_ranges[category])
    hour = random.randint(hr_range[0], hr_range[1])
    minute = random.randint(0,59)
    return hour , minute

data = []

base_date = datetime(2025,1,1)

for i in range(500):
    category = random.choice(categories)
    paidBy = random.choice(users)
    groupId = random.choice(groups)

    # 15% anomaly injection
    if random.random() < 0.15:
        amount = random.randint(10000, 50000)
        hour = random.randint(0,4)  # weird time
        minute = random.randint(0,59)
    else:
        amount = generate_amount(category)
        hour, minute = generate_time(category)

    createdAt = base_date + timedelta(days=random.randint(0,180),
                                       hours=hour,
                                       minutes=minute)
    data.append({
        "expenseId": f"E{i+1}",
        "groupId": groupId,
        "paidBy": paidBy,
        "amount": amount,
        "category": category,
        "createdAt": createdAt
    })

df = pd.DataFrame(data)
df.to_csv("data/raw/expenses.csv", index=False)

print("Dataset created.")