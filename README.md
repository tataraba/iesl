# Inland Empire Soccer League - Proof of Concept

## Table of Contents

- [Inland Empire Soccer League - Proof of Concept](#inland-empire-soccer-league---proof-of-concept)
  - [Table of Contents](#table-of-contents)
  - [About ](#about-)
  - [Getting Started ](#getting-started-)
    - [Prerequisites](#prerequisites)
    - [Installing](#installing)
    - [Just Go](#just-go)
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

Your first step should be cloning this repository for yourself. Once you have it in your system, navigate to the project folder and use one of the methods below for getting started.

### Just Go

The quickest way to get going is using the `just go` command. Of course, to do that, you will need to have [`just` installed](https://just.systems/man/en/chapter_1.html). Thankfully, there are [various ways to do that](https://just.systems/man/en/chapter_4.html) for just about any operating system.

Once you have it installed, you can type `just` in your terminal to access a list of recipes available to you:

```
Available recipes:
    bootstrap     # installs/updates all dependencies
    create_venv   # create a virtual environment and upgrade pip
    go            # starts app, installing all dependencies if needed
    reqs          # updates requirements.txt with hashed dependencies
    setup         # sets up a project to be used for the first time
    start_app     # start the application
    test          # runs tests
```

When you're ready, type the following in your terminal:

```
just go
```

This will attempt to run the app. If it doesn't find the correct dependencies, it will do all the setup for you. The first time you do this, it may take a few minutes for your virtual environment to be created and dependencies to be installed.

Once that is complete, the application will be started (this will also create a series of SQLite tables).

At the end, you should have the application running on http://127.0.0.1:8000!


#### Using PDM

As implied above, I use [PDM](https://pdm.fming.dev/latest/) as my package manager. If you have PDM installed, you can also get started by typing:

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

(Now you can navigate to the project root and run the `pdm install` command as noted above.)

#### Using venv

You can also get started more traditionally by creating your own virtual environment and installing dependencies using `pip`.

Make sure you're at the project root and type:

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

You can then start the application by running the following command(s):

```
# using just
just go

# or, make sure you've activated your virtual environment
uvicorn app.main:app --reload
```

Your first time, this will create SQLite tables and generate the main page. This section will be updated as progress continues.


## Testing <a name = "testing"></a>

You can run tests by typing this in your terminal:

```
pytest
```

Right now, the test passes if the application starts up successfully and sends a 200 response.

Pytest configurations are contained in `pyproject.toml`.