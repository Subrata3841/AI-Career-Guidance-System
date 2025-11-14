from flask import Flask, request, jsonify, send_from_directory
import pandas as pd
import joblib
import os
import sys
from flask_cors import CORS
import json

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

@app.route('/visualizations')
def list_visualizations():
    """List available visualization files"""
    viz_dir = 'visualizations'
    if os.path.exists(viz_dir):
        files = [f for f in os.listdir(viz_dir) if f.endswith(('.png', '.html', '.json'))]
        return jsonify({"visualizations": files})
    return jsonify({"visualizations": []})

@app.route('/visualizations/<filename>')
def get_visualization(filename):
    """Serve visualization files"""
    viz_dir = 'visualizations'
    if os.path.exists(viz_dir):
        return send_from_directory(viz_dir, filename)
    return jsonify({"error": "Visualization not found"}), 404

@app.route('/analytics/report')
def get_analytics_report():
    """Get statistical report for research"""
    report_path = 'visualizations/statistical_report.json'
    if os.path.exists(report_path):
        with open(report_path, 'r') as f:
            report = json.load(f)
        return jsonify(report)
    return jsonify({"error": "Report not found"}), 404

@app.route('/analytics/generate', methods=['POST'])
def generate_analytics():
    """Generate new visualizations and analytics"""
    try:
        # Import visualization generator
        from visualization_analyzer import generate_all_visualizations
        from sklearn.model_selection import train_test_split
        import numpy as np
        
        if model is None:
            return jsonify({"error": "Model not loaded"}), 500
        
        # Generate sample data for visualization
        from simple_model_runner import generate_training_data
        X_train, y_train = generate_training_data(500)
        
        # Generate test data
        X_features = model.extract_features(X_train)
        X_train_viz, X_test_viz, y_train_viz, y_test_viz = train_test_split(
            X_features, y_train, test_size=0.2, random_state=42
        )
        
        # Make predictions
        predictions_viz = model.model.predict(X_test_viz)
        
        # Generate visualizations
        generated_files, report = generate_all_visualizations(
            model.model, 
            X_train, 
            test_data=(X_test_viz, y_test_viz, predictions_viz)
        )
        
        return jsonify({
            "status": "success",
            "generated_files": generated_files,
            "report": report
        })
        
    except Exception as e:
        return jsonify({"error": f"Failed to generate analytics: {str(e)}"}), 500

@app.route('/analytics/dashboard')
def get_dashboard_data():
    """Get data for research dashboard"""
    try:
        # Sample dashboard data for research
        dashboard_data = {
            "model_metrics": {
                "accuracy": 88.5,
                "precision": 86.2,
                "recall": 87.1,
                "f1_score": 86.6
            },
            "career_distribution": {
                "Software Developer": 18,
                "Data Scientist": 22,
                "UX Designer": 12,
                "Project Manager": 15,
                "Business Analyst": 13,
                "Marketing Specialist": 8,
                "Healthcare Administrator": 7,
                "Financial Analyst": 5
            },
            "user_satisfaction": {
                "very_satisfied": 42,
                "satisfied": 35,
                "neutral": 15,
                "dissatisfied": 6,
                "very_dissatisfied": 2
            },
            "feature_importance": {
                "Skills Match": 35,
                "Interest Alignment": 28,
                "Experience Level": 22,
                "Education Background": 15
            }
        }
        
        return jsonify(dashboard_data)
        
    except Exception as e:
        return jsonify({"error": f"Failed to get dashboard data: {str(e)}"}), 500

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
    print("📊 Analytics endpoints available:")
    print("  GET /analytics/report - Statistical report")
    print("  GET /analytics/dashboard - Dashboard data") 
    print("  POST /analytics/generate - Generate new visualizations")
    print("  GET /visualizations - List visualization files")
    print("  GET /visualizations/<filename> - Get visualization file")
    app.run(debug=True, port=port)