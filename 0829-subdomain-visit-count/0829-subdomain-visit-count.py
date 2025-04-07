class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        subdomain_visit = dict()
        result = []
      
        for data in cpdomains:
            data_split = data.split(" ")
            count = int(data_split[0])
            domain_parts = data_split[1].split('.')

            # Update subdomain visit counts for all levels
            for i in range(len(domain_parts)):
                subdomain = '.'.join(domain_parts[i:])
                subdomain_visit[subdomain] = subdomain_visit.get(subdomain, 0) + count

        # Combine results
        for chars, count in subdomain_visit.items():
            result.append(str(count) + " " + chars)

        return result
        