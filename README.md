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

APPROACH

The approach for this project will be data-driven insights that help the student improve their performance in a quiz based on their historical data in quiz history. The steps will be broken down as follows:

Data Collection: The project collects quiz data, including user scores, topics, and difficulty levels, from JSON files and stores them in structured formats for easier analysis.

Data Extraction and Processing: The quiz data is in a nested form, which is further processed using pandas in Python for extracting key details of the topic and the difficulty level involved in each quiz.

Performance Analysis:

The system analyzes the performance of the student. It identifies areas of weakness with topics and their respective difficulty levels. It further calculates the average scores for each topic and difficulty level, and flags scores below a specific threshold of 50.
It tracks the student's recent quiz scores to visualize improvement or decline over time.
Personalized Recommendations: The system generates tailored recommendations based on the analysis. If the student is struggling in certain areas, which could be weak topics or difficulty levels, the system suggests focusing on those areas. If the student is performing well, it highlights their strengths.

Visualization: The outcome of the analysis is presented in a user-friendly format, where weak topics are shown with bullet points and the difficulty level of each topic along with a line chart representing recent performance.

Web Interface: The Flask app presents a simple web interface where the user can enter his ID and view his own insights. He can also be given recommendations to improve. It is an easily accessible and interactive application.

In essence, the method seeks to empower students with actionable insights, so they can focus on areas that need attention and track their progress over time.

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


![image](https://github.com/user-attachments/assets/c32244d3-425f-4dbe-9307-d74a82146c0b)


![image](https://github.com/user-attachments/assets/6f2536b2-0391-4671-9f08-843b313cf9c2)



