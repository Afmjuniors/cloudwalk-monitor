# CloudWalk Task 2

Brief description of the project.
## Table of Contents

- [Description](#description)
- [Architecture](#architecture)
- [Usage](#usage)
  - [Running with Docker](#running-with-docker)
  - [Running without Docker](#running-without-docker)
- [API Documentation](#api-documentation)

## Description

The project aims to perform real-time analysis of transactions and send email alerts based on defined rules. It is composed of multiple classes and packages that perform specific functions within the system.

## Architecture

The project structure is organized as follows:

- `alert/`: Python package containing the `SendEmail.py` class for email sending.
- `business/`: Python package containing the `TransactionsBusiness.py` class for transaction handling.
- `controller/`: Python package containing the `TransactionsController.py` class for transaction control.
- `database/`: Python package containing the `base_database.py` class for database manipulation and the `TransactionsDatabase.py` class for transaction manipulation in the database.
- `models/`: Python package containing the `transaction.py` class for representing transactions.
- `monitor/`: Python package containing the `realtime_monitor.py` script for real-time monitoring.
- `utils/`: Python package containing the `helper.py`  with helper functions.

Other important files and directories include:

- `.env.example`: Example files for variables that store project configurations.
- `app.py`: Main file of the application that contains the Flask server.
- `Dockerfile`: Docker file to create the application container image.
- `files_to_database.py`: File to import data into the database from CSV files.
- `README.md`: This documentation file.
- `requirements.txt`: File listing Python dependencies for the project.
- `tests.py`: File containing automated tests.

## Usage

### Running with Docker

To run the project using Docker, follow these steps:

1. Make sure you have Docker installed on your system.

2. Build the Docker image using the following command:
``
docker build -t project-name .
``

Replace `project-name` with a suitable name for your Docker image.

3. Run a Docker container based on the image using the following command:
``
docker run -p 5000:5000 project-name
``

Replace `project-name` with the name of your Docker image.

4. The Flask server will be running inside the Docker container and accessible at `http://localhost:5000`.

### Running without Docker

If you prefer to run the project without Docker, follow these steps:

1. Install project dependencies by running the following command:
``
pip install -r requirements.txt
``

2. Configure the required environment variables in the `.env` file (refer to `.env.example` file for an example).

3. Run the application using the following command:
``
python app.py
``

4. The Flask server will be running on port 5000. You can access the application at `http://localhost:5000`.


## API Documentation

For detailed information on the API endpoints and their usage, please refer to the [API Documentation](https://documenter.getpostman.com/view/24460683/2s93si1prr).