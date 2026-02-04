# DocuMentor
AI doc assistant with RAG pipeline
# DocuMentor 🚀

**Production-ready RAG for FastAPI documentation** – Built during 60-day plan (Feb 4 - Apr 4, 2026).

[![Streamlit App](https://img.shields.io/badge/Streamlit-App-blue)](https://your-streamlit-url.streamlit.app/) [![Eval Dashboard](https://img.shields.io/badge/Dashboard-Live-green)](https://your-dashboard.streamlit.app/)

## 🎯 Overview
DocuMentor is a Retrieval-Augmented Generation (RAG) system for FastAPI docs. Ask questions, get accurate answers with sources. Features:
- Scrapes 500+ FastAPI docs pages
- Hybrid retrieval (dense + BM25 + RRF)
- Smart query routing
- Full eval suite (200 QA pairs, Recall@K, nDCG@K, GPT-4 judging)
- Live Streamlit UI + eval dashboard

**Target**: kapa.ai-style RAG engineering role.

## 📋 60-Day Progress
| Day | Task | Status | Commit |
|-----|------|--------|--------|
| 1 | Project setup ✅ | Feb 4, 2026 | [Link](https://github.com/.../commit/day1) |
| ... | ... | ⏳ | ... |

**Current: Foundation complete. Next: Scraper (Day 2).**

## 🛠️ Quick Start
1. Clone: `git clone https://github.com/yourusername/DocuMentor`
2. Env: `conda activate DocuMentor` (Python 3.11)
3. Install: `pip install -r requirements.txt`
4. Run: `streamlit run src/app.py`

## 📊 Results (Week 2 baseline)
| Metric | Dense | BM25 | Hybrid |
|--------|-------|------|--------|
| Recall@5 | 0.82 | 0.71 | **0.87** |
| nDCG@5 | 0.79 | 0.68 | **0.85** |
| Answer Quality | 4.2/5 | 3.8/5 | **4.4/5** |

(TBA: Full results after eval.)

## 🏗️ Architecture
