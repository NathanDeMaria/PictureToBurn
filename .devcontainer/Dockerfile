# 3.11.0-bullseye on 2022-10-30
FROM python@sha256:3e2e743ca3027c375a13ee7b9b0f7757b0091501a7556563afbc8000b5c862a5

# For persisting bash history
RUN SNIPPET="export PROMPT_COMMAND='history -a' && export HISTFILE=/commandhistory/.bash_history" && echo $SNIPPET >> "/root/.bashrc"

# Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - --version 1.2.2
ENV PATH /root/.local/bin:${PATH}

# Is this a good way to add stuff on load?
# Not sure, but it's working
COPY profile.sh /root/profile.sh
RUN echo ". profile.sh" >> "/root/.bashrc"

RUN apt-get update && apt-get install ffmpeg=7:4.3.4-0+deb11u1 -y

# Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' && \
    apt-get update && \
    apt-get install -y google-chrome-stable=107.0.5304.87-1
# Chromedriver
RUN wget -O /tmp/driver.zip https://chromedriver.storage.googleapis.com/106.0.5249.61/chromedriver_linux64.zip && \
    unzip /tmp/driver.zip -d /usr/local/bin/ && \
    rm /tmp/driver.zip

COPY poetry.* ./
COPY pyproject.toml ./
RUN poetry install
