# 🎥 AI YouTube Video Analyzer

## 📌 Overview

This project is an **AI-powered YouTube Video Analyzer** built using **Agentic AI**. It uses an intelligent agent to extract video captions and generate meaningful insights such as summaries and key points.

The system combines a **tool-using agent (Agno)** with a **Large Language Model (Groq)** to analyze video content in a structured way.

---

## 🚀 Features

* 🔗 Accepts YouTube video links as input
* 📄 Extracts captions using built-in tools
* 🤖 Uses Agentic AI for reasoning and analysis
* 🧠 Generates:

  * Summary
  * Key Points
  * Insights
* 🖥️ Interactive UI built with Streamlit

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit** (Frontend UI)
* **Agno** (Agent framework)
* **Groq LLM** (qwen/qwen3-32b)
* **YouTubeTools** (for caption extraction)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

---

### 2️⃣ Create virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Create `.env` file

Create a `.env` file in the root directory and add:

```env
GROQ_API_KEY=your_api_key_here
```

---

### 5️⃣ Run the app

```bash
streamlit run ui.py
```

---

## 📂 Project Structure

```
youtube-video-analyzer/
├── ui.py
├── yt_analyzer.py
├── requirements.txt
├── .gitignore
├── .env.example
└── README.md
```

---

## 🧠 How It Works

1. User enters a YouTube video link
2. Agent uses **YouTubeTools** to fetch captions
3. Captions are passed to the **Groq LLM**
4. LLM generates structured analysis
5. Results are displayed in Streamlit UI

---

## ⚠️ Limitations

* Works best with **English captions only**
* May not work if captions are unavailable
* Depends on internet and API availability

---

## 🔮 Future Improvements

* 🌐 Multi-language (Hindi + English) support
* 💬 Chat with video feature
* 📄 Download analysis as PDF
* 🧠 Memory-enabled agent
* 🔍 Advanced insights (sentiment, topics)

---

## 🙌 Acknowledgements

* Agno (Agent Framework)
* Groq LLM
* Streamlit

---

## 📬 Contact

Feel free to connect or suggest improvements!

---

⭐ If you like this project, consider giving it a star!
