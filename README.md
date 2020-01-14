# reference.cash

This is the code for [reference.cash](https://reference.cash)

# Serve as HTML

## One-time setup

```
pip3 install mkdocs
pip3 install bs4
pip3 install python-git
pip3 install pymdown-extensions
(cd mkdocs-referencecash-plugin; sudo python3 setup.py install)
```

## Run

To fetch latest documents
```
./fetch-docs.py
```
To start mkdocs server
```
mkdocs serve
```

# Docker

```
docker build -t buwiki .
```

## Run
```
./start-docker.sh
```
