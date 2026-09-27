import streamlit as st
from google import genai
import os

# -----------------------------
# Gemini API Configuration
# -----------------------------

api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    st.error("Gemini API key is not connected.")
    st.stop()

client = genai.Client(api_key=api_key)


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚",
    layout="centered"
)


# -----------------------------
# Application Title
# -----------------------------

st.title("📚 AI Study Assistant")

st.write(
    "An AI-powered study utility that helps students "
    "understand concepts, summarize notes, generate quizzes, "
    "and improve answers."
)


# -----------------------------
# Select Study Utility
# -----------------------------

utility = st.selectbox(
    "Choose a study utility:",
    [
        "Concept Explanation",
        "Note Summarization",
        "Quiz Generation",
        "Answer Improvement"
    ]
)


# -----------------------------
# Student Input
# -----------------------------

if utility == "Concept Explanation":
    input_text = st.text_area(
        "Enter the topic or question you want to understand:",
        placeholder="Example: Explain Ohm's Law"
    )

elif utility == "Note Summarization":
    input_text = st.text_area(
        "Paste your notes here:",
        placeholder="Paste your study notes here..."
    )

elif utility == "Quiz Generation":
    input_text = st.text_area(
        "Enter the topic for the quiz:",
        placeholder="Example: Data Communication"
    )

else:
    input_text = st.text_area(
        "Paste your answer here:",
        placeholder="Paste your answer that you want to improve..."
    )


# -----------------------------
# Generate Button
# -----------------------------

if st.button("🤖 Generate", use_container_width=True):

    # Basic input validation
    if not input_text.strip():
        st.warning("⚠️ Please enter some text before generating an answer.")

    else:

        # -----------------------------
        # Structured Prompts
        # -----------------------------

        if utility == "Concept Explanation":

            prompt = f"""
You are an AI Study Assistant.

Help a college student understand the following topic.

Topic/Question:
{input_text}

Provide the answer in this structure:

1. Simple Definition
2. Easy Explanation
3. Important Points
4. Formula, if applicable
5. Simple Example
6. Short Exam-Ready Answer

Use simple and clear language.
Avoid unnecessary complexity.
"""

        elif utility == "Note Summarization":

            prompt = f"""
You are an AI Study Assistant.

Summarize the following student notes.

Notes:
{input_text}

Provide:

1. Main Topic
2. Key Points
3. Important Definitions
4. Important Formulas, if any
5. Short Revision Summary

Keep the information clear and useful for exam preparation.
"""

        elif utility == "Quiz Generation":

            prompt = f"""
You are an AI Study Assistant.

Create a short study quiz based on this topic:

Topic:
{input_text}

Generate:

1. Five multiple-choice questions
2. Four options for each question
3. Correct answer for each question
4. One-line explanation for each answer

Keep the questions suitable for a college student.
"""

        else:

            prompt = f"""
You are an AI Study Assistant.

Improve the following student's answer.

Student Answer:
{input_text}

Provide:

1. Improved Answer
2. Important corrections
3. Missing points
4. Simple exam-ready version

Keep the original meaning but improve clarity,
grammar, structure, and technical accuracy.
"""


        # -----------------------------
        # Gemini API Call
        # -----------------------------

        try:

            with st.spinner("🤖 Generating your answer..."):

                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=prompt
                )

            # -----------------------------
            # Display Result
            # -----------------------------

            st.success("Answer generated successfully!")

            st.subheader("📖 AI Result")

            st.write(response.text)

        except Exception as e:

            st.error(
                "❌ Something went wrong while generating the answer."
            )

            st.info(
                "Please check your internet connection and Gemini API configuration."
            )