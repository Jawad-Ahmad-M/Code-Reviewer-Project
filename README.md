# 🧠 Micro Code Review Assistant

A **web-based AI-powered platform** that allows users to write, execute, and receive instant **AI-generated code reviews** — combining real-time execution with intelligent feedback to enhance code quality, logic, and understanding.

---

## 🚀 Overview

**Micro Code Review Assistant** provides an interactive environment for:

* Writing and executing code directly in the browser
* Receiving AI-driven feedback on logic, structure, and optimization
* Reviewing past submissions and improvements
* Supporting multiple programming languages

This project bridges the gap between **automated code execution** and **AI-based code evaluation**, designed for both **learners and developers**.

---

## 🏗️ System Architecture

| Layer                | Technology                        | Description                             |
| -------------------- | --------------------------------- | --------------------------------------- |
| **Frontend**         | Angular 17                        | Interactive web-based UI                |
| **Backend**          | FastAPI / Flask                   | RESTful API for logic and communication |
| **Execution Engine** | Piston / Judge0 API               | Executes code safely in sandbox         |
| **AI Engine**        | Hugging Face Inference API        | Analyzes and reviews user code          |
| **Database**         | SQLite (local) / Supabase (cloud) | Stores history, users, and reviews      |
| **Deployment**       | Railway / Render / Vercel         | Cloud hosting                           |

---

## 🧩 Key Features

### 📝 1. Code Editor & Execution

* Syntax-highlighted online code editor
* Multi-language support (Python, C++, Java, JavaScript)
* Real-time execution using **Piston API**

### 🤖 2. AI Review & Feedback

* AI model analyzes code quality, readability, and efficiency
* Provides structured review responses
* Uses **Hugging Face inference API** for LLM-based analysis

### 📚 3. Review History

* Stores all code submissions, outputs, and AI feedback
* Search and filter previous reviews by date or language

### 🔗 4. API Sharing (Optional)

* Exposes `/ai-review` endpoint for external integrations
* Developers can submit code and receive AI reviews via REST API

---

## ⚙️ Requirements

| Component         | Version             |
| ----------------- | ------------------- |
| Node.js           | 20+                 |
| Angular CLI       | 17+                 |
| Python            | 3.11+               |
| FastAPI / Flask   | Latest              |
| SQLite / Supabase | Any                 |
| Internet          | Required (for APIs) |

---

## 🧠 Use Cases

| User Type                 | Description                                            |
| ------------------------- | ------------------------------------------------------ |
| **Student / Interviewee** | Practice coding and receive quick AI insights          |
| **Developer**             | Improve performance, readability, and code structure   |
| **Instructor**            | Demonstrate AI-based review and feedback in classrooms |

---

## 🔒 Non-Functional Requirements

| Category         | Description                                 |
| ---------------- | ------------------------------------------- |
| **Performance**  | Code execution < 2s, AI review < 5s         |
| **Scalability**  | Up to 50 concurrent users                   |
| **Security**     | HTTPS, CORS enabled, limited API key access |
| **Usability**    | Modern, intuitive UI with dark/light themes |
| **Availability** | 95% uptime (depends on hosting tier)        |

---

## 🧱 How It Works

1. **User writes code** in the Angular web editor
2. **Frontend sends code** to the backend (FastAPI)
3. Backend forwards to:

   * **Piston/Judge0 API** → executes code safely
   * **Hugging Face Model API** → generates intelligent feedback
4. **Response returned** to frontend and displayed in **Feedback** tab
5. **Submission stored** in database for review history

---

## 🔄 Future Enhancements

* 👥 Real-time collaboration (multi-user editing)
* 🔊 AI-generated voice feedback
* 💡 Smart code completion using LLMs
* 🔍 Plagiarism detection and originality scoring

---

## 🧰 Setup Instructions

### Clone the Repository

```bash
git clone https://github.com/Jawad-Ahmad-M/Micro-Code-Review-Assistant.git
cd Micro-Code-Review-Assistant
```

### Frontend Setup (Angular)

```bash
cd frontend
npm install
ng serve
```

Access via: [http://localhost:4200](http://localhost:4200)

### Backend Setup (FastAPI)

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Access via: [http://localhost:8000](http://localhost:8000)

---

## 🧪 API Reference

| Endpoint     | Method | Description                  |
| ------------ | ------ | ---------------------------- |
| `/execute`   | POST   | Executes code via Piston API |
| `/ai-review` | POST   | Gets AI feedback for code    |
| `/history`   | GET    | Fetches previous submissions |

---

## 🧑‍💻 Contributors

| Name                                                  | Role                       |
| ----------------------------------------------------- | -------------------------- |
| **Jawad Ahmad**                                       | Lead Developer & Architect |
| **Muneeb Shafique**                                   | Frontend Engineer          |
| **Dayyan Riaz**                                       | Backend Developer          |
| **Huzaifa Muzammil**                                  | QA & Integration           |
| **Supervisor:** Mam Iris                              | Project Advisor            |
| **Institute:** UET Lahore – Institute of Data Science |                            |

---

## 📄 License

This project is for educational and research purposes under the supervision of **UET Lahore**.
You may modify or extend it for non-commercial use.

---

## 🧭 References

* [Hugging Face Inference API Docs](https://huggingface.co/docs/api-inference)
* [Piston Code Execution API](https://github.com/engineer-man/piston)
* [FastAPI Documentation](https://fastapi.tiangolo.com)
* [Angular Official Docs](https://angular.dev)

---

### 🌐 “Turning Code into Intelligence.”

> *An AI-Driven Code Review Assistant built by students of UET Lahore.*
