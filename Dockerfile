# select operator
FROM python:3.9-slim-buster
# copy all the files and mkdir in container called 'app'
COPY . /app
# specify the directory it should look at to run the app
WORKDIR /app
# create virtual environment
#ENV VIRTUAL_ENV=/opt/venv
#RUN python3 -m venv $VIRTUAL_ENV
#ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ADD . /app
# install requirements.txt
RUN pip3 install -r requirements.txt
# copy files intp the image
COPY . .
# add entrypoint
#ENTRYPOINT FLASK_APP=main flask run --host=0.0.0.0
# empty port
EXPOSE 5000
# make the file executable
#RUN chmod a+x run.sh
# command to run the code
#CMD ["./run.sh"]
CMD [ "python", "app.py" ]