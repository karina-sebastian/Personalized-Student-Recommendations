from flask import Flask, render_template, request, jsonify
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

# Load sample data
current_quiz_data = pd.read_json('current_quiz.json')
historical_quiz_data = pd.read_json('historical_quiz.json')

# Extract relevant fields from nested data
if 'quiz' in historical_quiz_data.columns:
    historical_quiz_data['topic'] = historical_quiz_data['quiz'].apply(lambda x: x['topic'] if x and 'topic' in x else None)
    historical_quiz_data['difficulty_level'] = historical_quiz_data['quiz'].apply(lambda x: x['difficulty_level'] if x and 'difficulty_level' in x else None)


# Function to analyze user performance
def analyze_user_performance(user_id):
    # Ensure user_id is a string (sanitize input)
    user_id = str(user_id).strip()  # Remove any extra whitespace
    print(f"Received user_id: {user_id}")  # Debugging line
    
    # Filter user-specific data based on user_id
    user_data = historical_quiz_data[historical_quiz_data['user_id'] == user_id]
    print(f"Filtered user data: {user_data}")  # Debugging line

    if user_data.empty:
        return {
            "weak_topics": [],
            "weak_difficulty": [],
            "recent_scores": []
        }

    # Weak topics
    user_topic_performance = user_data.groupby('topic')['score'].mean()
    weak_topics = user_topic_performance[user_topic_performance < 50].index.tolist()

    # Weak difficulty levels
    user_difficulty_performance = user_data.groupby('difficulty_level')['score'].mean()
    weak_difficulty = user_difficulty_performance[user_difficulty_performance < 50].index.tolist()

    # Improvement trend
    recent_scores = user_data.tail(5)['score'].tolist()

    return {
        "weak_topics": weak_topics,
        "weak_difficulty": weak_difficulty,
        "recent_scores": recent_scores
    }
# Function to define the student persona
def define_student_persona(user_data):
    if user_data.empty:
        return "No data available for this user."

    # Calculate the average score of the user
    average_score = user_data['score'].mean()

    # Define the student persona based on the average score and recent performance trend
    if average_score >= 80:
        persona = "You’re on a roll! Keep up the fantastic work and aim for the stars 🎯"
        description = "You're a consistent high performer! Keep up the excellent work, and continue to challenge yourself with more advanced topics."
    elif average_score >= 50:
        persona = " Solid progress, but let's take it to the next level! 🚀 "
        description = "You're doing well, but there's room for improvement. Consider focusing on weak topics to enhance your performance."
    else:
        persona = "Don't worry, you're not alone—together we'll work through it! 💪"
        description = "It looks like you're struggling in some areas. Try to focus on improving your weak topics and difficulty levels. Don't hesitate to reach out for extra help!"
    
    # Consider trends (e.g., if a student is improving)
    recent_performance = user_data.tail(5)['score'].tolist()
    if all(score >= 50 for score in recent_performance):
        trend = "Improving"
        trend_description = "You're showing improvement in recent quizzes! Keep going, and you will see even more progress."
    elif all(score < 50 for score in recent_performance):
        trend = "Declining"
        trend_description = "Your recent scores suggest a decline in performance. Focus on reviewing the challenging topics."
    else:
        trend = "Mixed"
        trend_description = "Your performance has been inconsistent. Try to focus on identifying your weak areas and work on them."

    return {
        "persona": persona,
        "description": description,
        "trend": trend,
        "trend_description": trend_description
    }

# Modify analyze_user_performance function to return the persona insights
def analyze_user_performance(user_id):
    user_data = historical_quiz_data[historical_quiz_data['user_id'] == user_id]

    if user_data.empty:
        return {
            "weak_topics": [],
            "weak_difficulty": [],
            "recent_scores": [],
            "persona": "No data available",
            "description": "",
            "trend": "",
            "trend_description": ""
        }

    # Analyze weak topics, difficulty levels, and recent scores
    user_topic_performance = user_data.groupby('topic')['score'].mean()
    weak_topics = user_topic_performance[user_topic_performance < 50].index.tolist()

    user_difficulty_performance = user_data.groupby('difficulty_level')['score'].mean()
    weak_difficulty = user_difficulty_performance[user_difficulty_performance < 50].index.tolist()

    recent_scores = user_data.tail(5)['score'].tolist()

    # Define the student persona
    persona_data = define_student_persona(user_data)

    return {
        "weak_topics": weak_topics,
        "weak_difficulty": weak_difficulty,
        "recent_scores": recent_scores,
        "persona": persona_data["persona"],
        "description": persona_data["description"],
        "trend": persona_data["trend"],
        "trend_description": persona_data["trend_description"]
    }

# Home route
@app.route('/')
def index():
    return render_template('index.html')


# Analyze user performance and provide recommendations
@app.route('/analyze', methods=['POST'])
def analyze():
    user_id = request.form['user_id']  # Ensure user_id is taken as a string
    analysis = analyze_user_performance(user_id)

    # Generate recommendations
    recommendations = []
    if analysis["weak_topics"]:
        recommendations.append(f"Focus on weak topics: {', '.join(analysis['weak_topics'])}")
    else:
        recommendations.append("You're doing well in all topics!")

    if analysis["weak_difficulty"]:
        recommendations.append(f"Focus on questions with difficulty levels: {', '.join(analysis['weak_difficulty'])}")
    else:
        recommendations.append("You're performing well in all difficulty levels!")

    # Save improvement trend chart
    plt.figure(figsize=(6, 4))
    plt.plot(range(1, len(analysis["recent_scores"]) + 1), analysis["recent_scores"], marker='o')
    plt.title("Recent Performance Trend")
    plt.xlabel("Recent Quizzes")
    plt.ylabel("Scores")
    plt.savefig('static/trend.png')

    return render_template('insights.html', analysis=analysis, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
