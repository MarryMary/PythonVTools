import hashlib, os, base64

# list_key_exists function is judge key exists in target list
def list_key_exists(key: int, target_list: list):
    if(key < len(target_list)):
        return True
    else:
        return False

# dict_key_exists function is judge key exists in target dictionary
def dict_key_exists(key, target_dict: dict):
    if(key in target_dict):
        return True
    else:
        return False

# array_key_exists function is judge key exists in target list or dict
def array_key_exists(key, target_array):
    if(type(target_array) is dict):
        return dict_key_exists(key, target_array)
    elif(type(target_array) is list):
        if(type(key) is int):
            return list_key_exists(key, target_array)
        else:
            #exception throw here
            return False
    else:
        #exception throw here
        return False

# is_null function is judge the target is null(none) in python
def is_null(needle):
    if(needle is None):
        return True
    else:
        return False

# is_none function is is_null function's alias
def is_none(needle):
    return is_null(needle)

# htmlspecialchars function is detoxifying html special chars(e.g. &, <>)
def htmlspecialchars(text: str):
    return text.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;")

# ltrim is left triming string from string.
def ltrim(target, criterion = " "):
    return target.lstrip(criterion)

# rtrim is right triming string from string
def rtrim(target, criterion = " "):
    return target.rstrip(criterion)

# trim is right and left triming string from string
def trim(target, criterion = " "):
    return target.strip(criterion)

def str_replace(search, replace, string):
    return string.replace(search, replace)

def is_array(search):
    if(is_dict(search) or is_list(search)):
        return True
    else:
        return False

def is_list(search):
    if(type(search) is list):
        return True
    else:
        return False

def is_dict(search):
    if(type(search) is dict):
        return True
    else:
        return False

def strtolower(string: str):
    return string.lower()

def strtoupper(string: str):
    return string.upper()

def count(target):
    return len(target)

def length(target):
    return len(target)

def can_cast_int(target):
    try:
        int(target)
    except ValueError:
        return False
    else:
        return True

def explode(separate, target):
    return target.split(separate)

def strcspn(target, needle):
    return target.find(needle)

def substr(target: str, start: int, end: int):
    return target[start:end]

def method_exists(instance, MethodName: str):
    if(instance.__dict__[MethodName]):
        return True
    else:
        return False

def password_hash(password: str):
    salt = base64.b64encode(os.urandom(32))
    separator = "$"
    loop = 100000
    digest = hashlib.pbkdf2_hmac('sha256', bytes(password, 'utf-8'), salt, loop).hex()
    digest = str(salt).lstrip("b'").rstrip("'") + separator + str(loop) + separator + digest
    return digest

def password_verify(hashed_password: str, input_password: str):
    hashed_password = hashed_password.split("$")
    salt = hashed_password[0].encode()
    loop = hashed_password[1]
    hashed_password = hashed_password[2]
    digest = hashlib.pbkdf2_hmac('sha256', bytes(input_password), salt, loop).hex()
    if(digest == hashed_password):
        return True
    else:
        return False
    
def SecFromMin(min: int):
    return min*60

def MinFromTime(time: int):
    return time*60

def SecFromTime(time: int):
    return MinFromTime(time)*60

def TimeFromSec(sec: int):
    return MinFromSec(sec)/60

def MinFromSec(sec: int):
    return sec/60
