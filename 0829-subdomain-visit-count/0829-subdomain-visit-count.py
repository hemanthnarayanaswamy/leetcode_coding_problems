class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        subdomain_visit = dict()
      
        for data in cpdomains:
            count, domain_parts = data.split(" ")
            count ,domain_parts = int(count), domain_parts.split('.')

            # Update subdomain visit counts for all levels
            for i in range(len(domain_parts)):  ## Iterate through the All different Parts 
                subdomain = '.'.join(domain_parts[i:])             # Join from Start/current to end of domains
                subdomain_visit[subdomain] = subdomain_visit.get(subdomain, 0) + count      # If its exisits get that data and add the current count to update the hashMap

        return [f"{v} {k}" for k, v in subdomain_visit.items()]
            