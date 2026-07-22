FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends tk && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml README.md main.py ./
COPY src ./src

RUN python -m pip install --no-cache-dir --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org .

ENTRYPOINT ["python","main.py"]
CMD ["--help"]
