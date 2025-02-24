FROM ubuntu
COPY ip-reporter /usr/local/bin/ip-reporter
RUN chmod +x /usr/local/bin/ip-reporter
ENV CONTAINER_NETWORK=192.168.1.0/24
CMD ["ip-reporter"]