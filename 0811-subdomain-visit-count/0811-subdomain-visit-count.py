class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain = collections.defaultdict(int)
        for s in cpdomains:
            v, d = s.split()
            k, v = '', int(v)
            for c in d.split('.')[::-1]:
                k = c+k
                domain[k] += v
                k = '.'+k
        return [str(v)+' '+k for k, v in domain.items()]