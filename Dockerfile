FROM ubuntu:latest
ENV  PATH="$PATH:/usr/games"
RUN apt-get update && apt-get install -y \
  cowsay \
  fortune-mod bash \
  netcat-openbsd \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY wisecow.sh .
RUN chmod +x wisecow.sh
EXPOSE 4499
CMD ["sh", "wisecow.sh"]
