<h1 >
  🤖 ZERO: The Intelligent Multilingual Calculator
</h1>

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/NLP-Natural_Language-green?style=for-the-badge" />
</p><br>

<p align="left">
  <strong>ZERO</strong> is a Python-based, command-line intelligent assistant designed to bridge the gap between human language and mathematical computation. Unlike a standard calculator, it uses Natural Language Processing (NLP) logic to interpret commands in both <b>English</b> and <b>Malay</b>, making math more intuitive for regional users.
</p>


## ✨ Technical Architecture & Key Features

### 1️⃣ Intent Recognition & NLP Logic
Instead of relying on rigid syntax, ZERO identifies user "intent" by scanning input against bilingual keyword banks.
* **Contextual Awareness:** The system detects the language of the request and dynamically adjusts its response language (EN or MY).
* **Regex-Based Extraction:** Uses Regular Expressions to isolate numerical data from conversational text (e.g., extracting `16` from *"What is the square root of 16?"*).

### 2️⃣ Robustness & User Experience
* **Auto-Correction Engine:** Built-in spelling correction for common typos (e.g., `squar` → `square`, `tamba` → `tambah`).
* **Interactive Confirmation:** Implements a confirmation loop for ambiguous inputs to ensure calculation accuracy.
* **Data Persistence:** Integrated with `CSV` and `Pandas` to log, store, and display calculation history with timestamps.

### 3️⃣ Advanced Operations
Supports standard arithmetic plus:
* **Advanced Math:** Square roots (`√`), Exponents (`^`), and Factorials (`!`).
* **Input Validation:** Handles edge cases like division by zero and non-numeric factorial requests.
<br>

## 📂 Project Structure
```text
├── CSV/
│   └── calculate_history.csv    # Persistent data storage
├── Project.py                   # Core application logic
└── README.md                    # Project documentation
```
<br>


##  How to Use

**ZERO** is designed to be conversational. Once prompted with *"How can I help you?"*, you can use various input styles:

| Input Style | User Command | Assistant Response |
| :--- | :--- | :--- |
| **Natural English** | *"Can you help me add 10 and 5?"* | *"Got it! The result is 15"* |
| **Natural Malay** | *"Berapa punca kuasa dua 144?"* | *"Mesti boleh! Hasilnya adalah 12"* |
| **Mathematical** | `(20 * 4) + 5` | *"Done! Here is the total: 85"* |
| **System** | *"Show calculation history"* | *[Displays formatted Pandas table]* |

> [!TIP]
> **To Exit:** Simply type `Exit` to end the session.
<br>

## Demo Display
<div >
  <img width="640" height="904" alt="image" src="https://github.com/user-attachments/assets/69b2c6b0-820a-49a9-8ac4-ebfe6e97b061" />
  <br>
</div><br><br>

<div >
  <img width="640" height="827" alt="image" src="https://github.com/user-attachments/assets/77a08650-abe7-4402-b183-40012f560638" />
  <br>
</div><br>




## Contact
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/steven0908)
[![Jobstreet](https://img.shields.io/badge/Jobstreet-003580?style=for-the-badge&logo=target&logoColor=white)](https://my.jobstreet.com/profiles/steven-gohyishen-97x9Q8tbmm)

> **Degree Project** &nbsp; | &nbsp; Completed on Jul 28, 2025  
> *Developed with passion for Software Engineering.*
