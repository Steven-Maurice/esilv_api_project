
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 17:23:28 2024

@author: arthur
"""

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download the VADER lexicon
nltk.download('vader_lexicon')

def FeelingsAnalysis(text):
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(text)