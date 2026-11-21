"""Generates a synthetic customer support ticket dataset (3000 tickets).
Columns: ticket_id, text, category, priority
Run: python data/generate_data.py
"""
import random
import pandas as pd

random.seed(7)

cats = {
    "Billing": [
        "i was charged twice for my subscription this month",
        "my invoice shows the wrong amount",
        "i need a refund for my last payment",
        "the card payment failed but the money was deducted",
        "please update the billing address on my invoice",
        "why was i charged a late fee on my account",
        "the coupon code did not apply at checkout and i paid full price",
    ],
    "Technical Issue": [
        "the app crashes every time i open it",
        "i get error 500 when uploading files",
        "the website is very slow and pages are not loading",
        "unable to sync data between my phone and laptop",
        "the software update failed and now it will not start",
        "there is a bug in the export feature and the report is blank",
        "notifications stopped working after the latest version",
    ],
    "Account Access": [
        "i forgot my password and the reset email never arrives",
        "my account is locked after too many login attempts",
        "i cannot log in with my username",
        "how do i change the registered email address on my account",
        "the two factor authentication code is not working",
        "i want to delete my account permanently",
        "i am not able to verify my phone number",
    ],
    "Shipping": [
        "my order has not arrived yet",
        "tracking says delivered but i did not get the package",
        "i received a damaged item in the parcel",
        "the wrong product was delivered to me",
        "can i change the delivery address for my order",
        "the courier has delayed my shipment by one week",
        "part of my order is missing from the box",
    ],
    "General Inquiry": [
        "do you offer student discounts",
        "what are your customer support working hours",
        "can you tell me about the premium plan features",
        "how do i contact the sales team",
        "is there a mobile app available",
        "do you have an api for developers",
        "where can i find the user guide",
    ],
}

openers = ["hi team,", "hello,", "good morning,", "dear support,", "", ""]
closers = ["thanks", "please help", "regards", "thank you", "", ""]
high = ["this is urgent", "i need this fixed immediately", "asap please", "this is a critical issue for my business",
        "i am losing money every hour", "extremely frustrated and escalating this", "my whole team is blocked"]
medium = ["please resolve this soon", "i have been waiting for two days", "this is the second time i am writing",
          "kindly look into this at the earliest"]
extras = ["", "", "", "i already tried restarting", "i am using the premium plan", "this happened yesterday", "i have attached a screenshot"]

# probability of (High, Medium, Low) per category
prio_weights = {
    "Billing": (0.30, 0.40, 0.30),
    "Technical Issue": (0.40, 0.40, 0.20),
    "Account Access": (0.35, 0.40, 0.25),
    "Shipping": (0.25, 0.40, 0.35),
    "General Inquiry": (0.03, 0.17, 0.80),
}

rows = []
for i in range(3000):
    cat = random.choice(list(cats))
    prio = random.choices(["High", "Medium", "Low"], weights=prio_weights[cat])[0]
    parts = [random.choice(openers), random.choice(cats[cat]), random.choice(extras)]
    if prio == "High" and random.random() < 0.9:
        parts.append(random.choice(high))
    elif prio == "Medium" and random.random() < 0.8:
        parts.append(random.choice(medium))
    parts.append(random.choice(closers))
    text = " ".join(p for p in parts if p)
    # 3% label noise to mimic human mis-tagging
    if random.random() < 0.03:
        cat = random.choice(list(cats))
    rows.append([f"T{i+1:05d}", text, cat, prio])

pd.DataFrame(rows, columns=["ticket_id", "text", "category", "priority"]).to_csv("data/support_tickets.csv", index=False)
print("saved", len(rows))
