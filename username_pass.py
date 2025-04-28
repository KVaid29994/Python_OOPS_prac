import pandas as pd

# Create sample data
data = {
    'email': [
        'john@example.com', 'alice@example.com', 'bob@example.com',
        'carla@example.com', 'dave@example.com', 'eve@example.com',
        'frank@example.com', 'grace@example.com', 'henry@example.com', 'irene@example.com'
    ],
    'password': [
        'john123', 'alice123', 'bob123', 'carla123', 'dave123',
        'eve123', 'frank123', 'grace123', 'henry123', 'irene123'
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('users.csv', index=False)
