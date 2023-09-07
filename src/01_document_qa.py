from os import chdir, environ

from dotenv import load_dotenv
from pandas import read_csv
import chainlit as cl
import openai


from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
from io import BytesIO

from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)


chdir(
    "/Users/blabaschin/Documents/Technical/GitHub/what_is_an_ai_agent_oreilly/"
)  # noqa: sets my current directory
load_dotenv(".env")  # loads sensitive information


openai.api_key = environ["OPENAI_API_KEY"]  # sets openai api key

# load the initial prompt

system_template = """Use the following pieces of context to answer the users question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.
ALWAYS return a "SOURCES" part in your answer.
The "SOURCES" part should be a reference to the source of the document from which you got your answer.

Example of your response should be:

```
The answer is foo
SOURCES: xyz
```

Begin!
----------------
{summaries}"""  # noqa
messages = [
    SystemMessagePromptTemplate.from_template(system_template),
    HumanMessagePromptTemplate.from_template("{question}"),
]
prompt = ChatPromptTemplate.from_messages(messages)
chain_type_kwargs = {"prompt": prompt}

# load the data


def leverage_pandas_ai(df, prompt: str):
    """
    A function to run the Query on given Pandas Dataframe
    Args:

        df: A Pandas dataframe
        prompt: Query / Prompt related to data

    Returns: Response / Results

    """

    pandas_ai = PandasAI(
        OpenAI(api_token=openai.api_key), conversational=True, verbose=False
    )
    response = pandas_ai.run(df, prompt=prompt, is_conversational_answer=True)

    return response


@cl.on_chat_start
async def start():
    files = None

    # Wait for the user to upload a file
    while files == None:
        files = await cl.AskFileMessage(
            content="Please upload a text file to begin!", accept=["text/csv"]
        ).send()

    file = files[0]
    csv_file = BytesIO(file.content)
    df = read_csv(csv_file)
    cols = [col for col in df.columns if "star" not in col and "link" not in col]
    df = df[cols]
    cl.user_session.set("data", df)
    cols = "\n".join(df.columns.tolist())
    await cl.Message(
        content="Here are the columns contained in the data you've provided!\n" + cols
    ).send()


@cl.on_message
async def main(message: str):
    answer = leverage_pandas_ai(df=cl.user_session.get("data"), prompt=message)

    # Send a response back to the user
    await cl.Message(
        content=answer,
    ).send()
