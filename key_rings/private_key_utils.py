from key_rings.private_key_ring import privateKeyRing


def get_private_key_by_id(ring_id):
    for key in privateKeyRing:
        if key.id == ring_id:
            return key
    return None


def get_property_by_value(name, ring):
    if name == 'N':
        return ring.n
    elif name == 'D':
        return ring.d
    return None
