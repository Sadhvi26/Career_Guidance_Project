from flask import Flask, render_template, request, jsonify
import pickle
import sqlite3
import pandas as pd

app = Flask( __name__)

# Load model and encoders
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('encoders.pkl', 'rb') as f:
    encoders = pickle.load(f)

interest_encoder = encoders['interest']
skill_encoder = encoders['skill']
career_encoder = encoders['career']

# Load roadmap data from the same CSV used for training
roadmap_df = pd.read_csv('career_dataset.csv')

DB_NAME = 'database.db'

@app.route('/')
def index():
    return render_template('index.html',
                           interests=list(interest_encoder.classes_),
                           skills=list(skill_encoder.classes_))

@app.route('/guidance', methods=['POST'])
def guidance():
    try:
        data = request.json
        name = data['name']
        maths = float(data['maths'])
        science = float(data['science'])
        english = float(data['english'])

        # If all marks are zero
        if maths == 0 and science == 0 and english == 0:
            return jsonify({'message': 'Please enter valid marks. All subjects cannot be zero.', 'status': 'error'})

        interest = interest_encoder.transform([data['interest']])[0]
        skill = skill_encoder.transform([data['skill']])[0]

        prediction = model.predict([[maths, science, english, interest, skill]])[0]
        career = career_encoder.inverse_transform([prediction])[0]

        # Get the roadmap from the CSV
        roadmap_row = roadmap_df[roadmap_df['Career'] == career]
        roadmap = roadmap_row['Roadmap'].values[0] if not roadmap_row.empty else 'No roadmap available.'

        # Save user data to SQLite
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS Career_Guidance 
                     (Name TEXT, Maths REAL, Science REAL, English REAL, Interest TEXT, Skill TEXT, Career TEXT, Roadmap TEXT)""")
        c.execute("INSERT INTO Career_Guidance VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                  (name, maths, science, english, data['interest'], data['skill'], career, roadmap))
        conn.commit()
        conn.close()

        return jsonify({'career': career, 'roadmap': roadmap, 'status': 'success'})
    except Exception as e:
        return jsonify({'message': str(e), 'status': 'error'})

if __name__ == '__main__':
    app.run(debug=True)