FROM python:3.8.18

RUN apt-get update -y \
  && apt-get install libgdal-dev -y

ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

COPY . .

RUN python -m pip install --upgrade pip
RUN pip install numpy==1.24.4
RUN pip install GDAL==3.6.2
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]