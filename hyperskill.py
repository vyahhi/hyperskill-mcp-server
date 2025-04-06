import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Hyperskill")

@mcp.tool()
async def get_topic(id: str) -> str:
    """Get topic by id"""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://hyperskill.org/api/topics/{id}")
        if response.status_code == 200:
            return response.text
        else:
            return f"Error fetching topic {id}: {response.status_code}"

# FIXME: requires auth to search
# @mcp.tool()
# async def get_topics(query: str) -> str:
#     """Search for topics on Hyperskill and return the results with URLs"""
#     async with httpx.AsyncClient() as client:
#         response = await client.get(f"https://hyperskill.org/api/search-results?query={query}")
#         if response.status_code == 200:
#             data = response.json()
#             results = []
            
#             # Check if there are topics in the response
#             if "search-results" in data:
#                 search_results = data["search-results"]
#                 if search_results:
#                     results.append("## Topics Found:")
#                     for search_result in search_results:
#                         if search_result.get("target_type") == "topic":
#                             topic_id = search_result.get("target_id", "")
#                             url = f"https://hyperskill.org/learn/topic/{topic_id}"
#                             response2 = await client.get(url)
#                             if response2.status_code == 200:
#                                 topic = response2.json()["topics"][0]
#                                 title = topic["title"]
#                                 summary = topic["summary"]
#                                 results.append(f"- [{title}]({url}): {summary}")
#                 else:
#                     results.append("No topics found for this query.")
#             else:
#                 results.append("No topics section in the response.")
                
#             return "\n".join(results)
#         else:
#             return f"Error searching for topics with query '{query}': {response.status_code}"

if __name__ == "__main__":
    mcp.run(transport='stdio')