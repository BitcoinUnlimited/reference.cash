FROM python:3

WORKDIR /workdir
COPY mkdocs-referencecash-plugin /workdir/mkdocs-referencecash-plugin
COPY custom_theme /workdir/custom_theme
COPY fetch-docs.py /workdir/fetch-docs.py
COPY dockerentry.sh /workdir/dockerentry.sh

RUN pip install --no-cache-dir mkdocs
# Implicit requirement of referencecash plugin
RUN pip install --no-cache-dir bs4
RUN pip install --no-cache-dir python-git
RUN pip install --no-cache-dir pymdown-extensions
RUN (cd mkdocs-referencecash-plugin; python3 setup.py install)

WORKDIR /workdir

EXPOSE 8000

ENTRYPOINT ["/workdir/dockerentry.sh"]
