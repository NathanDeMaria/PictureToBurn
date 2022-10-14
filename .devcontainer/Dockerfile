FROM python:3.10@sha256:745efdfb7e4aac9a8422bd8c62d8bc35a693e8979a240d29677cb03e6aa91052

# For persisting bash history
RUN SNIPPET="export PROMPT_COMMAND='history -a' && export HISTFILE=/commandhistory/.bash_history" && echo $SNIPPET >> "/root/.bashrc"

# Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - --version 1.2.0
ENV PATH /root/.local/bin:${PATH}

# Is this a good way to add stuff on load?
# Not sure, but it's working
COPY profile.sh /root/profile.sh
RUN echo ". profile.sh" >> "/root/.bashrc"

RUN apt-get update && apt-get install ffmpeg=7:4.3.4-0+deb11u1 -y

COPY poetry.* ./
COPY pyproject.toml ./
RUN poetry install
