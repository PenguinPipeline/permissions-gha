FROM python:3

#Set via GITHUB_WORKSPACE environment variable
# WORKDIR /github/home

# Copy in the files from source control to the container
COPY . /github/workspace

RUN pip install --no-cache-dir -r requirements.txt
# ENV PYTHONPATH /app
RUN chmod +x /github/workspace/app.py
# CMD ["/app/app.py" ]
ENTRYPOINT ["python" , "/github/workspace/app.py"]