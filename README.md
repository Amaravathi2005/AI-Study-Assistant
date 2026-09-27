# AI Study Assistant

## Project Description

AI Study Assistant is a simple AI-powered student utility application built using Python, Streamlit, and Google Gemini API.

It helps students with common study tasks such as:

- Concept Explanation
- Note Summarization
- Quiz Generation
- Answer Improvement

## Features

### 1. Concept Explanation
Explains a topic in simple language with definitions, important points, examples, and an exam-ready answer.

### 2. Note Summarization
Converts study notes into important points and a short revision summary.

### 3. Quiz Generation
Generates multiple-choice questions with answers and explanations.

### 4. Answer Improvement
Improves a student's answer by correcting grammar, structure, clarity, and missing points.

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- Google GenAI Python SDK

## How It Works

1. The student selects a study utility.
2. The student enters the required content.
3. The application validates the input.
4. A structured prompt is created.
5. The prompt is sent to the Gemini API.
6. Gemini generates the response.
7. The result is displayed in the Streamlit application.

## Error Handling

The application checks for empty input and displays a warning.

It also handles API errors and displays an error message if the AI response cannot be generated.

## How to Run

Install the required packages:

```bash
pip install -r requirements.txt