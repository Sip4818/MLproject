import logging
from datetime import datetime
import os

file_format=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
file_path=os.path.join(os.getcwd(),"logs",file_format)
os.makedirs(file_path,exist_ok=True)

logging.basicConfig(
    filename=file_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,

)
