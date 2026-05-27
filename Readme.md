# ✨ Groq AI Chatbot

A modern AI chatbot built using:

- Groq API
- Streamlit
- Python
- GitHub Actions

This project features:

✅ Real-time streaming responses  
✅ Modern dark UI  
✅ Chat history  
✅ GitHub CI workflow  
✅ Streamlit Cloud deployment  
✅ Secure API key management  

---

# 🚀 Demo

Deployed using Streamlit Community Cloud.

---

# 📸 Features

- ⚡ Ultra-fast Groq inference
- 💬 Streaming chatbot responses
- 🎨 Aesthetic modern UI
- 🔒 Secure API key handling
- ☁️ Cloud deployment
- 🔄 Automatic redeployment via GitHub
- 🛠 GitHub Actions CI pipeline

---

# 🧠 Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend |
| Streamlit | Frontend |
| Groq API | LLM inference |
| GitHub Actions | CI/CD |
| Streamlit Cloud | Hosting |

---

# 📂 Project Structure

```bash
GroqBot/
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── app.py
├── requirements.txt
├── .gitignore
├── .env
└── README.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git

cd YOUR_REPO
```

---

## 2. Create Virtual Environment

### Windows (Git Bash)

```bash
python -m venv venv

source venv/Scripts/activate
```

### Windows CMD

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Get API key from:

https://console.groq.com

---

# ▶️ Run Locally

```bash
streamlit run app.py
```

Application runs on:

```text
http://localhost:8501
```

---

# ☁️ Deployment

## Deploy on Streamlit Cloud

1. Push project to GitHub
2. Open Streamlit Cloud
3. Create new app
4. Select repository
5. Deploy

---

# 🔒 Streamlit Secrets

Inside Streamlit Cloud:

```text
App Settings → Secrets
```

Add:

```toml
GROQ_API_KEY = "your_api_key"
```

---

# 🔄 Automatic Deployment

Every GitHub push automatically redeploys the app.

```bash
git add .
git commit -m "Updated chatbot"
git push
```

---

# ⚙️ GitHub Actions

Workflow file:

```text
.github/workflows/deploy.yml
```

The pipeline:

- Checks syntax
- Installs dependencies
- Validates app before deployment

---

# 📦 requirements.txt

```txt
streamlit
groq
python-dotenv
```

---

# 🧪 Example Models

You can use:

```python
model="llama-3.3-70b-versatile"
```

Other supported Groq models:

- llama3
- mixtral
- gemma
- deepseek

---

# 🎨 UI Features

- Gradient dark background
- Custom chat bubbles
- Streaming typing effect
- Responsive layout
- Modern design

---

# 📸 Screenshot

Add your screenshot here.

```text
assets/screenshot.png
```

---

# 🛠 Future Improvements

- Voice assistant
- PDF chatbot
- RAG pipeline
- Authentication
- Database storage
- Multi-user chat
- Docker deployment
- AWS deployment

---

# 🐞 Troubleshooting

## Module Not Found Error

```bash
pip install -r requirements.txt
```

---

## Streamlit Not Found

```bash
pip install streamlit
```

---

## Git Bash Virtual Environment Error

Use:

```bash
source venv/Scripts/activate
```

---

# 📚 Useful Links

## Groq

https://console.groq.com

## Streamlit

https://streamlit.io

## GitHub Actions

https://docs.github.com/actions

---

# 📄 License

MIT License

---

# 👨‍💻 Author

Avirup Pal

Built with ❤️ using Groq + Streamlit