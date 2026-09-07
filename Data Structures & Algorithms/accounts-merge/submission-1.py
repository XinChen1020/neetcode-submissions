from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        parents = [i for i in range(len(accounts))]
        rank = [1] * len(accounts)

        def find(u):
            if parents[u] != u:
                parents[u] = find(parents[u])
            return parents[u]

        def union(u, v):
            u_p = find(u)
            v_p = find(v)

            if u_p == v_p:
                return

            if rank[u_p] > rank[v_p]:
                parents[v_p] = u_p

            elif rank[u_p] < rank[v_p]:
                parents[u_p] = v_p

            else:
                parents[u_p] = v_p
                rank[v_p] += 1

        # email -> first account index where email appeared
        first_seen = {}

        for i in range(len(accounts)):
            for email in accounts[i][1:]:
                if email not in first_seen:
                    first_seen[email] = i
                else:
                    union(first_seen[email], i)

        # root account -> all emails belonging to component
        account_emails = defaultdict(list)

        for email, i in first_seen.items():
            account_emails[find(i)].append(email)

        res = []

        for root, emails in account_emails.items():
            name = accounts[root][0]
            res.append([name] + sorted(emails))

        return res