class Problem:
    def __init__(self,nvideos,nendpoint,nrequest,ncache,cache_size,  videos, endpoints, requests):
        self.nvideos = nvideos # Tal vez no sea necesario
        self.nendpoint = nendpoint # Tal vez no sea necesario
        self.nrequest = nrequest # Tal vez no sea necesario
        self.ncache = ncache # Tal vez no sea necesario
        self.cache_size = cache_size # Tal vez no sea necesario
        self.requests = requests
        self.videos = videos
        self.endpoints = []
        for idx, val in enumerate(endpoints):
            val.ID = idx
            self.endpoints.append(val)

class EndPoint:
    def __init__(self,latency_DC,nCaches,caches):
        self.latency_DC = latency_DC
        self.nCaches = nCaches # Tal vez no sea necesario
        self.caches = caches # Lista de IDServer - Latencia (tublas)

class Request:
    def __init__ (self, IDV, IDE, nRequest):
        self.IDV = IDV
        self.IDE = IDE
        self.nRequest = nRequest