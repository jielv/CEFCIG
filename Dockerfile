FROM python:2.7
RUN pip install numpy
RUN pip install pandas
RUN pip install scipy
RUN pip install sklearn
RUN pip install matplotlib
RUN pip install rpy2
CMD ["python", "./CEFCIG"]
