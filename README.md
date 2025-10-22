# Career Compass: AI-Enhanced Career Guidance System

![Career Compass Logo](https://img.shields.io/badge/Career-Compass-blue)
![Version](https://img.shields.io/badge/version-1.0.0-green)
![License](https://img.shields.io/badge/license-MIT-orange)

## 🚀 Overview

Career Compass is an innovative AI-powered career guidance platform designed to provide personalized career pathways for students and professionals. The system leverages machine learning algorithms to analyze an individual's aptitude, aspirations, skills, and work experience to recommend tailored career options and future progression opportunities.

## 🎯 Problem Statement

Traditional career counseling methods often lack personalization and fail to fully account for an individual's unique profile. Career Compass addresses this challenge by creating an intelligent system that provides personalized, dynamic, and future-oriented career recommendations.

## ✨ Key Features

- **Aptitude Assessment:** AI-driven tools that assess an individual's natural aptitudes and strengths
- **Aspiration Analysis:** Captures and analyzes the user's career aspirations, interests, and values
- **Skill Mapping:** Evaluates current abilities and experiences against potential career paths
- **Future Progression Planning:** Uses predictive analytics to identify future career opportunities
- **Skill Gap Analysis:** Highlights gaps and suggests targeted learning opportunities
- **User-Friendly Interface:** Intuitive design accessible for users at all educational levels

## 🛠️ Technology Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **Machine Learning:** scikit-learn, NumPy, Pandas
- **Model Types:** Gradient Boosting Classifier, Random Forest Classifier
- **Data Processing:** TF-IDF Vectorization, Standard Scaling, SVD

## 📋 Installation & Setup

### Prerequisites
- Python 3.7+
- pip package manager
- Modern web browser

### Setup Instructions

1. **Clone the repository**
   ```
   git clone https://github.com/Subrata3841/AI-Career-Guidance-System.git
   cd career-compass
   ```

2. **Set up a virtual environment (optional but recommended)**
   ```
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install required packages**
   ```
   pip install -r requirements.txt
   ```

4. **Run the application**
   
   For Windows:
   ```
   run_career_compass.bat
   ```
   
   For PowerShell:
   ```
   .\Run-CareerCompass.ps1
   ```

5. **Access the application**
   
   The application will be available at:
   - API Server: http://localhost:5000
   - Frontend: Will automatically open in your default browser

## 🖥️ Usage

1. Fill out the career assessment form with your skills, interests, education level, and experience
2. Submit the form to receive personalized career recommendations
3. Explore recommended career paths and progression opportunities
4. Review suggested skill development areas to enhance your career prospects

## 🧪 Project Structure

```
career-compass/
│
├── career_recommendation_model.joblib  # Pre-trained ML model
├── career-recommendation-model.py      # Model training script
├── simple_model_runner.py             # Simplified model runner
├── simple_api_server.py               # Flask API server
├── career-guidance-backend.py         # Advanced backend implementation
├── simple_frontend.html               # Basic UI implementation
├── career-guidance-frontend.tsx       # Advanced React frontend
├── run_career_compass.bat             # Windows batch startup script
└── Run-CareerCompass.ps1              # PowerShell startup script
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

<p align="center">Made with ❤️ for empowering career decisions</p>
