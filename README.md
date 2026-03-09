# Simple `taskipy` case

This repository contains a very simple use case for downloading a dataset using the Taskipy tool.

## Usage

To run the project via `uv`, after cloning, use the following command:

```
uv sync
```

After the dependencies have been installed in the new virtual environment, you can activate it using:

```
source .venv/bin/activate
```

Or you can run any command without activating the environment using

```
uv run <comand>
```

### Authentication

The use case utilizes the `kaggle` library, which is an interface to the Kaggle API, therefore you need a Kaggle API token. To obtain a Kaggle API token, you will first need a Kaggle account. You can sign up [here](https://www.kaggle.com/).

After logging in, you can download your Kaggle API credentials at https://www.kaggle.com/settings by clicking on the "**Generate New Token**" button under the "API" section.

With the token, create a `.env` file with the following content:

```
KAGGLE_API_TOKEN=<your_kaggle_api_token>
```

## Task runing

The pyproject.py file contains only one task for downloading data. To run this task, with the virtual environment activated,)use the following command:

```
task dataset
```

or without the virtual environment activated by using:

```
uv run task dataset
```

After running, the task will create the `data/raw` directory, download the data files, and unpack them in `data/raw` folder. After that, you can use the data files in your analyses.