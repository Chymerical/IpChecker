FROM ubuntu
RUN apt-get update && apt-get install -y python3
COPY ip-reporter.py /usr/local/bin/ip-reporter
RUN chmod +x /usr/local/bin/ip-reporter
ENV CONTAINER_NETWORK=192.168.1.0/24
CMD ["python3", "/usr/local/bin/ip-reporter"]