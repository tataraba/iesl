# Set shell for Windows OSs (PowerShell Core):
set windows-shell := ["pwsh.exe", "-NoLogo", "-Command"]
set dotenv-load := false

bool_prefix := if os_family() == "windows" { "$" } else { "" }
python_dir := if os_family() == "windows" { ".venv/Scripts" } else { ".venv/bin" }
python := python_dir + if os_family() == "windows" { "/python.exe" } else { "/python" }
system_python := if os_family() == "windows" { "py.exe" } else { "python" }
uvicorn := python_dir + if os_family() == "windows" { "/uvicorn.exe" } else { "/uvicorn" }
uvicorn_exists := bool_prefix + path_exists(uvicorn)
venv_exists := bool_prefix + path_exists(".venv")
venv_activate := python_dir + if os_family() == "windows" { "/activate.bat" } else { "/activate" }


@_default:
    just --list

@_venv:
    {{ system_python }} -m venv .venv --upgrade-deps

@_venv_pdm:
    just create_venv
    {{ python }} -m pip install pdm
    {{ venv_activate }} && echo "Installing dependencies with PDM" && pdm install

# create a virtual environment and upgrade pip
@create_venv:
    if (-not ( {{ venv_exists }} )) { just _venv } else { echo 'Virtual environment already exists' }

# start the application
@start_app:
    if ((-not {{ uvicorn_exists }} )) { just setup } else { echo "Starting app..." }
    {{ uvicorn }} app.main:app --reload

# installs/updates all dependencies
@bootstrap:
    pdm install || just _venv_pdm

# run '--fmt' in "check" mode.
@check:
    just --check --fmt --unstable

# format and overwrite justfile
@fmt:
    just --fmt --unstable

# starts app
@go:
    {{ uvicorn }} app.main:app --reload || \
    just start_app

# sets up a project to be used for the first time
@setup:
    echo "Setting up your project... "
    just bootstrap
    tailwindcss_install

# runs tests
@test:
    pytest

# updates requirements.txt with hashed dependencies
@reqs:
    pdm export -o requirements.txt
