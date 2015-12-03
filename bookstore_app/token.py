import os
import base64
import hmac
import hashlib

def IssueToken(string):
    signature = hmac.new(os.environ.get('APP_SECRET'), string, digestmod=hashlib.sha256).hexdigest()
    concat_str = string + ' ' + signature
    return base64.b64encode(concat_str)

def VerifyToken(token):
    decoded_string = base64.b64decode(token)
    split_string = (" ".join(decoded_string.split(' ')[:-1]), decoded_string.split(' ')[-1])
    check_signature = hmac.new(os.environ.get('APP_SECRET'), split_string[0], digestmod=hashlib.sha256).hexdigest()
    if hmac.compare_digest(split_string[-1], check_signature):
        return True
    else:
        return False