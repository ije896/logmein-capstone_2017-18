# Presentation Helper
This repository contains the work done for the UCSB course, CS189A-B, for the company LogMeIn

- A visual and aural analyzer that helps you improve your presentation skills
- Web app (thin-client) that records you using your webcam and gives you scores and gives you recommendations for your presentation

# MODULES

## Text_Analysis

The Text_Analysis module provides a number of functions to aid in analyzing a presentation's script.

- Analyzes sentiment (tone) with watson_analyzer.py

- Gets (sorted) frequencies of each word in text_analysis.py

- Can be queried for synonyms

USAGE:

All calls to the text analysis module can be done through text_analysis.py, which serves as a class that integrates the various submodules (watson_analyzer, synonyms, etc)
