FROM python:3.8.2-alpine

LABEL maintainer="suhrawardi@gmail.com"

ARG USER_ID
ARG GROUP_ID

RUN apk add --no-cache \
    chromium \
    chromium-chromedriver \
    gcc \
    git \
    libc-dev \
    libxml2-dev \
    libxslt-dev \
    nodejs \
    npm

COPY .env /usr/src/app/
COPY behave_reporter.js /usr/src/app/
COPY entrypoint.sh /usr/bin/
COPY package.json /usr/src/app/
COPY package-lock.json /usr/src/app/
COPY requirements.txt /usr/src/app/

RUN chmod +x /usr/src/app/behave_reporter.js
RUN chmod +x /usr/bin/entrypoint.sh

RUN if [ ${USER_ID:-0} -ne 0 ] && [ ${GROUP_ID:-0} -ne 0 ]; then \
      addgroup --g ${GROUP_ID} test-user && \
      adduser -H -D -u ${USER_ID} -G test-user test-user \
    ;fi

WORKDIR /usr/src/app

RUN npm install

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT [ "/usr/bin/entrypoint.sh" ]
