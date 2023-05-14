import datetime
import string


class PrivateKeyRing:
    timestamp: datetime
    keyId: int
    publicKey: int
    privateKey: int
    userId: string

    def __init__(self, timestamp, keyId, publicKey, privateKey, userId) -> None:
        super().__init__()
        self.timestamp = timestamp
        self.keyId = keyId
        self.publicKey = publicKey
        self.privateKey = privateKey
        self.userId = userId


privateKeyRing = list()
