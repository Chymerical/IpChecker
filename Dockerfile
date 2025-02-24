FROM ubuntu
COPY IpChecker /usr/local/bin/ip-tool
RUN chmod +x /usr/local/bin/IpChecker.
ENV CONTAINER_NETWORK=192.168.1.0/24
CMD ["IpChecker"]