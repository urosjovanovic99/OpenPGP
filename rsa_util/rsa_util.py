import rsa
from key_rings.enumerations import KEY


def generate_keys(nbits):
    (publicKey, privateKey) = rsa.newkeys(nbits)
    return publicKey, privateKey


def import_from_file(path, keyType):
    with open(path, mode='rb') as file:
        keydata = file.read()
    key = None
    if keyType == KEY.PRIVATE:
        key = rsa.key.PrivateKey.load_pkcs1(keydata)
    elif keyType == KEY.PUBLIC:
        key = rsa.key.PublicKey.load_pkcs1(keydata)
    return key


def export_to_file(path, key: rsa.key.AbstractKey):
    content = key.save_pkcs1()
    file = open(path, "w")
    file.write(content)
