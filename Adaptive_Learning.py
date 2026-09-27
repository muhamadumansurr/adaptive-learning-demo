import streamlit as st
import numpy as np
import pandas as pd
import sqlite3
import time
from sklearn.tree import DecisionTreeClassifier
from fpdf import FPDF   # ✅ Replaced WeasyPrint with fpdf2

# ==========================================
# 1. DATABASE & PERSISTENCE LAYER (SQLite)
# ==========================================
DB_FILE = "adaptive_learning.db"

# ... (keep your existing init_db, get_learner_profile, upsert_learner_profile, log_assessment)

# ==========================================
# 2. PDF REPORT GENERATION (fpdf2)
# ==========================================


def generate_report(student_id, profile):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Adaptive Learning Report", ln=True, align="C")
    pdf.ln(10)

    pdf.cell(200, 10, txt=f"Student ID: {student_id}", ln=True)
    pdf.cell(
        200, 10, txt=f"Average Score: {profile['topic_score_avg']}%", ln=True)
    pdf.cell(200, 10, txt=f"Attempts: {profile['attempt_count']}", ln=True)
    pdf.cell(200, 10, txt=f"Error Frequency: {profile['error_frequency']}", ln
