import pandas as pd 
df = pd.read_csv("../../data/raw/expenses.csv")
df.head(10)

df["createdAt"] = pd.to_datetime(df["createdAt"])
df = df.sort_values("createdAt")
df

user_stats = {} 
past_counts  = [] 
user_avg_amounts = [] 
amount_minus_user_avg = [] 
time_gaps = []

for _, row in df.iterrows():
    user = row['paidBy']
    amount = row["amount"]
    current_timestamp = row['createdAt']
    
    # if user is seen before
    if user in user_stats:
        past_count = user_stats[user]['count']
        past_sum = user_stats[user]['sum']
        last_timestamp = user_stats[user]['last_timestamp']

        user_avg = past_sum / past_count
        time_gap = (current_timestamp - last_timestamp).total_seconds() / 60
    else: 
        past_count = 0
        user_avg = 0
        time_gap = 0

    # Storing the features
    past_counts.append(past_count)
    user_avg_amounts.append(user_avg)
    amount_minus_user_avg.append(amount - user_avg)
    time_gaps.append(time_gap)

    # update dict after computing features
    if user in user_stats:
        user_stats[user]['count'] += 1
        user_stats[user]['sum'] += amount
        user_stats[user]['last_timestamp'] = current_timestamp
    else:
         user_stats[user] = {
            "count": 1,
            "sum": amount,
            'last_timestamp' : current_timestamp
        }

df["past_transaction_count"] = past_counts
df["user_avg_amount"] = user_avg_amounts
df["amount_minus_user_avg"] = amount_minus_user_avg
df['time_gap_minutes'] = time_gaps
df.head(20)

df['hour'] = pd.to_datetime(df['createdAt']).dt.hour
df['date'] = pd.to_datetime(df['createdAt']).dt.date

df['date'] = pd.to_datetime(df['date']).dt.floor('D')
df['day_of_week'] = df['date'].dt.dayofweek


df = df.drop(columns=['expenseId','groupId', 'paidBy', 'date', 'createdAt', 'category'])

df.isna().sum()

df.to_csv('../../data/processed/features.csv')


