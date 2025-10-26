# 🛍️ AI Conversational Sales Agent (Basic Prototype)


> **Hackathon Project — ABFRL Retail Challenge 2025**  
> 🧠 A next-generation, ethical, and intelligent **AI Sales Associate** that redefines retail interactions — blending **sales psychology, personalization, and conversational intelligence**.  
> 💬 Designed to bridge **online and in-store shopping** into one seamless, human-like experience.  
> 🚀 Built using **Google Gemini (for now), LangChain, and Streamlit** — showcasing the future of AI-driven commerce.


---

## 🚀 Overview

This project introduces an **AI Sales Agent** that helps customers discover and buy products through natural, persuasive, and human-like conversations.

The agent leverages **Google Gemini + LangChain + Streamlit** to simulate a real sales associate — understanding user intent, suggesting relevant products, and building trust using ethical sales psychology.

---

## 💡 Core Features

- 🤖 **AI-Driven Conversations:** Understands context, preferences, and buying intent.  
- 🧠 **Ethical Persuasion:** Uses real psychological principles — no manipulation or false claims.  
- 👗 **Personalized Product Discovery:** Recommends items based on user needs, budget, and style.  
- 🧾 **Natural Chat Interface:** Built with **Streamlit** for an interactive experience.  
- 🛒 **Future Integration Ready:** Can connect to Digital Twin and various worker agents 

---

## 🧩 Tech Stack

| Category | Technology |
|-----------|-------------|
| 💬 LLM | **Google Gemini (via LangChain)** |
| 🧠 Framework | **LangChain** |
| 🌐 Frontend | **Streamlit** |
| 🔐 Environment | **Python-dotenv** |
| ⚙️ Language | **Python 3.10+** |

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/<repo-name>.git
```
### 2️⃣ Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```
### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Add your API key
Create a .env file in the root directory and add:
```bash
GOOGLE_API_KEY=your_google_api_key_here

```
### 5️⃣ Run the app
```bash
streamlit run main.py
```

## 🧠 System Prompt Summary
The AI agent:
- Greets the customer by name.
- Asks qualifying questions (budget, size, occasion, etc.).
- Suggests 2–4 tailored options with benefits & social proof.
- Confirms stock, price, and delivery before closing.
- Never manipulates or deceives — builds trust to increase conversions naturally.

## 🧭 Example Use Case

>User: “Show me a blue dress under ₹800.”

>AI: “Hi there! Great choice — blue is trending this season.
Before I recommend, do you prefer something casual or more party-wear?
I can shortlist a few options that fit your budget and style.”

## 🧱 Folder Structure
```bash
📦 ai-sales-agent/
 ┣ 📄 main.py               # Streamlit app with LangChain + Gemini logic
 ┣ 📄 requirements.txt      # Dependencies
 ┣ 📄 .env.example          # Environment variable sample
 ┣ 📄 README.md             # Project documentation
 ┗ 📁 assets/               # (Optional) Images or future extensions
 ```