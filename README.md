# 🎓 JAMB Subject Combination Predictor

## 📌 Overview

The **JAMB Subject Combination Predictor** is a simple Machine Learning-inspired web application built with **Python** and **Streamlit**. The application helps Nigerian students identify the recommended **JAMB subject combination** based on their chosen university course.

Users enter a course name, and the system searches through a dataset to find the closest matching course using text similarity, then returns the appropriate JAMB subjects.

This project demonstrates practical problem-solving using data processing and similarity matching techniques in an interactive web interface.

---

## 🚀 Features

* ✅ Course-based JAMB subject recommendation
* ✅ Text similarity matching for flexible input
* ✅ Interactive Streamlit user interface
* ✅ Lightweight and fast prediction system
* ✅ Beginner-friendly ML logic implementation
* ✅ Real-time result display

---

## 🧠 How It Works

The application follows these steps:

1. User enters a course name.
2. The system compares the input with courses in the dataset.
3. A text similarity function calculates matching scores.
4. The closest matching course is selected.
5. Recommended JAMB subjects are displayed to the user.

The similarity score is calculated using word overlap between the user input and dataset entries.

---

## 🛠️ Technologies Used

* Python
* Pandas
* Streamlit

---

## 📂 Project Structure

```
jamb-subject-predictor/
│
├── app.py
├── jamb_subjets_data.csv
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation and Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/jamb-subject-predictor.git
cd jamb-subject-predictor
```

### 2️⃣ Create Virtual Environment (Optional)

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Run the Streamlit app with:

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## 📊 Input Example

```
Computer Science
Medicine and Surgery
Electrical Engineering
```

---

## 📈 Future Improvements

* Improved NLP similarity matching
* Support for course synonyms
* Deployment to Streamlit Cloud
* Mobile-friendly UI improvements
* Expanded course dataset

---

## 👨‍💻 Author

**Najari Umar Jibril**
Machine Learning Engineer
Focused on building practical AI solutions for education and real-world applications.

---

## 📜 License

This project is open-source and available under the MIT License.
