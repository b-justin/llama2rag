import requests
import streamlit as st

api = st.secrets.TOGETHER_API_KEY


url = "https://api.together.xyz/inference"

headers = {
    "Authorization": f"Bearer {api}",
    "Content-Type": "application/json",
}


def llama(
    question,
    context="",
    add_inst=True,
    model="togethercomputer/llama-2-70b-chat",
    temperature=0.0,
    max_tokens=1024,
    url=url,
    headers=headers,
):

    if context:
        prompt = f"[CONTEXT] {context.strip()} \\n [PROMPT] {question.strip()}"
    else:
        prompt = question.strip()

    if add_inst:
        prompt = f"[INST]{prompt}[/INST]"

    data = {
        "model": model,
        "prompt": prompt,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    response = requests.post(url, headers=headers, json=data)

    return response.json()["output"]["choices"][0]["text"]
