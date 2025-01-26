# Personalized-Student-Recommendations

Project Overview
This project offers in-depth performance analysis for a student using data from their quiz. It assists in finding what topics and weak difficulty levels can be found or performance trends of students over time. Insights are delivered to the teachers or even directly to the student for a proper understanding of what's happening regarding performance and focus areas for enhancement.

Using the Flask application developed, the application will accept students' student IDs and generate detailed insights, personalized recommendations, and performance trends on their quiz outcomes. Furthermore, the system deduces a pattern in quiz data to define the personality of a student and give action-oriented insights for improvement.

Solution
1. Data Extraction and Analysis
History Quiz Data : We load in historical quiz data and extract applicable fields such as topic, level of difficulty, and score from nested quiz data.
Student Performance Analysis: We analyze the performance of each student in different topics, difficulty levels, and track the performance trend over time.
Recommendations and Insights: The system provides recommendations like areas for improvement, weak topics, and difficulty levels to focus on based on the performance data.
Persona Generation: The system dynamically generates a student persona based on performance patterns, which helps students understand their learning style and identify strengths and weaknesses.
2. User Interaction:
Students can input their user_id to receive personalized insights.
The application displays:
Weak topics and difficulty levels
A performance trend graph
Personalized recommendations to improve performance
3. Visualization:
A performance trend chart is generated using Matplotlib, displaying recent quiz scores for each student.
Insights are presented in an easy-to-read format using HTML and CSS.
Features
User Performance Analysis: Helps identify weak topics, difficulty levels, and tracks progress.
Personalized Recommendations: Provides actionable recommendations for improvement.
Performance Trend Graph: It shows a graphical representation of performance over recent quizzes.
Student Persona: Automatically generates a student persona based on quiz patterns and performance.
Responsive Web Interface: Designed for easy interaction with the student and educator.
Setup Instructions
Prerequisites
Make sure you have the following software installed:

Python 3.x
Flask
Pandas
Matplotlib
Installation Steps
Clone the repository:

bash
Copy
Edit
git clone <repository_url>
cd student-performance-insights
Create a Virtual Environment:

If you're using venv for Python virtual environments:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`
Install Dependencies:

Install the following Python packages:

bash
Copy
Edit
pip install -r requirements.txt
Prepare the Data:

Move your current_quiz.json and historical_quiz.json files into the root directory of the project.

Run the Application:

Start the Flask application:

bash
Copy
Edit
python app.py
The app should be now accessed at http://127.0.0.1:5000/.
Project Structure
php
Copy
Edit
student-performance-insights/
├── app.py # Main Flask application
├── requirements.txt # requirements from downloaded dependencies
├── current_quiz.json # JSON file with current quiz information
├── historical_quiz.json # JSON file with historical quiz information
├── templates/
│ ├── index.html # Home page
│ └── insights.html # Page of insights
├── static/
│ └── trend.png # Trend chart of performance
└── README.md # This file

![image](https://github.com/user-attachments/assets/e056829a-0fbb-45b0-9f71-c9a4bbba603b)


