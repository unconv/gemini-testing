# Gemini API examples

These are some examples of using the Gemini API in Python

## API Key Setup

Get your API-key [here](https://ai.google.dev) and export it as an environment variable.

```shell
$ export GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
```

## Basic Usage

In `basic.py` there is a simple demo of creating a basic chat completion

## Streaming

In `stream.py` there is an example of streaming the chat completion.

## Chat (easy way)

In `chat.py` there is a simple terminal chatbot implementation using the `ChatSession`` class

## Chat (harder way)

In `hard_chat.py` there is a terminal chatbot implementation using `generate_content()` with a list of messages directly.

## Vision

In `vision.py` there is a demo of the `gemini-pro-vision` model

## Function calling

In `gemini-ai-agent` three is a demo of an AI agent that can write to files, using Gemini
