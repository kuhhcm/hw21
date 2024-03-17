import requests
import time

url = "https://jsonplaceholder.typicode.com/posts/"

# # Задание 1
# def load_urls(url):
#     response = requests.get(url)
#     return response.json()




# # Задание 2
# def load_urls(url, file_name):
#     response = requests.get(url)
#     with open(file_name, "w") as file:
#         file.write(response.text)

# start = time.time()
# for i in range(1, 10):
#     load_urls(url, f"post{i}.json")
# end = time.time()
# print("Время выполнения: ", end - start)






# # Задание 3
# import asyncio
# import requests
# import time

# async def fetch_url(url, file_name):
#     response = requests.get(url)
#     with open(file_name, "w") as file:
#         file.write(response.text)

# async def urls(url, total):
#     tasks = []
#     for i in range(1, total + 1):
#         file_name = f"post{i}.json"
#         task = asyncio.create_task(fetch_url(url, file_name))
#         tasks.append(task)
#     await asyncio.gather(*tasks)

# async def main():
#     url = "https://jsonplaceholder.typicode.com/posts"
#     start = time.time()
#     await urls(url, 100)
#     end = time.time()
#     print("Время выполнения: ", end - start)

# asyncio.run(main())





