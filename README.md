# 🌏 HILIGAYNER  
**Baseline Named-Entity Recognition & NLP Resources for Hiligaynon**  

> First publicly available Hiligaynon NER dataset & transformer-based models — built with **mBERT** and **XLM-RoBERTa**.  

---

## 📌 Overview  
HILIGAYNER is the first open-source **Named Entity Recognition (NER)** corpus and baseline models for the Hiligaynon language, spoken by ~11M people in the Philippines.  
- **~8,000 sentences** annotated with CoNLL BIO format  
- **Entity types**: Person (PER), Organization (ORG), Location (LOC), Other (O)  
- **High-quality annotations** (Cohen’s κ = 0.81)  
- Baseline models: **mBERT** & **XLM-RoBERTa** (F1 ≈ 0.86)  
- Cross-lingual evaluation with Cebuano & Tagalog (F1 ≈ 0.46)  

---

## 📂 Contents  
- **📁 Dataset** – Cleaned & annotated corpus in CoNLL-U format  
- **⚙️ Models** – Fine-tuned mBERT & XLM-RoBERTa checkpoints  
- **📜 Annotation Guide** – BIO tagging instructions  
- **🧪 Scripts** – Training & evaluation pipelines  

---

## 🚀 Quick Start  

```bash
# Clone repo
git clone https://github.com/<your-repo>/HILIGAYNER.git
cd HILIGAYNER

# Install dependencies
pip install -r requirements.txt

# Train model
python train.py --model mBERT --epochs 3

# Evaluate
python evaluate.py --model mBERT --dataset test.conllu
