# build stage
FROM python:3.11 AS builddev

RUN apt-get update && apt-get install -y \
    libgl1 \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# refresh system font cache
# フォントを扱う際に推奨されているが意味があるか不明です...
ENV FONTCONFIG_PATH=/etc/fonts
ENV FONTCONFIG_FILE=/etc/fonts/fonts.conf
RUN fc-cache -f -v

# Install project dependencies, without installing the project
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# dev stage
FROM builddev AS rundev

WORKDIR /app
COPY . /app

# devcontainer側で置き換えるのでここでは起動などしなくても良い
CMD ["python"]