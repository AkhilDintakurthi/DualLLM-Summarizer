# DualLLM-Summarizer

**LLM-Powered Web Summarizer with Multi-Model Evaluation**  
Built to showcase full-stack GenAI engineering — from dynamic web scraping to dual-model summarization and automated LLM-based evaluation.

---

## Overview

**DualLLM-Summarizer** is a powerful web summarization tool that:

- Extracts and cleans text from complex web pages (even JS-heavy content)
- Summarizes the article using **two different LLMs**: OpenAI and Ollama
- Automatically evaluates both summaries using **GPT-4 as a judge** based on clarity, faithfulness, and conciseness

This allows users to **visually compare** the summaries and understand which model performs better — and why.

---

## Features

| Feature                          | Description |
|----------------------------------|-------------|
| **Playwright Scraper**        | Handles dynamic web content (scrolling, JS rendering, login flows) |
| **BeautifulSoup Cleaner**     | Strips out noise (ads, footers, scripts) to retain pure article content |
| **OpenAI + Ollama Summarizer**| Dual summarization using both cloud and local LLMs |
| **LLM Evaluation (GPT-4)**     | GPT-4 scores and explains which summary is better and why |
| **Modular Design**             | Easy to plug in other models (Claude, Gemini, Mistral, etc.) |

---

## Architecture

```
URL → Playwright Scraper → Clean HTML → Extracted Text
                                 ↓
                      ┌────────────────────┬────────────────────┐
                      ↓                    ↓
              🧠 OpenAI Summary      🧠 Ollama Summary
                      ↓                    ↓
               🤖 GPT-4 Evaluation → 🏆 Winner Summary & Reason
```

## 📁 Folder Structure
```
DualLLM-Summarizer/
├── scraper/
│   ├── scraper.py           # Core scraping logic using Playwright
│   ├── web_scraper.py       # Wrapper for single-URL scraping
│   └── __init__.py
│
├── summarizer/
│   ├── openai_summarizer.py # Calls OpenAI models (GPT-3.5/GPT-4)
│   ├── ollama_summarizer.py # Calls local models via Ollama (e.g., LLaMA2, Mistral)
│   └── __init__.py
│
├── eval/
│   ├── gpt_judge.py         # GPT-based evaluation logic
│   ├── evaluator.py         # Wrapper to call GPT-4 to compare summaries
│   └── __init__.py
│
├── main.py                  # End-to-end controller (takes URL → outputs comparison)
├── requirements.txt         # All dependencies
├── README.md                # Project documentation
└── .env                     # API keys for OpenAI, etc.
```

---

## 🔧 Tech Stack

- **Language**: Python 3.11+
- **Scraping**: Playwright, BeautifulSoup
- **LLMs**: OpenAI API (GPT-4), Ollama (local models)
- **Evaluation**: GPT-4 using LangChain's Structured Output
- **Utilities**: `httpx`, `dotenv`, `langchain`, `scikit-learn` (optional for later analysis)

---

## 👤 Author

**Akhil Sai Kalyan Dintakurthi**  
GenAI Engineer | Data Scientist | LLM Integrator

- 📧 Email: dintakurthiakhilsai@gmail.com  

---
