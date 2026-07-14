# What Are AI Agents? (Companion Code)

Companion code for my O'Reilly report **[What Are AI Agents? When and How to Use LLM Agents](https://www.oreilly.com/library/view/what-are-ai/9781098159726/)**. The report introduces AI agents, how they differ from large language models, and when to use them. This repository holds two small, runnable examples that go with it.

## What's inside

- **Document Question-Answering** (`src/01_document_qa.py`). Answers questions over a text dataset with a conversational model.
- **Chatbot** (`src/02_chatbot.py`). A simple chatbot built on Hugging Face's `hugchat` and served with Streamlit.

## Installation

Requires a recent Python and [Poetry](https://python-poetry.org/).

```bash
git clone https://github.com/EconoBen/what_are_ai_agents.git
cd what_are_ai_agents
poetry install
```

## Usage

### Document Question-Answering

1. Create a `.env` file in the project root with your OpenAI key.

   ```env
   OPENAI_API_KEY=your_api_key_here
   ```

2. Place your `.csv` files in `data/sample_book_dataset/`.
3. Run it.

   ```bash
   python src/01_document_qa.py
   ```

### Chatbot

1. Add your Hugging Face credentials to Streamlit secrets in `.streamlit/secrets.toml`.

   ```toml
   HUGGINGFACE_EMAIL = "your_email_here"
   HUGGINGFACE_PASSWORD = "your_password_here"
   ```

2. Run it.

   ```bash
   streamlit run src/02_chatbot.py
   ```

## File structure

```
.
├── data/
│   └── sample_book_dataset/
├── src/
│   ├── 01_document_qa.py
│   └── 02_chatbot.py
├── Makefile
├── pyproject.toml
└── README.md
```

## License

MIT

## Author

Built by [Ben Labaschin](https://econoben.dev), O'Reilly author on AI agents and agent memory.
