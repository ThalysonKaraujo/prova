class HashMap:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    #put
    def put(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k,v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        bucket.append((k,v))

    def get(self,key):
        index = self._hash(key)
        bucket  = self.buckets[index]

        for k,v in bucket:
            if k == key:
                return v
        return None
    #get
    #delete

        