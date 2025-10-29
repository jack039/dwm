graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['A']
}

damping_factor = 0.85
num_iterations = 100
num_nodes = len(graph)
page_rank = dict.fromkeys(graph.keys(), 1 / num_nodes)

for i in range(num_iterations):
    new_rank = dict.fromkeys(graph.keys(), (1 - damping_factor) / num_nodes)
    for page in graph:
        outgoing_links = len(graph[page])
        for link in graph[page]:
            new_rank[link] += damping_factor * (page_rank[page] / outgoing_links)
    page_rank = new_rank

print("\nFinal PageRank Values:\n")
for page, rank in page_rank.items():
    print(f"{page}: {round(rank, 4)}")
max_page = max(page_rank, key=page_rank.get)
print("\nHighest Ranked Page:")
print(f"{max_page} with PageRank = {round(page_rank[max_page], 4)}")
'''
The PageRank Algorithm is a link analysis algorithm used by search engines (originally by Google) to rank web pages in search results.
It measures the importance of each page based on the number and quality of links pointing to it.

The basic idea is that a page is important if it is linked to by other important pages.'''