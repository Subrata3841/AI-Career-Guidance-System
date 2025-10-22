from flask import Flask, request, jsonify
import pandas as pd
import joblib
import os
import sys
from flask_cors import CORS

# Import the SimpleCareerModel class from simple_model_runner.py
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from simple_model_runner import SimpleCareerModel

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the model
MODEL_PATH = 'career_recommendation_model.joblib'

def load_model():
    try:
        if os.path.exists(MODEL_PATH):
            model = joblib.load(MODEL_PATH)
            print("Model loaded successfully")
            return model
        else:
            print("Model file not found. Please run simple_model_runner.py first")
            return None
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

model = load_model()

@app.route('/')
def index():
    return jsonify({"status": "API is running", "model_loaded": model is not None})

@app.route('/recommend', methods=['POST'])
def recommend():
    if model is None:
        return jsonify({"error": "Model not loaded. Please run simple_model_runner.py first"}), 500
    
    try:
        data = request.json
        print("Received data:", data)
        
        # Validate input
        required_fields = ['skills', 'interests', 'years_of_experience', 'education_level_encoded']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
        
        # Create dataframe from user input
        user_data = pd.DataFrame([{
            'skills': data['skills'],
            'interests': data['interests'],
            'years_of_experience': int(data['years_of_experience']),
            'education_level_encoded': int(data['education_level_encoded'])
        }])
        
        print("Processed user data:", user_data)
        
        # Get predictions
        recommendations = model.predict(user_data)
        print("Model predictions:", recommendations)
        
        # Format and return results
        formatted_results = []
        for rec in recommendations[0][:5]:  # Return top 5 recommendations
            formatted_results.append({
                "career_path": rec['career_path'],
                "confidence_score": round(rec['confidence_score'], 1),
                "skills_required": get_required_skills(rec['career_path'])
            })
        
        print("Formatted results:", formatted_results)
        
        return jsonify({
            "recommendations": formatted_results
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_required_skills(career_path):
    """Return sample required skills for each career path"""
    skills_map = {
        'Software Developer': ["Python", "JavaScript", "Cloud Computing", "Git", "DevOps"],
        'Data Scientist': ["Python", "Statistics", "Machine Learning", "SQL", "Data Visualization"],
        'UX Designer': ["UI Design", "User Research", "Wireframing", "Prototyping", "Design Tools"],
        'Project Manager': ["Agile", "Communication", "Leadership", "Risk Management", "Stakeholder Management"],
        'Business Analyst': ["SQL", "Data Analysis", "Requirements Gathering", "Documentation", "Process Modeling"],
        'Marketing Specialist': ["Digital Marketing", "Content Creation", "Analytics", "Social Media", "SEO"],
        'Healthcare Administrator': ["Healthcare Systems", "Regulations", "Budget Management", "Staff Coordination", "Patient Services"],
        'Financial Analyst': ["Financial Modeling", "Excel", "Accounting", "Data Analysis", "Forecasting"]
    }
    
    return skills_map.get(career_path, ["Analytical Thinking", "Problem Solving", "Communication"])

if __name__ == '__main__':
    port = 5000
    print(f"Starting API server on port {port}")
    app.run(debug=True, port=port)