import time
import logging
from functools import wraps
from PIL import Image, ImageOps

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def log_inference(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        
        logging.info(f"\n\n--------------------------------------INFERENCE--------------------------------------")
        logging.info(f"Calling function '{func.__name__}' with arguments:")
        logging.info(f"  args: {args}")
        logging.info(f"  kwargs: {kwargs}")
        
        try:
            # 调用被修饰的函数
            result = func(*args, **kwargs)
            
            # 记录函数返回的信息
            logging.info(f"Function '{func.__name__}' returned: {result}")
        except Exception as e:
            # 记录异常信息
            logging.error(f"Function '{func.__name__}' raised an error: {e}")
            raise
        finally:
            # 记录函数执行的时间
            end_time = time.time()
            logging.info(f"Function '{func.__name__}' executed in {end_time - start_time:.4f} seconds")
        
        return result
    return wrapper

@log_inference
def inference(img: Image.Image, inference_mode: str):
    if inference_mode == 'mode1':
        result = 'True or False'
    elif inference_mode == 'mode2':
        result = 'True'
    else:
        result = 'False'
    return result

