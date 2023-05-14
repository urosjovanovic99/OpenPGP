import datetime
import string
import uuid


class PrivateKeyRing:
    timestamp: datetime
    keyId: uuid
    publicKey: int
    privateKey: int
    userId: string

    def __init__(self, timestamp, publicKey, privateKey, userId) -> None:
        super().__init__()
        self.timestamp = timestamp
        self.keyId = uuid.uuid4()
        self.publicKey = publicKey
        self.privateKey = privateKey
        self.userId = userId


privateKeyRing = list()
