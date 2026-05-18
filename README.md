# 🤖 AI Recommendation Logic — Tech Stack Recommender

A content-based AI recommendation system that maps user skills
to the most relevant career paths using TF-IDF vectorization
and Cosine Similarity mathematics.
Built as Project 3 of my AI Engineering journey at DecodeLabs Batch 2026.

---

## 📌 Project Overview

This project builds a intelligent recommendation engine that
acts as a "Digital Matchmaker" — taking a user's raw skills
as input and recommending the Top 3 most relevant tech career
paths using pure similarity mathematics. No random suggestions.
Just pattern alignment.

---

## 🎯 Goal

Create a simple recommendation system based on user preferences
that matches skills to job roles using Content-Based Filtering.

---

## ✅ Key Requirements Completed

- ✔️ Takes minimum 3 user skill inputs
- ✔️ Converts skills to TF-IDF weighted vectors
- ✔️ Matches preferences using Cosine Similarity
- ✔️ Displays Top 3 recommended career paths with match scores
- ✔️ Implements complete 4-step ranking pipeline

---

## 🧠 Key Skills Learned

- ✅ Content-Based Filtering concepts
- ✅ TF-IDF (Term Frequency-Inverse Document Frequency)
- ✅ Cosine Similarity mathematics
- ✅ Vector space modeling
- ✅ 4-Step Ranking Pipeline (Ingest → Score → Sort → Filter)
- ✅ Pattern matching & recommendation logic
- ✅ Real-world AI recommendation concepts

---

## 🛠️ Technologies Used

| Tool | Purpose |
|---|---|
| Python 3.x | Core programming language |
| Scikit-learn | TF-IDF & Cosine Similarity |
| NumPy | Vector mathematics |
| Pandas | Data handling |
| VS Code | Development environment |

---

## 📂 Project Structure


---

## 🔧 How the Pipeline Works

---

## 💼 Job Roles in Dataset

| Job Role | Key Skills |
|---|---|
| Data Scientist | Python, ML, SQL, Statistics |
| AI Engineer | Deep Learning, TensorFlow, NLP |
| Web Developer | HTML, CSS, JavaScript, React |
| DevOps Engineer | AWS, Docker, Kubernetes |
| Backend Developer | Python, Java, APIs, Databases |
| Frontend Developer | React, Vue, TypeScript, UI/UX |
| Cloud Architect | AWS, Azure, Infrastructure |
| Data Analyst | SQL, Excel, Power BI |
| Cybersecurity Analyst | Networking, Linux, Ethical Hacking |
| Mobile Developer | Flutter, React Native, Android |

---

## ▶️ How to Run

1. Make sure Python is installed
2. Install required libraries:
```bash
pip install scikit-learn pandas numpy
```
3. Clone this repository:
```bash
git clone https://github.com/farheenrafiq20056-svg/task-3-farheenrafiq.git
```
4. Navigate to project folder:
```bash
cd task-3-farheenrafiq
```
5. Run the recommender:
```bash
python recommender.py
```

---

## 💬 Sample Output

---

## 🔍 The Math Behind It

**TF-IDF** converts skills into weighted numbers:
- Common skills get LOW weight
- Unique/specific skills get HIGH weight

**Cosine Similarity** measures alignment:
- Score 1.0 = Perfect match 🎯
- Score 0.0 = No match ❌

---

## 🚀 Future Improvements

- [ ] Add user rating system for preferences
- [ ] Include salary data for each role
- [ ] Build web interface using Flask
- [ ] Add collaborative filtering
- [ ] Connect to LinkedIn Jobs API
- [ ] Export recommendations as PDF report

---

## 👩‍💻 Author

**Farheen Rafiq**
- 🔗 LinkedIn: [https://www.linkedin.com/in/farheen-rafiq-682316281/]
- 🐙 GitHub: [https://github.com/farheenrafiq20056-svg](https://github.com/farheenrafiq20056-svg)
- 🏢 AI Engineering Intern at DecodeLabs — Batch 2026

---

## 📃 License

This project is open source and available under the
[MIT License](LICENSE).

---

⭐ If you found this helpful, please give it a star!