# Diamond Price Prediction

A machine learning-powered web application that predicts diamond prices based on physical characteristics. Built with Flask and Scikit-learn.

[Live Demo](https://daimondpriceprediction.onrender.com)

![Diamond Price Prediction](https://img.shields.io/badge/Status-Active-success)

## 🌟 Features

- **Accurate Predictions**: Uses a trained regression model to estimate diamond prices.
- **Modern UI**: Clean, professional interface with glassmorphism and gradient design.
- **Real-time**: Instant price estimation based on carat, cut, color, clarity, and dimensions.
- **Responsive**: Fully optimized for desktop and mobile devices.

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3 (Custom Design System)
- **Backend**: Python, Flask
- **Machine Learning**: Scikit-learn, Pandas, NumPy
- **Environment**: Anaconda / Conda

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- Conda (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "Diamond Price Prediction"
   ```

2. **Create and activate the environment**
   ```bash
   conda create -n my_env python=3.11.9 -y
   conda activate my_env
   ```

3. **Install dependencies**
   ```bash
   # Essential packages
   pip install -r requirements.txt
   
   # IMPORTANT: Install specific scikit-learn version required by the model
   pip install scikit-learn==1.6.1
   ```

### Running the Application

1. **Activate the environment** (if not already active)
   ```bash
   conda activate my_env
   ```

2. **Start the server**
   ```bash
   python application.py
   ```

3. **Access the application**
   Open your browser to: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## ⚠️ Troubleshooting

**Internal Server Error on Prediction**
If you see an error when clicking "Predict":
- **Cause**: Scikit-learn version mismatch. The model requires v1.6.1.
- **Fix**: Run `pip install scikit-learn==1.6.1` inside your `my_env` environment.

**Port Already in Use**
If the application fails to start because port 5000 is busy:
- **Fix**: Open Task Manager or Terminal and kill existing python processes, or restart your computer.

## 📂 Project Structure

```
Diamond Price Prediction/
├── application.py       # Main Flask application
├── requirements.txt     # Python dependencies
├── src/                 # Source code for pipelines and utilities
│   ├── pipelines/       # Prediction and training pipelines
│   ├── components/      # Data handling components
│   └── utils.py         # Utility functions
├── static/              # CSS, JavaScript, and images
├── templates/           # HTML templates for UI
└── artifacts/           # Trained models (model.pkl, preprocessor.pkl)
```

## 📝 License

This project is licensed under the MIT License.
