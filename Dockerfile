FROM python:3.10
ADD . .
RUN pip install -r requirements.txt
COPY . .
WORKDIR /tests/
CMD ["pytest"]