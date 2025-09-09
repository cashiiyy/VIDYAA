# example Dockerfile (Python)
FROM python:3.11-slim

# set working dir
WORKDIR /app

# copy dependency files first for caching
COPY requirements.txt ./

# install deps
RUN pip install --no-cache-dir -r requirements.txt

# copy rest of the source
COPY . .

# don't run as root
RUN useradd -m appuser
USER appuser

# unbuffered stdout for logs
ENV PYTHONUNBUFFERED=1

# run your agent (change agent.py if your file name differs)
CMD ["python", "agent.py", "start"]