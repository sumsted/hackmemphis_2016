import inspect
import time


def logit(message, level="INFO"):
    try:
        calling_module_stack = inspect.stack()[1]
        line_number = calling_module_stack[2]
        calling_module = inspect.getmodule(calling_module_stack[0])
        module_name = calling_module.__name__
    except:
        line_number = 0
        module_name = ''
    print('%s: %s: %s: %d: %s' % (
        time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()), level, module_name, line_number, str(message)))
