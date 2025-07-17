#!/usr/bin/env python
import json
import os
import sys
import warnings
from pathlib import Path
from datetime import datetime
from dateutil.relativedelta import relativedelta

from releases.crew import Releases

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def get_inputs():
    language_style = """
    Background for Style
    - The reader is from the CREWAI community and uses CREWAI tools and platform.
    - The reader is interested in learning about and producing projects with CREWAI.
    - The reader may have any role in the company, from developer to CEO.

    1. Core Voice & Tone
    - Professional, supportive, pragmatic – speak as a seasoned entrepreneur-advisor.
    - Balanced and non-partisan – present multiple views; avoid political bias.
    - Succinct and action-oriented – favour clear calls to action over theory.
    - Inclusive and encouraging – build community, highlight collaboration.
    - Confident but modest – share expertise without hype or jargon overload.

    2. Readability Principles
    - Use plain English and UK spelling – avoid idioms that may confuse non-native readers.
    - Assume the reader is educated but may not be a native English speaker.
    - Use short sentences (max 20 words) – break up complex ideas.
    - Use single-idea paragraphs – improve scanning.
    - Use bullet points as default – convert lists or multi-step ideas into bullets.
    - Use active voice (e.g., "We'll launch the pilot next week.")
    - Explain acronyms on first use – essential for dyslexic and new readers.

    3. Perspective & Pronouns
    - Default to first-person singular ("I") when speaking personally.
    - Use first-person plural ("we") for team or community efforts.
    - Address the reader as "you" for a conversational, direct tone.
    - Avoid filler words: just, really, very.
"""
    knowledge_dir = Path("knowledge")
    release="0.148.0"

    # read the templates for the reports

    with open(os.path.join(knowledge_dir, "release_template.md"), "r") as f:
        release_template = f.read()  

    with open(os.path.join(knowledge_dir, "insights_template.md"), "r") as f:
        insights_template = f.read()  

    with open(os.path.join(knowledge_dir, "issue_template.md"), "r") as f:
        issue_template = f.read()  

    with open(os.path.join(knowledge_dir, "community_template.md"), "r") as f:
        community_template = f.read()  

    with open(os.path.join(knowledge_dir, "tldr_template2.md"), "r") as f:
        tldr_template = f.read()  

    return {
        #project specific inputs for the crew
        'current_year': str(datetime.now().year),
        'current_date': str(datetime.now().strftime("%Y-%m-%d")),
        'two_months_ago': str((datetime.now() - relativedelta(months=2)).strftime("%Y-%m-%d")),
        'language_style': language_style,
        'release_template': release_template,
        'insights_template': insights_template,
        'issue_template': issue_template,
        'community_template': community_template,
        'tldr_template': tldr_template,
        'release': release
    }

# Call get_inputs() ONCE here as this is used for the crew inputs
inputs = get_inputs()

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    try:
        Releases().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    try:
        Releases().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Releases().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    try:
        # If you want to add/override keys, do it here:
        Releases().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
