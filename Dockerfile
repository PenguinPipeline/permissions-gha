FROM python:3

#Set via GITHUB_WORKSPACE environment variable
WORKDIR /app

# Copy in the files from source control to the container
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
# ENV PYTHONPATH /app
RUN chmod +x /app/app.py
# CMD ["/app/app.py" ]
ENTRYPOINT ["python" , "/app/app.py"]