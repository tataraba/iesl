# Inland Empire Soccer League - Proof of Concept

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

This is a proof of concept app for IESL (Inland Empire Soccer League), meant to serve as a place to manage team registration, stats, and scheduling.

## Getting Started <a name = "getting_started"></a>

To get started, clone the repo and make sure you have Python 3.11+ installed in your system.
### Prerequisites

The libraries that you need are in the` requirements.txt` file.

### Installing

After cloning, you will need to create a virtual environment. Navigate to the location where you have cloned the project (your project root) and run the following command in your terminal:

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

This will create sqlite tables and generate a hello world page. This will be updated as progress continues.
