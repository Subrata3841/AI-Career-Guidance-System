import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

print("Creating a simplified career recommendation model with sample data...")

# Define possible career paths
career_paths = [
    'Software Developer', 
    'Data Scientist', 
    'UX Designer', 
    'Project Manager',
    'Business Analyst', 
    'Marketing Specialist', 
    'Healthcare Administrator', 
    'Financial Analyst'
]

# Create a simple model class
class SimpleCareerModel:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.career_paths = career_paths
        
        # Map skill keywords to numerical features
        self.skill_map = {
            'programming': 0, 'coding': 0, 'development': 0, 'software': 0, 'python': 0, 'java': 0,
            'data': 1, 'analysis': 1, 'statistics': 1, 'analytics': 1, 'research': 1,
            'design': 2, 'ui': 2, 'ux': 2, 'graphic': 2, 'creative': 2, 'visual': 2,
            'management': 3, 'leadership': 3, 'coordination': 3, 'planning': 3, 'organization': 3,
            'business': 4, 'finance': 4, 'economics': 4, 'accounting': 4,
            'marketing': 5, 'communication': 5, 'content': 5, 'writing': 5,
            'healthcare': 6, 'medical': 6, 'clinical': 6, 'patient': 6,
            'finance': 7, 'financial': 7, 'investment': 7, 'banking': 7
        }
        
        # Map interest keywords to numerical features
        self.interest_map = {
            'technology': 0, 'tech': 0, 'computers': 0, 'software': 0, 'programming': 0,
            'science': 1, 'research': 1, 'data': 1, 'analysis': 1, 'mathematics': 1,
            'art': 2, 'design': 2, 'creative': 2, 'visual': 2,
            'business': 3, 'management': 3, 'leadership': 3, 'entrepreneurship': 3,
            'healthcare': 4, 'medical': 4, 'patient': 4, 'care': 4, 'health': 4,
            'education': 5, 'teaching': 5, 'learning': 5, 'training': 5,
            'finance': 6, 'investment': 6, 'banking': 6, 'economics': 6,
            'engineering': 7, 'building': 7, 'construction': 7, 'mechanical': 7
        }

    def extract_features(self, data):
        """Extract numerical features from text data"""
        # Initialize feature vector for each sample
        features = []
        
        for _, row in data.iterrows():
            # Initialize feature vector with zeros
            feature_vector = [0] * 20  # 8 for skill categories, 8 for interest categories, 2 for experience and education
            
            # Process skills
            if 'skills' in row:
                skills = row['skills'].lower().split()
                for skill in skills:
                    if skill in self.skill_map:
                        feature_vector[self.skill_map[skill]] += 1
            
            # Process interests
            if 'interests' in row:
                interests = row['interests'].lower().split()
                for interest in interests:
                    if interest in self.interest_map:
                        feature_vector[8 + self.interest_map[interest]] += 1
            
            # Add experience and education features
            if 'years_of_experience' in row:
                feature_vector[16] = min(row['years_of_experience'], 15) / 15  # Normalize to 0-1
                
            if 'education_level_encoded' in row:
                feature_vector[17] = row['education_level_encoded'] / 5  # Normalize to 0-1
                
            features.append(feature_vector)
            
        return np.array(features)

    def train(self, X_data, y_data):
        """Train the model on given data"""
        print("Training the model...")
        X = self.extract_features(X_data)
        y = y_data
        self.model.fit(X, y)
        return self

    def predict(self, user_data):
        """Predict career recommendations for user data"""
        X = self.extract_features(user_data)
        probs = self.model.predict_proba(X)[0]
        
        # Convert to recommendations format
        results = []
        for i in range(len(probs)):
            confidence = round(probs[i] * 100, 1)  # Convert to percentage
            results.append({
                'career_path': self.career_paths[i],
                'confidence_score': confidence
            })
        
        # Sort by confidence score
        results.sort(key=lambda x: x['confidence_score'], reverse=True)
        return [results]  # Maintain compatibility with original format

    def save_model(self, path):
        """Save the model to a file"""
        print(f"Saving the model to {path}...")
        joblib.dump(self, path)
        print("Model saved successfully!")

    @classmethod
    def load_model(cls, path):
        """Load the model from a file"""
        print(f"Loading model from {path}...")
        return joblib.load(path)

# Generate synthetic training data
def generate_training_data(num_samples=1000):
    print("Generating synthetic training data...")
    
    data = []
    labels = []
    
    # Define skill sets for different career paths
    career_skill_sets = {
        0: ['programming', 'coding', 'development', 'software', 'python', 'java'],
        1: ['data', 'analysis', 'statistics', 'analytics', 'research', 'python'],
        2: ['design', 'ui', 'ux', 'graphic', 'creative', 'visual'],
        3: ['management', 'leadership', 'coordination', 'planning', 'organization'],
        4: ['analysis', 'business', 'research', 'data', 'requirements'],
        5: ['marketing', 'communication', 'content', 'writing', 'social'],
        6: ['healthcare', 'management', 'organization', 'medical', 'patient'],
        7: ['financial', 'finance', 'analysis', 'accounting', 'economics']
    }
    
    # Define interest sets for different career paths
    career_interest_sets = {
        0: ['technology', 'tech', 'computers', 'software', 'programming'],
        1: ['science', 'research', 'data', 'analysis', 'mathematics'],
        2: ['art', 'design', 'creative', 'visual'],
        3: ['business', 'management', 'leadership', 'entrepreneurship'],
        4: ['business', 'data', 'analysis', 'research'],
        5: ['marketing', 'business', 'communication', 'social'],
        6: ['healthcare', 'medical', 'patient', 'care', 'health'],
        7: ['finance', 'investment', 'banking', 'economics']
    }
    
    # Generate data for each career path
    for _ in range(num_samples):
        # Choose a random career path
        career_idx = np.random.randint(0, len(career_paths))
        
        # Generate skills for this career
        main_skills = np.random.choice(career_skill_sets[career_idx], size=np.random.randint(2, 5), replace=False)
        # Add some random skills
        other_skills = np.random.choice(
            [s for i, skills in career_skill_sets.items() for s in skills if i != career_idx],
            size=np.random.randint(0, 3),
            replace=False
        )
        all_skills = ' '.join(np.concatenate([main_skills, other_skills]))
        
        # Generate interests for this career
        main_interests = np.random.choice(career_interest_sets[career_idx], size=np.random.randint(1, 3), replace=False)
        # Add some random interests
        other_interests = np.random.choice(
            [i for idx, interests in career_interest_sets.items() for i in interests if idx != career_idx],
            size=np.random.randint(0, 2),
            replace=False
        )
        all_interests = ' '.join(np.concatenate([main_interests, other_interests]))
        
        # Generate experience and education
        years_exp = np.random.randint(0, 16)
        education = np.random.randint(1, 6)
        
        # Add noise to make it more realistic
        if np.random.random() < 0.1:  # 10% chance of noise
            career_idx = np.random.randint(0, len(career_paths))
        
        # Create a sample
        data.append({
            'skills': all_skills,
            'interests': all_interests,
            'years_of_experience': years_exp,
            'education_level_encoded': education
        })
        labels.append(career_idx)
    
    return pd.DataFrame(data), np.array(labels)

# Train and save the model
X_train, y_train = generate_training_data(1000)
model = SimpleCareerModel()
model.train(X_train, y_train)
model_path = 'career_recommendation_model.joblib'
model.save_model(model_path)

# Generate visualizations for research
print("\n🎨 Generating research visualizations...")
try:
    from visualization_analyzer import generate_all_visualizations
    
    # Generate test data for visualizations
    from sklearn.model_selection import train_test_split
    X_features = model.extract_features(X_train)
    X_train_viz, X_test_viz, y_train_viz, y_test_viz = train_test_split(
        X_features, y_train, test_size=0.2, random_state=42
    )
    
    # Make predictions for visualization
    predictions_viz = model.model.predict(X_test_viz)
    
    # Generate all visualizations
    generated_files, report = generate_all_visualizations(
        model.model, 
        X_train, 
        test_data=(X_test_viz, y_test_viz, predictions_viz)
    )
    
    print("✅ Research visualizations generated successfully!")
    print(f"📊 Files saved in 'visualizations/' directory")
    
except ImportError as e:
    print("⚠️  Visualization libraries not installed. Run: pip install -r requirements.txt")
except Exception as e:
    print(f"⚠️  Error generating visualizations: {e}")

# Test the model with a sample user
print("\nTesting the model with a sample user...")
sample_user = pd.DataFrame([{
    'skills': 'python data analysis research',
    'interests': 'technology science data',
    'years_of_experience': 3,
    'education_level_encoded': 3  # Master's degree
}])

# Load the model and predict
loaded_model = SimpleCareerModel.load_model(model_path)
recommendations = loaded_model.predict(sample_user)

print("\nTop career recommendations for the sample user:")
for i, career in enumerate(recommendations[0][:3]):
    print(f"{i+1}. {career['career_path']}: {career['confidence_score']}% confidence")

print("\nModel is ready for use with the frontend!")
print("📈 Research visualizations and analytics are available for your paper!")