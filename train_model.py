import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv('career_dataset.csv')

# Encode categorical data
interest_encoder = LabelEncoder()
skill_encoder = LabelEncoder()
career_encoder = LabelEncoder()

df['Interest'] = interest_encoder.fit_transform(df['Interest'])
df['Skill'] = skill_encoder.fit_transform(df['Skill'])
df['Career'] = career_encoder.fit_transform(df['Career'])

# Features and labels
X = df[['Maths', 'Science', 'English', 'Interest', 'Skill']]
y = df['Career']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model and encoders
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('encoders.pkl', 'wb') as f:
    pickle.dump({
        'interest': interest_encoder,
        'skill': skill_encoder,
        'career': career_encoder
    }, f)