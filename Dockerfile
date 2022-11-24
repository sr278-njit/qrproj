FROM python:3.8-slim-buster
WORKDIR /app

ENV QR_CODE_IMAGE_DIRECTORY='images'
ENV QR_CODE_DEFAULT_URL='https://www.njit.edu'
ENV QR_CODE_DEFAULT_FILE_NAME='default.png'

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "main.py"]