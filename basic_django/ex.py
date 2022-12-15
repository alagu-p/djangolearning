from django.core.signing import TimestampSigner
from django.core import signing
import sys
signer = TimestampSigner()

x = signer.sign_object({'user_id': '1'})

try:
    original = signer.unsign_object(x, max_age=5)
    print("successful")
except signing.BadSignature:
    print("securty Warning")
    sys.exit()
