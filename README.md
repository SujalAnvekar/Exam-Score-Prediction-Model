# 🎓 Exam Score Predictor

An interactive web application that predicts a student's exam score based on study time, attendance, and sleep habits.

## ✨ Features

* **Study Hours:** Select daily study hours using a slider.
* **Attendance:** Select attendance percentage using a slider.
* **Sleep Hours:** Select average sleep per night using a slider.
* **Sleep Quality:** Choose your sleep quality.
* **Study Method:** Select your preferred study method.
* **Score Prediction:** Get an estimated exam score.
* **Personalized Feedback:** Receive suggestions to improve your performance.
* **Interactive Interface:** Responsive design with sliders, buttons, and animated results.
* **Reset Option:** Clear the inputs and start again.

## 🛠️ Technologies Used

* HTML
* CSS
* JavaScript

## 🚀 How to Run the Project

1. Create a folder named `Exam-Score-Predictor`.
2. Create a file named `index.html`.
3. Paste your frontend HTML, CSS, and JavaScript code into `index.html`.
4. Save the file.
5. Open `index.html` in your web browser.
6. Select your study hours, attendance, and sleep hours.
7. Choose your sleep quality and study method.
8. Click the **Predict Score** button to see your estimated result.

## 📊 Input Parameters

| Parameter     | Description                             |
| ------------- | --------------------------------------- |
| Study Hours   | Number of hours spent studying per day  |
| Attendance    | Percentage of classes attended          |
| Sleep Hours   | Average number of hours slept per night |
| Sleep Quality | Student's self-reported sleep quality   |
| Study Method  | Student's preferred study technique     |

## 🧠 How It Works

The frontend collects the student's information and uses a sample JavaScript formula to calculate an estimated exam score.

**Important:** The current prediction is based on a demonstration formula. It is not a trained machine learning model, and its predictions should not be treated as accurate academic forecasts.

To generate predictions using machine learning, connect the frontend to a backend API that loads a trained model.

## 🔌 Connecting a Machine Learning Model

For a real prediction system, you can build a backend using Python and Flask or FastAPI.

Example request:

```json
{
  "study_hours": 5,
  "attendance": 85,
  "sleep_hours": 7,
  "sleep_quality": "Good",
  "study_method": "Practice Questions"
}
```

Example JavaScript request:

```javascript
fetch("http://127.0.0.1:8000/predict", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    study_hours: 5,
    attendance: 85,
    sleep_hours: 7,
    sleep_quality: "Good",
    study_method: "Practice Questions"
  })
})
  .then(response => response.json())
  .then(data => {
    console.log("Predicted score:", data.predicted_score);
  })
  .catch(error => {
    console.error("Prediction failed:", error);
  });
```

The backend must implement the `/predict` endpoint and return a prediction in the expected JSON format.

## 📁 Project Structure

```text
Exam-Score-Predictor/
│
├── index.html
└── README.md
```

If you add a machine learning backend later, you can extend the structure:

```text
Exam-Score-Predictor/
│
├── index.html
├── README.md
└── backend/
    ├── app.py
    └── model.pkl
```

## 🔮 Future Improvements

* Integrate a trained machine learning model.
* Store student information and prediction history.
* Add charts to visualize study habits and predicted scores.
* Improve prediction accuracy using a suitable dataset.
* Add user registration and login.
* Make the interface more accessible and mobile-friendly.

## 📄 License

This project is intended for educational and demonstration purposes. Add a license file if you plan to distribute the project publicly.
