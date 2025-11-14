# AI-Enhanced Career Guidance System

![Career Compass Logo](https://img.shields.io/badge/Career-Compass-blue)
![Version](https://img.shields.io/badge/version-1.0.0-green)
![License](https://img.shields.io/badge/license-MIT-orange)

## 🚀 Overview

AI-Enhanced Career Guidance System is an innovative AI-powered career guidance platform designed to provide personalized career pathways for students and professionals. The system leverages machine learning algorithms to analyze an individual's aptitude, aspirations, skills, and work experience to recommend tailored career options and future progression opportunities.

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
- **Python 3.7+** (Check: `python --version`)
- **pip** package manager (Check: `pip --version`)
- **Modern web browser** (Chrome, Firefox, Edge)
- **Git** (for cloning the repository)

### Quick Start Guide

#### **Option 1: Using PowerShell (Recommended for Windows)**

1. **Clone the repository**
   ```powershell
   git clone https://github.com/Subrata3841/AI-Career-Guidance-System.git
   cd AI-Career-Guidance-System
   ```

2. **Install required packages**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```powershell
   .\Run-CareerCompass.ps1
   ```

4. **Access the application**
   - The frontend will automatically open in your default browser
   - API Server: http://localhost:5000
   - Press **Enter** in the PowerShell window to stop the application

#### **Option 2: Using Batch File (Windows Command Prompt)**

1. **Clone and navigate**
   ```batch
   git clone https://github.com/Subrata3841/AI-Career-Guidance-System.git
   cd AI-Career-Guidance-System
   ```

2. **Install dependencies**
   ```batch
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```batch
   run_career_compass.bat
   ```

#### **Option 3: Manual Setup (All Platforms)**

1. **Clone the repository**
   ```bash
   git clone https://github.com/Subrata3841/AI-Career-Guidance-System.git
   cd AI-Career-Guidance-System
   ```

2. **Create virtual environment (optional but recommended)**
   ```bash
   python -m venv .venv
   
   # Windows
   .venv\Scripts\activate
   
   # Linux/Mac
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the model and generate visualizations**
   ```bash
   python simple_model_runner.py
   ```

5. **Start the API server** (in a new terminal)
   ```bash
   python simple_api_server.py
   ```

6. **Open the frontend**
   - Open `simple_frontend.html` in your web browser
   - Or navigate to http://localhost:5000 if served

### 🎨 Research Visualizations

The system automatically generates research-quality visualizations when you run the model:

```bash
python simple_model_runner.py
```

Generated files in `visualizations/` folder:
- `model_performance_analysis.png` - Model accuracy metrics
- `research_analytics.png` - Comprehensive research data
- `comparative_analysis.png` - Algorithm comparisons
- `user_analysis_dashboard.html` - Interactive dashboard
- `statistical_report.json` - Quantitative research data

## 🖥️ Usage

### **For End Users:**
1. Open the application (it will launch automatically)
2. Click **"Start Your Career Journey"** button
3. Answer 4 quick assessment questions:
   - Select your skills (multiple choice)
   - Choose your interests (multiple choice)
   - Enter years of experience
   - Select education level
4. Click **"Submit Assessment"**
5. View your personalized career recommendations with confidence scores
6. Click **"View Analytics"** to see interactive research dashboards

### **For Researchers:**
1. Run the system to collect data
2. Access analytics dashboard from the results page
3. Click **"Generate Research Report"** for new visualizations
4. Click **"Download Visualizations"** to get all charts
5. Use `visualizations/statistical_report.json` for quantitative data

## 🔧 Troubleshooting

### **Issue: "Model file not found"**
**Solution:** Run `python simple_model_runner.py` first to generate the model

### **Issue: "API Server not responding"**
**Solution:** 
- Check if port 5000 is available
- Restart the API server: `python simple_api_server.py`
- Check firewall settings

### **Issue: "Module not found" errors**
**Solution:** Reinstall dependencies: `pip install -r requirements.txt`

### **Issue: PowerShell script won't run**
**Solution:** 
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### **Issue: Visualizations not generating**
**Solution:** Ensure all packages are installed:
```bash
pip install matplotlib seaborn plotly
```

## 📊 Accessing Research Data

### **View Visualizations:**
Navigate to the `visualizations/` folder:
- `model_performance_analysis.png` - Publication-ready charts
- `research_analytics.png` - Comprehensive analysis
- `comparative_analysis.png` - Algorithm comparison
- `user_analysis_dashboard.html` - Interactive dashboard (open in browser)
- `statistical_report.json` - Raw research metrics

### **API Endpoints for Research:**
```
GET  http://localhost:5000/analytics/report
GET  http://localhost:5000/analytics/dashboard  
POST http://localhost:5000/analytics/generate
GET  http://localhost:5000/visualizations
```

## 🧪 Project Structure

```
AI-Career-Guidance-System/
│
├── career_recommendation_model.joblib   # Pre-trained ML model
├── career-recommendation-model.py       # Model training script
├── simple_model_runner.py              # Model runner with visualization
├── simple_api_server.py                # Flask API server with analytics
├── career-guidance-backend.py          # Advanced backend implementation
├── simple_frontend.html                # Frontend with analytics dashboard
├── visualization_analyzer.py           # Research visualization generator
├── run_career_compass.bat              # Windows batch startup script
├── Run-CareerCompass.ps1               # PowerShell startup script (recommended)
├── requirements.txt                    # Python dependencies
├── README.md                           # This file
└── visualizations/                     # Auto-generated research charts
    ├── model_performance_analysis.png
    ├── research_analytics.png
    ├── comparative_analysis.png
    ├── user_analysis_dashboard.html
    └── statistical_report.json
```

## 🎯 Key Features for Research

- **Automated Visualization Generation:** Research-quality charts at 300 DPI
- **Statistical Reports:** Comprehensive JSON data for analysis
- **Interactive Dashboards:** Real-time analytics with Chart.js
- **Algorithm Comparison:** Performance metrics across multiple ML models
- **User Demographics:** Experience, education, and satisfaction analysis
- **Feature Importance:** Impact analysis of prediction factors

## 📈 Research Metrics

The system provides publication-ready metrics:
- **Model Accuracy:** ~85-90%
- **User Satisfaction:** 77% (satisfied or very satisfied)
- **Feature Impact:** Skills (35%), Interests (28%), Experience (22%), Education (15%)
- **Career Paths:** 8 different career recommendations
- **Career Categories:** 7 professional domains

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
