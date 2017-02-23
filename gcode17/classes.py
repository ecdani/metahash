class Problem:
    def __init__(self,nvideos,nendpoint,nrequest,ncache,cache_size,  videos, endpoints, requests):
        self.cache_size = cache_size
        self.nvideos = nvideos # Tal vez no sea necesario
        self.nendpoint = nendpoint # Tal vez no sea necesario
        self.nrequest = nrequest # Tal vez no sea necesario
        self.ncache = ncache # Tal vez no sea necesario
        self.caches = [] # Tal vez no sea necesario
        self.requests = requests
        self.videos = videos
        self.endpoints = []
        for idx, val in enumerate(endpoints):
            val.ID = idx
            self.endpoints.append(val)

        for n in range(ncache):
            self.caches.append(Cache(cache_size,n))

        def videoInCache(IDC, IDV):
            # comprobar si en esa caché está ese video
            for i in range(self.caches[IDC].videos)
                if self.caches[IDC].videos[i] == IDV:
                    return True
            return False

        def videoFit (IDC,IDV):
            # Comprobar si el video cabe en la cache
            return  (self.caches[IDC].size_cache >= self.videos[IDV])
        
        def videoPush (IDC, IDV):
            self.caches[IDC].videos.append(IDV)
        
        # Numero de cachés que tienen algún video dentro
        def notEmptyCache():
            nNotEmpty = 0
            for i,c in enumerate(self.caches)
                if len(c.videos) != 0:
                    nNotEmpty += 1
            return nNotEmpty



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

class Cache:
    def __init__ (self,size_cache, IDC):
        self.videos = []
        self.size_cache = size_cache
        # Añadir ID
        self.IDC = IDC
    # Is Empty?
    def Empty(self):
        return (len(self.videos) == 0)
    
    def __str__(self):
        return str(self.IDC) + ' '.join(str(x) for x in self.videos)