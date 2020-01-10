#!/usr/bin/env python3
import glob
import logging
import os
import shutil
import sys

DOCS_REPO = "https://github.com/BitcoinUnlimited/BitcoinCashSpecification.git"
DOCS_DIR = "docs"

logging.basicConfig(format = '%(asctime)s.%(levelname)s: %(message)s',
        level=logging.INFO,
        stream=sys.stdout)

try:
    import git
except Exception as e:
    logging.error("Failed to 'import git'")
    logging.error("Tip: On Debian/Ubuntu you need to install python3-git")
    logging.error("You can also try pip3 install python-git")
    logging.error(e)
    sys.exit(1)

if not os.path.exists("docs"):
    logging.info(f"Folder {DOCS_DIR} does not exist, cloning from {DOCS_REPO}")
    git.Repo.clone_from(DOCS_REPO, DOCS_DIR)
else:
    repo = git.Repo(DOCS_DIR)
    if repo.is_dirty():
        logging.error(f"Docs repo {DOCS_DIR} has local modifications, cannot update.")
        sys.exit(1)

    logging.info(f"Pulling changes from {DOCS_REPO} to {DOCS_DIR}")
    repo.remotes.origin.pull()

# mkdocs expects there to be a index.md, while the spec has named this file
# home.md
os.rename("docs/home.md", "docs/index.md")

# copy static files, they need to be in docs root
for f in glob.glob(os.path.join("static", "*.*")):
    shutil.copy(f, "docs/")

logging.info("DONE")
