import httpx
import asyncio

URL = "https://jsonplaceholder.typicode.com"


# # GET request
# response = httpx.get(f"{BASE_URL}/posts/1")
# data=response.json()
# print(data["title"])
# # print("Status code:", response.status_code)
# # print("Response body:")
# # print(response.json())


# # POST request
payload = {
    "title": "Learning Python",
    "body": "Today I learned REST APIs with Python",
    "userId": 1
}

# response = httpx.post(
#     f"{BASE_URL}/posts",
#     json=payload
# )

# # print("\nPOST status code:", response.status_code)
# # print("POST response:")
# print(response.headers)
# print(response.json())


#Async REQ
async def call_api(BASE_URL):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/posts/1")
        data = response.json()
        print(data["title"])
        response2 = await client.post(f"{BASE_URL}/posts",json=payload)
        print(response2.json())

asyncio.run(call_api(URL))

