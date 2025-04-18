# Career_Guidance_Project
# Files arrangement
  app.py
 "database.db
 train_model.py
 "encoders.pkl
 "model.pkl
 career_dataset.csv
  templates 
 '' index.html

 Introduction

Career confusion is common among students.
Choosing the right career at the right time is important.
Our system suggests careers based on academic performance and interests. Image: Confused student vs guided student

Objective

Predict suitable career paths using user inputs.
Guide students with a step-by-step career roadmap.
Build an intelligent, user-friendly system.

System Architecture

User inputs data (marks, interest, skills)
Data sent to backend via Flask
Model processes and predicts career
Roadmap is shown based on career 
User → Frontend → Flask → Model → Result

Technologies Used
Languages: Python, HTML, CSS, JS
Framework: Flask
Database: SQLite
Libraries: scikit-learn, pandas, pickle

Model Training

Used Random Forest Classifier
Features: Maths, Science, English, Interest, Skill
Encoded categorical data using LabelEncoder
Trained on cleaned CSV dataset with 25+ careers 

 Frontend & Backend

Frontend: Beautiful HTML/CSS form with background image
Backend: Flask handles form, predicts using ML model
Data sent and received using fetch API (JavaScript) 

 Database Design
 
SQLite database named database.db
Stores user data with predicted career and roadmap
Future reference possible Table Fields: Name, Maths, Science, English, Interest, Skill, Career, Roadmap

 Output & Results
 
Predicts career in real-time
Shows personalized roadmap for guidance
Prevents invalid input (like all 0 marks)

Future Scope:

Add more features like personality test
Suggest relevant courses or colleges
Make it multi-language

Conclusion:
The system is simple, effective, and helpful for students
Covers all basic needs for career guidance
