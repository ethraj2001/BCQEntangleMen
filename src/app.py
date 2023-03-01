import datetime
import os

import gradio as gr

from langchain import LLMMathChain, OpenAI, SerpAPIWrapper
from langchain.agents import initialize_agent, Tool
from langchain import OpenAI, Wikipedia
from langchain.agents import initialize_agent, Tool
from langchain.agents.react.base import DocstoreExplorer
from langchain.chains.conversation.memory import ConversationBufferMemory

memory = ConversationBufferMemory(memory_key="chat_history")
llm = OpenAI(temperature=0, model_name="text-davinci-003")
search = SerpAPIWrapper()
llm_math_chain = LLMMathChain(llm=llm, verbose=True)

key_rsc = os.environ.get("RSC_API_KEY")

tools = [
    Tool(
        name = "Search",
        func=search.run,
        description="useful for when you need to answer questions about current events. You should ask targeted questions"
    ),
    Tool(
        name="Calculator",
        func=llm_math_chain.run,
        description="useful for when you need to answer questions about math"
    ),
]

agent_state = initialize_agent(tools, llm, agent="conversational-react-description", verbose=True, memory=memory)


def chat(inp, history):
    history = history or []
    if agent_state is None:
        history.append((inp, "Please paste your OpenAI key to use"))
        return history, history
    print("\n==== date/time: " + str(datetime.datetime.now()) + " ====")
    print("inp: " + inp)
    history = history or []
    output = agent_state.run(f"{inp}")
    # answer = output["answer"]
    answer = output
    history.append((inp, answer))
    print(history)
    return history, history


block = gr.Blocks(css="#chatbot .overflow-y-auto{height:500px}")

with block:

    with gr.Row():
        gr.Markdown("<h3><center>Quantum Dolphin 🪄🐬</center></h3>")
        gr.HTML(
            """
        This simple application is an implementation of ChatGPT but can do genome sequencing."""
        )

    chatbot = gr.Chatbot(elem_id="chatbot")
    state = gr.State([])

    with gr.Row():
        message = gr.Textbox(
            label="What's your question?",
            placeholder="What's the answer to life, the universe, and everything?",
            lines=1,
        )
        submit = gr.Button(value="Send", variant="secondary").style(full_width=False)

    gr.Examples(
        examples=[
            "What is the genome sequence of a banana?",
            "How similar is a gorilla to a squid?",
            "Who will win QHack2023?",
        ],
        inputs=message,
    )

    gr.HTML(
        "<center>All rights reserved. <a href='https://quantumdolphin.com'>Quantum Dolphin 🪄🐬</a></center>"
    )

    state = gr.State()


    submit.click(chat, inputs=[message, state], outputs=[chatbot, state])
    message.submit(chat, inputs=[message, state], outputs=[chatbot, state])

    

block.launch(debug=True)