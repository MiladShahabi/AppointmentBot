








FROM python:latest as compiler
ENV PYTHONUNBUFFERED 1
ENV PATH $PATH:env/bin
ENV PATH $PATH:env/bin/activate
RUN . env/bin/activate
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH


WORKDIR /app/

RUN python -m venv /opt/venv
# Enable venv
ENV PATH="/opt/venv/bin:$PATH"

COPY ./requirements.txt /app/requirements.txt
RUN pip install -Ur requirements.txt




FROM python:3.9-slim as runner
WORKDIR /app/
COPY --from=compiler /opt/venv /opt/venv

# Enable venv
ENV PATH="/opt/venv/bin:$PATH"
COPY . /app/
CMD ["python", "app.py", ]




FROM python:2.7

RUN virtualenv /ve
RUN /ve/bin/pip install somepackage

CMD ["/ve/bin/python", "yourcode.py"]






FROM python:2.7

RUN virtualenv /ve
ENV PATH="/ve/bin:$PATH"
RUN pip install somepackage

CMD ["python", "yourcode.py"]




ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH




RUN virtualenv env                       # setup env
RUN which python                         # -> /usr/bin/python
RUN . /env/bin/activate && which python  # -> /env/bin/python
RUN which python                         # -> /usr/bin/python





RUN virtualenv env
ENV VIRTUAL_ENV /env                     # activating environment
ENV PATH /env/bin:$PATH                  # activating environment
RUN which python                         # -> /env/bin/python



FROM python:2.7

RUN virtualenv virtual
RUN /bin/bash -c "source /virtual/bin/activate && pip install pyserial && deactivate"




CMD ["/bin/bash", "-c", "source <your-env>/bin/activate && cd src && python main.py"]

RUN pip install virtualenv
RUN virtualenv -p python3.5 virtual
RUN /bin/bash -c "source /virtual/bin/activate"




# Use an official Python runtime as a parent image
FROM python:3.12.0b3-alpine

LABEL Maintainer="Milad"

# Set the working directory in the container
WORKDIR /usr/src/app



# Install python module
RUN pip install selenium 
RUN pip install webdriver-manager
RUN pip install pyTelegramBotAPI
RUN pip install termcolor
RUN pip install anticaptchaofficial


# Install Chrome and Chromedriver
RUN apt-get update && apt-get install -y \
  unzip \
  libglib2.0-0 \
  libnss3 \
  libx11-6 \
  net-tools \
  nano 

ADD https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb /chrome.deb
ADD https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip /usr/local/bin/chromedriver

RUN dpkg -i /chrome.deb || apt-get install -fy
RUN unzip /usr/local/bin/chromedriver && rm /usr/local/bin/chromedriver

# Make port 443 available to the world outside this container
EXPOSE 443

# Copy the current directory contents into the container
COPY /mybot/src/roya_3233.py /usr/src/app/termin_bot_app.py
# Run the python script when the container launches
CMD ["python3", "termin_bot_app.py"]

