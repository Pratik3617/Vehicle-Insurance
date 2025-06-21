# from src.logger import logging

# logging.debug("This is a debug message")

# # below code is to check the exception config
# from src.logger import logging
# from src.exception import MyException
# import sys

# try:
#     a = 1+'Z'
# except Exception as e:
#     logging.info(e)
#     raise MyException(e, sys) from e

from dotenv import load_dotenv
import os

load_dotenv()  # This loads variables from .env

mongodb_url = os.getenv("MONGODB_URL")

print("MONGODB_URL from .env:", mongodb_url)

from src.pipeline.training_pipeline import TrainPipeline

pipeline = TrainPipeline()
pipeline.run_pipeline()