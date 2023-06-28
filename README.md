# Inland Empire Soccer League - Proof of Concept

## Table of Contents

- [Inland Empire Soccer League - Proof of Concept](#inland-empire-soccer-league---proof-of-concept)
  - [Table of Contents](#table-of-contents)
  - [About ](#about-)
  - [Getting Started ](#getting-started-)
    - [Prerequisites](#prerequisites)
    - [Installing](#installing)
      - [Using PDM](#using-pdm)
      - [Using venv](#using-venv)
  - [Usage ](#usage-)
  - [Testing ](#testing-)

## About <a name = "about"></a>

This is a proof of concept app for IESL (Inland Empire Soccer League), meant to serve as a place to manage team registration, stats, and season schedule.

## Getting Started <a name = "getting_started"></a>

This application is built using the [PyHAT stack](https://github.com/PyHAT-stack/awesome-python-htmx).

What is 🐍🤠?

It represents a web application using Python, [htmx](https://htmx.org), ASGI, and [TailwindCSS](https://tailwindcss.com).

More specifically, the web framework is [FastAPI](https://fastapi.tiangolo.com). A combination of [Jinja templates](https://jinja.palletsprojects.com/en/3.1.x/) and htmx provides the front end experience.

The database ORM is [SQLModel](https://sqlmodel.tiangolo.com), utilizing SQLite (for the time being) as the storage solution.


### Prerequisites

You must have **Python 3.11** installed. Compatibility with earlier versions is likely, but not guaranteed.

The rest of the dependencies are in the `pyproject.toml` file listed under `dependencies`. Also, note that there are development dependencies under the `[tool.pdm.dev-dependencies]` table.

All dependencies are also exported to the `requirements.txt` file.

### Installing

#### Using PDM

As implied above, I use [PDM](https://pdm.fming.dev/latest/) as my package manager. If you have PDM installed, all you need to do to get started is clone the repo and run the following command:

```
pdm install
```

This will create a virtual environment and install all the required dependencies.

If you do not have PDM installed, my recommendation would be to first install [pipx](https://pypa.github.io/pipx/).

>**Note** From the pipx documentation:
>
> pipx is a tool to help you install and run end-user applications written in Python. It's roughly similar to macOS's brew, JavaScript's npx, and Linux's apt.
>
> It's closely related to pip. In fact, it uses pip, but is focused on installing and managing Python packages that can be run from the command line directly as applications.

To install pipx:

```
# On Windows
python -m pip install --user pipx
pipx ensurepath  # Only needed if installation generated a WARNING

# On MacOS/Linux
$ brew install pipx
$ pipx ensurepath
```

Once you have successfully installed pipx, you can install Python CLI tools/apps into an isolated environment that you can then access in anywhere in your shell/terminal session.

To install PDM into this isolated environment, just run:

```
pipx install pdm
```

This will then allow you to use the `pdm` CLI within any python project.

(Now you can navigato to the project root and run the `pdm install` command as noted above.)

#### Using venv

You can also get started more traditionally by creating your own virtual environment and installing dependencies using `pip`.

After cloning, navigate to the location where you have cloned the project (your project root) and run the following command in your terminal:

```
python -m venv .venv
```

This will create a `.venv` directory within your project.

Next, activate your environment:

```
# On Windows
.\.venv\Scripts\activate

# On MacOS/Linux
$ source .venv/bin/activate
```

Then, install the requirements:

```
python -m pip install -r requirements.txt
```

## Usage <a name = "usage"></a>

You can then start the application by running the following command:

```
uvicorn app.main:app --reload
```

This will create sqlite tables and generate the main page. This section will be updated as progress continues.


## Testing <a name = "testing"></a>

You can run tests by typing this in your terminal:

```
pytest
```

Right now, the test passes if the application starts up successfully and sends a 200 response.

Pytest configurations are contained in `pyproject.toml`.