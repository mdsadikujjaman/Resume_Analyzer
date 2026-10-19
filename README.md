# 🤖 AI Resume Analyzer

An AI-powered resume analysis application built with **Python, Streamlit, CrewAI, and Groq**. It uses multiple specialized AI agents to review resumes, evaluate ATS compatibility, and provide personalized career recommendations.

## 🚀 Live Demo

**Try the application:** [AI Resume Analyzer](https://resume-analyzer-sadikujjaman.streamlit.app/)

## 📸 Application Screenshot

<img width="1920" height="4279" alt="Image" src="https://github.com/user-attachments/assets/efe34719-b01b-43b6-91e5-d3c08d853c4d" />


*Replace the image path above with the actual path to your uploaded screenshot.*

## ✨ Features

- **📝 AI Resume Review:** Identifies resume weaknesses, formatting problems, and areas for improvement.
- **🎯 ATS Compatibility Analysis:** Evaluates resume structure, keyword usage, and ATS compatibility, including an AI-estimated score out of 100.
- **💼 Career Coaching:** Provides personalized career advice, identifies skill gaps, and recommends improvements.
- **📄 PDF Upload:** Upload a resume in PDF format for analysis.
- **🤝 Multi-Agent Architecture:** Uses CrewAI to coordinate three specialized AI agents.
- **⚡ Fast AI Inference:** Uses a Groq-hosted language model to generate feedback.
- **🌐 Interactive Web Interface:** Built with Streamlit and deployed online.

## 🛠️ Tech Stack

| Technology    | Purpose                               |
| ------------- | ------------------------------------- |
| Python        | Core programming language             |
| Streamlit     | Web application interface             |
| CrewAI        | Multi-agent orchestration             |
| Groq API      | Language model inference              |
| LiteLLM       | LLM integration through CrewAI        |
| python-dotenv | Local environment variable management |

## 🧠 AI Agents

### 1. Senior Tech Recruiter

Reviews the resume, identifies weak bullet points, and provides actionable feedback on strengths and weaknesses.

### 2. ATS Expert

Evaluates resume formatting, structure, and keyword usage, then provides an AI-estimated ATS compatibility score and recommendations.

### 3. Senior Career Coach

Analyzes the candidate's skills and experience to suggest career development opportunities and areas for improvement.

## 📂 Project Structure

```text
AI_Resume_Checker/
├── app.py              # Streamlit application
├── agents.py           # AI agent configurations
├── tasks.py            # Agent task definitions
├── crew_setup.py       # CrewAI orchestration
├── requirements.txt    # Python dependencies
├── .gitignore          # Ignored files and secrets
├── .env.example        # Environment variable template
└── screenshots/
    └── app-screenshot.png
```

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or a compatible Python version supported by your installed dependencies
- A Groq API key
- Git

### 1. Clone the repository

```bash
git clone https://github.com/mdsadikujjaman/Resume_Analyzer.git
cd Resume_Analyzer
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Replace the placeholder with your own API key.

**Security:** Never commit your `.env` file or expose your API key in source code.

### 5. Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to use the application.

## 🔐 Environment Variables

| Variable       | Description                                    |
| -------------- | ---------------------------------------------- |
| `GROQ_API_KEY` | API key used to access the Groq language model |

For local development, the application can load this variable from `.env`. For Streamlit Community Cloud, configure it in the app's secrets settings.

## 📌 Important Note

The ATS score is an AI-generated estimate based on the application's analysis. It is not an official score from a commercial applicant tracking system, and results may vary depending on the resume and language model output.

## 🔮 Future Improvements

- Job description matching and tailored resume recommendations
- Matched and missing keyword visualization
- Downloadable resume analysis reports
- Resume improvement suggestions tailored to specific job roles
- Enhanced error handling and input validation

## 👨‍💻 About the Developer

**Md Sadikujjaman**

Interested in Artificial Intelligence, Machine Learning, NLP, and building practical AI-powered applications.

- **LinkedIn:** [Connect with me](https://www.linkedin.com/in/sadikujjaman/)
- **GitHub:** [mdsadikujjaman](https://github.com/mdsadikujjaman)
- **Live Project:** [AI Resume Analyzer](https://resume-analyzer-sadikujjaman.streamlit.app/)

## 📄 License

This project is available for educational and portfolio purposes. Add a `LICENSE` file to the repository if you intend to distribute it under a specific open-source license.

---

⭐ If you find this project useful, consider starring the repository!
