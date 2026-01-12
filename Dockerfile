FROM python:3.11-slim


COPY .env .
COPY agent.py .
COPY main.py .
COPY prompt_generator.py .
COPY prompts.json .
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["streamlit", "run", "main.py", "--server.fileWatcherType=none"]



