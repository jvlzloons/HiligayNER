# 🌏 HILIGAYNER: A Baseline Named Entity Recognition Model and NLP Resource for Hiligaynon
//**Baseline Named-Entity Recognition & NLP Resources for Hiligaynon**  

> This repository contains the code, dataset, and models for our study entitled HILIGAYNER: Building Baseline Named-Entity Recognition and NLP Resources for the Hiligaynon Language. First publicly available Hiligaynon NER dataset & transformer-based models — built with **mBERT** and **XLM-RoBERTa**.

Authored by: James Ald Teves, Ray Daniel Cal, Josh Villaluz, Mico Magtira, Jean Malolos, Ramon Rodriguez, Mideth B. Abisado, and Joseph Imperial.

---

## 📦 Dependencies

- Label Studio – For annotation and dataset preparation
- Hugging Face Transformers – For implementing and fine-tuning transformer-based NER models
- Scikit-Learn – For computing inter-annotator agreement via Cohen’s Kappa
- SeqEval – For evaluation of precision, recall, and F1 scores in sequence labeling
- Datasets – Hugging Face’s datasets library for preprocessing and handling CoNLL format

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
  
| **Source**                           | **Original** | **Cleaned** |
| ------------------------------------ | ------------ | ----------- |
| Ang Pulong Sang Dios (New Testament) | 11,000       | 5,500       |
| Ilonggo News Live                    | 3,925        | 1,877       |
| Hiligaynon News and Features         | 2,281        | 919         |
| Bombo Radyo Bacolod                  | 286          | 276         |
| Ilonggo Balita sa Uma                | 155          | 153         |

- **⚙️ Models** – Fine-tuned mBERT & XLM-RoBERTa checkpoints  
- **📜 Annotation Guide** – BIO tagging instructions  
- **🧪 Scripts** – Training & evaluation pipelines

## 📬 Contact
For more questions, you may reach the corresponding author of the study at:

James Ald Teves
BS Computer Science, College of Computer Studies
Silliman University, Dumaguete
jamesyteves@su.edu.ph

Joseph Marvin Imperial
Faculty Member, Department of Computer Science
Lab Head, NU Human Language Technology Lab
jrimperial@national-u.edu.ph
