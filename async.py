import asyncio
import time
import aioping
import httpx


async def download_photos(num_photos, init_url):
    async with httpx.AsyncClient() as client:
        tasks = [download_photo(client, init_url) for _ in range(num_photos)]
        return await asyncio.gather(*tasks)


async def download_photo(client, init_url):
    try:
        response = await client.get(init_url, follow_redirects=True)
        response.raise_for_status()
        final_url = response.url
        return final_url
    except Exception as e:
        return f"Error downloading photo: {str(e)}"


async def ping(host):
    try:
        delay = await aioping.ping(host)
        return f"Ping to {host} successful, delay: {delay:.2f} ms"
    except Exception as e:
        return f"Ping to {host} failed: {str(e)}"


async def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


async def stop_event_loop(loop, seconds):
    print(f"Stopping event loop in {seconds} seconds")
    await asyncio.sleep(seconds)
    # loop.stop()
    print("Event loop stopped")


async def main():
    init_url = "https://picsum.photos/400/600"
    host = "www.youtube.com"
    num_pings = 5
    num_photos = 10
    # factorial_number = 10

    async with httpx.AsyncClient() as client:

        event_loop = asyncio.get_event_loop()
        shielded_stop = asyncio.shield(stop_event_loop(event_loop, 10))

        print("Start download photo")
        base_url_response = await client.get(init_url)
        base_url = base_url_response.url

        print("Start factorial")
        factorial_tasks = [asyncio.create_task(factorial(n)) for n in range(20)]

        print("Start ping tasks")
        ping_tasks = [asyncio.create_task(ping(host)) for _ in range(num_pings)]

        urls = await download_photos(num_photos, base_url)
        for url in urls[:5]:
            print(f'Photo link: {url}')

        results = await asyncio.gather(*ping_tasks, *factorial_tasks)
        for result in results:
            print(result)

        await shielded_stop


if __name__ == "__main__":
    print(f"Execution Started at {time.strftime('%X')}")
    asyncio.run(main())
    print(f"Execution Completed at {time.strftime('%X')}")
