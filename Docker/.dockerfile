FROM Ubuntu

RUN apt-get install python3
RUN pip3 install bottle
RUN pip3 install

COPY . /opt/source-code
ENTRYPOINT BOTTLE_APP=/opt/source-code/app.py bottle app.py