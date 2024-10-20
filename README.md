# Network Traffic Classifier

An AI-powered **Network Traffic Classifier** designed to predict and categorize network traffic behaviors based on input CSV data. This project simplifies the process of analyzing network traffic, helping security professionals identify patterns that may indicate threats or anomalous activities. With a sleek web interface, it ensures ease of use for anyone managing network data.

---

# Team Members

- Lekhyasree Medarametla - PES1UG23CS328 [Github](https://github.com/Lekhya25)
- Pranav Rajesh Narayan - PES1UG23CS435 [Github](https://github.com/pranav-rn)
- Pranav Hemanth - PES1UG23CS433 [Github](https://github.com/Pranavh-2004)
- Kshitij Koushik Kota - PES1UG23CS908 [Github](https://github.com/kshitijkota)
- Sampriti Saha - PES1UG23CS505 [Github](https://github.com/Sampriti2803)
- Roshini Ramesh - PES1UG23CS488 [Github](https://github.com/roshr22)

---

# 📋 Project Description

This Network Traffic Classifier allows users to upload network traffic data (in CSV format) and obtain predictions. It utilizes machine learning models to classify network activity into various categories, enabling security teams to monitor, analyze, and act on network patterns effectively.

---

## 📊 Flowchart

![Flowchart](Assets/Flowchart.png)

---

# 🎯 Target Audience

- Small and Medium Enterprises (SMEs): Enhance security without requiring extensive resources.
- IT Security Professionals: Equip teams with advanced threat detection tools.
- Regulatory Bodies: Facilitate compliance with data protection laws.
- Educational Institutions: Protect sensitive academic and student data.

---

# ⚙️ Proposed Solution Features

1. File Upload & Prediction

Allows users to upload CSV files containing network traffic data.

2. Machine Learning Algorithms

- Algorithms can predict network activity labels based on the input data.
- Random Forest: Handles large datasets with many features.
- Support Vector Machine (SVM): Ideal for binary classification tasks.
- Neural Networks: Detects complex patterns in high-dimensional data.

3. Result Visualization

Displays predictions on a user-friendly web interface, listing true and predicted labels.

4. Alert Mechanism (Future Enhancement)

Future updates will include real-time alerts for suspicious activities.

---

# 📊 Data Requirements

    •	UNSW-NB15 Dataset: Comprehensive dataset with a wide range of attack scenarios and normal network traffic.
    •	CIC-IDS2017 Dataset: Real-world traffic scenarios for effective testing and validation.

---

## Setup

1. Generate a new ssh key and add it to github
   [Follow this video](https://www.youtube.com/watch?v=O5H_KFzla6M)

2. Clone the repo

```bash
git clone https://github.com/Pranavh-2004/T3N50R5.git
cd T3N50R5
```

3. Create a branch with your name and switch to it

```bash
git branch "your_name"
git switch "your_name"
git status #to check if u have switched to your branch
```

4. To check if you are able to push changes to github, edit this README.md file with some new text (it can be anything).
   And then push the changes to github

```bash
git config --global user.email "change this with your github email id"
git config --global user.name "change this with your github username"
git add README.md
git commit -m "Updated the readme file"
git push origin main
```

5. To push and pull changes

```bash
git pull origin main  #pulls latest code from the repo
git push origin "your_name" #pushes your commits to your branch in the repo
```

**Never push to main!! And NEVER FORCE PUSH TO MAIN**

6. Install dependencies

```bash
pip install -r requirements.txt
```

7. Start Python Backend

```bash
python model_server.py
```

8. Start Node.js Server:

```bash
node server.js
```

9. Check setup - open [http://localhost:3000](http://localhost:3000) in browser

---

# 💡 Future Enhancements

- Extend support for more datasets.
- Add advanced alerting features with SMS/Email notifications.
- Implement reinforcement learning for adaptive detection.

---

# 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.
