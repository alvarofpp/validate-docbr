FROM python:3.12.1-slim

# Virtual environment
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install requirements
# hadolint ignore=DL3013
RUN pip3 install --no-cache-dir --upgrade pip
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir --requirement /tmp/requirements.txt

# Set environment variables
ENV WORKDIR=/app
WORKDIR ${WORKDIR}
