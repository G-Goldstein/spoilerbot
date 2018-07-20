FROM python:3.5

RUN mkdir -p /app/spoiled && \
  useradd -m spoiler && \
  chown -R spoiler:spoiler /app

WORKDIR /app

COPY --chown=spoiler:spoiler requirements.txt /app/

RUN pip3.5 install -r requirements.txt

USER spoiler

ENTRYPOINT ["python"]

CMD ["app.py"]

COPY --chown=spoiler:spoiler app/ /app/
