# AI Code Debugger

This repository contains a minimal prototype of an AI-assisted code debugger. The
application allows a user to paste Python code into a Tkinter GUI, analyses the
code using `pyflakes` and the OpenAI ChatCompletion API, then stores analysis
history in MongoDB.

## Features

- Paste Python code in a text editor widget.
- Detect issues with `pyflakes`.
- Get refactoring suggestions from OpenAI models (default: `gpt-3.5-turbo`).
- Save code and results to MongoDB if a connection string is provided.

## Requirements

- Python 3.11+
- Dependencies from `requirements.txt`
- Environment variables:
  - `OPENAI_API_KEY` – your OpenAI API key.
  - `MONGODB_URI` – optional MongoDB connection string.

## Running

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m app.main
```

This will open a simple GUI where you can paste Python code and obtain analysis
and suggestions.


## Instrukcja w języku polskim

To repozytorium zawiera prototyp narzędzia do analizy kodu Python z
wykorzystaniem AI. Aplikacja pozwala wkleić kod w okno edytora, wyszukuje
błędy za pomocą `pyflakes`, a następnie wysyła kod do modelu OpenAI w celu
uzyskania sugestii refaktoryzacji. Wyniki mogą zostać zapisane w bazie MongoDB.

### Uruchamianie

1. Zainstaluj wymagane biblioteki:

   ```bash
   pip install -r requirements.txt
   ```

2. Ustaw zmienne środowiskowe `OPENAI_API_KEY` oraz opcjonalnie `MONGODB_URI`.

3. Uruchom aplikację poleceniem:

   ```bash
   python -m app.main
   ```

Po uruchomieniu zobaczysz proste okno, w którym możesz wkleić kod Python i
uzyskać podpowiedzi dotyczące błędów oraz możliwych ulepszeń.

