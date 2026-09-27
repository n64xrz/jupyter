# Jupyter DEV

This repository is intended for developing in Jupyter.

---

## Overview

The Jupyter notebook allows you to selectively mount repositories as a working session with correct paths, enabling normal imports as if they were installed. Follow the steps below to configure and manage your environment.

---

## Configuration

### 1. Mark Directories as Safe

Periodically update the repositories to stay in sync with the latest changes. Use the following script to pull updates for each repository:

```bash
# mark safe
git config --global --add safe.directory /home/jupyter/src/analytics
git config --global --add safe.directory /home/jupyter/src/crawler
git config --global --add safe.directory /home/jupyter/src/gat
git config --global --add safe.directory /home/jupyter/src/jupyter
git config --global --add safe.directory /home/jupyter/src/nets
git config --global --add safe.directory /home/jupyter/src/routes
git config --global --add safe.directory /home/jupyter/src/scheduler
git config --global --add safe.directory /home/jupyter/src/search
git config --global --add safe.directory /home/jupyter/src/transformer

#pull
cd /home/jupyter/src/analytics
git pull
cd ../crawler
git pull
cd ../gat
git pull
cd ../jupyter
git pull
cd ../nets
git pull
cd ../routes
git pull
cd ../scheduler
git pull
cd ../search
git pull
cd ../transformer
git pull
```