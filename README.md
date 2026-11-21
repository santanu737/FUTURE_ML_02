# FUTURE_ML_02 - Support Ticket Classification

Future Interns - Machine Learning Track | Task 2

## Overview
An NLP system that reads a customer support ticket, predicts its **category** (Billing, Technical Issue, Account Access, Shipping, General Inquiry) and tags a **priority** (High / Medium / Low) so support teams respond faster.

## What is inside
| File | Purpose |
|---|---|
| `support_ticket_classification.ipynb` | full workflow with outputs |
| `data/support_tickets.csv` | 3000 tickets (`ticket_id, text, category, priority`) |
| `data/generate_data.py` | script that created the dataset |
| `outputs/` | confusion matrices and analytics charts |

## Dataset note
The dataset is **synthetic**, generated from realistic ticket templates with random openers, closers, urgency phrases and 3% label noise. To use real tickets, replace `data/support_tickets.csv` with a file that has `text`, `category`, `priority` columns.

## Approach
1. **Text cleaning:** lowercase, punctuation removal, tokenization, stop-word removal (negations like "not" and "cannot" are kept).
2. **Features:** TF-IDF with unigrams + bigrams.
3. **Category model:** Logistic Regression vs Linear SVM, compared by accuracy and macro F1.
4. **Priority tagging:** Logistic Regression (class-balanced) + a business rule that always escalates tickets with urgency keywords.
5. **Evaluation:** classification reports, confusion matrices, High-priority recall before and after the rule.
6. **`analyze_ticket(text)`** returns category + priority for any new ticket.

## How to run
```bash
pip install -r requirements.txt
jupyter notebook support_ticket_classification.ipynb
```

## Tech
Python, Pandas, Scikit-learn (TF-IDF, Logistic Regression, LinearSVC), Matplotlib
