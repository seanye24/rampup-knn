FROM amazonlinux:latest

WORKDIR /app
COPY . .
RUN yum install -y python3
RUN mkdir csv
RUN cd scripts && ./generate-input.sh 10 10 5 # generate random input
# CMD ["python3", "main.py", "csv/index.csv", "csv/query.csv", "l2", "4", "csv/output.csv"]
RUN python3 main.py csv/index.csv csv/query.csv l2 4 csv/output.csv
