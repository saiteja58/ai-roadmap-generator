# AI Roadmap Generator

The **AI Roadmap Generator** is an intelligent system designed to guide users in achieving their career goals by generating a personalized step-by-step roadmap. The generator tests the user on one of three starting courses — Data Science, Software Development, or AI Engineering — and based on their quiz responses, provides a tailored learning path with resources.

## Features

- **Personalized Roadmap**: Generates a step-by-step roadmap for the user’s selected course.
- **Random MCQ Quiz**: Administers a 15-question quiz to evaluate the user’s current knowledge.
- **Course Selection**: Choose from three initial career tracks: Data Science, Software Development, or AI Engineering.
- **AI-Driven Recommendations**: Based on quiz results, the AI model suggests a customized learning plan with resources.
- **Streamlit Interface**: Easy-to-use web interface for interacting with the roadmap generator.

## Tech Stack

- **Python**
- **Streamlit**: For building the user interface.
- **Hugging Face**: For integrating AI-powered suggestions.
- **TensorFlow / PyTorch**: For AI model training and inference (if used).
- **Other Libraries**: Depending on the resources you use, this can include libraries for quiz generation, web development, etc.

## Setup

### Prerequisites

Make sure you have Python 3.7 or higher installed. You'll also need `pip` to install the dependencies.

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/ai-roadmap-generator.git
   cd ai-roadmap-generator
