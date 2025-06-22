# 📚 Automated Book Publication Workflow

An AI-powered pipeline to automate the process of extracting book chapters from the web, generating rewritten content using large language models (LLMs), performing human-in-the-loop editing, and storing the final versions with searchable version control.

---

## ✨ Features

- 🔍 **Web Scraping**: Extract content from a Wikisource chapter using Playwright.
- 🤖 **AI Writing**: Spin content with Google's Gemini model.
- 📋 **AI Review**: Refine the spun content with another AI pass.
- 👨‍💻 **Human-in-the-Loop Interface**: Use a Streamlit interface to review and edit the content.
- 🧠 **Versioning with ChromaDB**: Store finalized versions with metadata and searchability.
- 🧪 **RL-based Document Retrieval**: Reinforcement Learning-inspired scoring and retrieval of best versions.

---

## 🚀 How to Run

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
playwright install
```

### 2️⃣ Run the pipeline
```bash
python main.py
```
This will:

- Scrape the original chapter
- Spin and review it using Gemini
- Save intermediate outputs for manual review

### 3️⃣ Open the Streamlit human review UI
```bash
streamlit run interface/human_review_interface.py
```
- Review the AI-generated content side-by-side with the original.
- Edit and save the final version to final_output/.

### 4️⃣ Press ENTER in the original terminal and provide the filename when prompted.

---

## 💾 Example Final Output
- After saving the edited content from the UI as final_output.txt, it will be:
- Stored in ChromaDB
- Tagged with document ID: gates_of_morning_chapter_01
- Scored for quality via RL logic in rl_search.py

---

## 🧠 Models & Tools Used
- Gemini (Free Model): Text generation and review
- ChromaDB: Versioned document storage
- Sentence-Transformers: For semantic embedding
- Playwright: Web scraping
- Streamlit: Human review UI

---

## 🧑‍💻 Author
- Kousthubh N
- B.E. CSE, PES University
- GitHub: @Kousthubh142
