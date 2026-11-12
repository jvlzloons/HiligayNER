# 🌏 HILIGAYNER: A Baseline Named Entity Recognition Model for Hiligaynon

> This repository contains the code, dataset, and models for our study entitled HILIGAYNER: Building Baseline Named-Entity Recognition for the Hiligaynon Language. First publicly available Hiligaynon NER dataset & transformer-based models — built with **mBERT** and **XLM-RoBERTa**.

Authored by: James Ald Teves, Ray Daniel Cal, Josh Villaluz, Mico Magtira, Jean Malolos, Ramon Rodriguez, Mideth Abisado, and Joseph Marvin Imperial.

---
## Access the fine-tuned HiligayNER models on HuggingFace:

- [XLM-RoBERTa Large](https://huggingface.co/josephimperial/hiligayner-xlmr-large)
- [XLM-RoBERTa Base](https://huggingface.co/josephimperial/hiligayner-xlmr-base)
- [mBERT](https://huggingface.co/josephimperial/hiligayner-mbert)

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


- **⚙️ Models** Fine-tuned mBERT & XLM-RoBERTa checkpoints

- **Table 3:** Performance of mBERT Transformer-based model fine-tuning for Hiligaynon NER
  
| Tagset | Precision | Recall | F1-Score | Support |
| ------ | --------- | ------ | -------- | ------- |
| B-PER  | 0.95      | 0.97   | 0.96     | 1754    |
| I-PER  | 0.93      | 0.94   | 0.94     | 2181    |
| B-LOC  | 0.79      | 0.86   | 0.83     | 565     |
| I-LOC  | 0.82      | 0.83   | 0.82     | 1237    |
| B-ORG  | 0.77      | 0.87   | 0.82     | 505     |
| I-ORG  | 0.77      | 0.82   | 0.79     | 944     |

- **Table 4:** Performance of XLM-RoBERTa Transformer-based model fine-tuning for Hiligaynon NER
  
| Tagset | Precision | Recall | F1-Score | Support |
| ------ | --------- | ------ | -------- | ------- |
| B-PER  | 0.95      | 0.97   | 0.96     | 1777    |
| I-PER  | 0.93      | 0.95   | 0.94     | 2268    |
| B-LOC  | 0.79      | 0.86   | 0.82     | 577     |
| I-LOC  | 0.83      | 0.85   | 0.84     | 1228    |
| B-ORG  | 0.76      | 0.87   | 0.81     | 514     |
| I-ORG  | 0.74      | 0.84   | 0.79     | 910     |

- **📜 Annotation Guide** – BIO tagging instructions  
- **🧪 Scripts** – Training & evaluation pipelines

## 📬 Contact
For more questions, you may reach the corresponding author of the study at:

**James Ald Teves**  <br>
BS Computer Science, College of Computer Studies  <br>
Silliman University, Dumaguete  <br>
jamesyteves@su.edu.ph  <br><br>

**Joseph Marvin Imperial**  <br>
Faculty Member, Department of Computer Science  <br>
Lab Head, NU Human Language Technology Lab  <br>
jrimperial@national-u.edu.ph
