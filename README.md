# What Is An AI Agent: O'Reilly Edition

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
   - [Document Question-Answering](#document-question-answering)
   - [Chatbot](#chatbot)
4. [File Structure](#file-structure)
5. [Contributing](#contributing)
6. [License](#license)
7. [Acknowledgments](#acknowledgments)

## Introduction

This repository is created as part of an O'Reilly project to explore the fundamentals of AI agents. It features two main components:

1. **Document Question-Answering (`src/01_document_qa.py`)**: Utilizes a conversational model to answer questions based on a given text dataset.
2. **Chatbot (`src/02_chatbot.py`)**: A simple chatbot implemented using Hugging Face's `hugchat` library.

## Installation

### Requirements

- Python 3.6+
- poetry for dependency management

Clone the repository:

```bash
git clone https://github.com/yourusername/what_is_an_ai_agent_oreilly.git
```

Navigate to the project directory:

```bash
cd what_is_an_ai_agent_oreilly/
```

Install the dependencies:

```bash
poetry install
```

## Usage

### Document Question-Answering

1. **Environment Setup**: Create a `.env` file in the project root and set your OpenAI API key:

   ```env
   OPENAI_API_KEY=your_api_key_here
   ```

2. **Data Preparation**: Place your `.csv` data files in the `data/sample_book_dataset/` directory.

3. **Run the Script**: Execute the following command:

   ```bash
   python src/01_document_qa.py
   ```

4. **Follow the Instructions**: Upload your text file when prompted and interact with the agent.

### Chatbot

1. **Environment Setup**: Add your Hugging Face credentials to Streamlit's secrets:

   ```bash
   st.secrets["HUGGINGFACE_EMAIL"] = your_email_here
   st.secrets["HUGGINGFACE_PASSWORD"] = your_password_here
   ```

2. **Run the Script**: Execute the following command:

   ```bash
   streamlit run src/02_chatbot.py
   ```

3. **Interact**: Open the Streamlit app and start chatting with the bot.

## File Structure

```plaintext
.
├── data/
│   ├── sample_book_dataset/
├── Makefile
├── poetry.lock
├── pyproject.toml
├── README.md
└── src/
    ├── 01_document_qa.py
    └── 02_chatbot.py
```

## Contributing

If you wish to contribute to this project, please read the [CONTRIBUTING.md](CONTRIBUTING.md) guide.

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- O'Reilly for the opportunity to explore AI agents.
- OpenAI for their conversational models.
- Hugging Face for their `hugchat` library.
