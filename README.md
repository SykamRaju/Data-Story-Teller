# 🧠 Data Story Teller

A Streamlit-powered AI application that turns raw data into insightful business stories using GPT.

![demo](https://raw.githubusercontent.com/SykamRaju/Data-Story-Teller/refs/heads/main/app/static/demo.png)

## 🌟 Features

- 📊 Upload a dataset (CSV)
- 🤖 Auto-generate insights using GPT-3.5
- 🧮 Uses real startup funding data from India
- ⚙️ Hosted live using Streamlit Cloud
- 🔐 Uses OpenAI API via secret key
- 💡 Ready for portfolio and LinkedIn showcase

## 🚀 Live Demo

👉 [data-story-teller.streamlit.app](https://data-story-teller.streamlit.app)

## 🧰 Tech Stack

- Python 3.10
- Streamlit
- Pandas
- OpenAI GPT-3.5 API

## 💻 Local Setup

```bash
git clone https://github.com/SykamRaju/Data-Story-Teller.git
cd Data-Story-Teller

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Set your OpenAI API key in .env (optional for local)
echo OPENAI_API_KEY=your_key > .env

# Run the app
streamlit run app/main.py
```
