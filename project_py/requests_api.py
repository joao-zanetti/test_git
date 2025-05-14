import requests

def fetch_and_transform_data(api_url):
    try:
        # Make a GET request to the API
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad status codes

        # Parse the JSON response
        data = response.json()

        # Transform the data (example: extract specific fields)
        transformed_data = [
            {
                "id": item.get("id"),
                "name": item.get("name"),
                "value": item.get("value")
            }
            for item in data if isinstance(item, dict)
        ]

        return transformed_data

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    api_url = "https://api.example.com/data"
    result = fetch_and_transform_data(api_url)
    if result:
        print("Transformed Data:")
        print(result)



import aiohttp
import asyncio

async def fetch_and_transform_data_async(api_url):
    try:
        # Make an asynchronous GET request to the API
        async with aiohttp.ClientSession() as session:
            async with session.get(api_url) as response:
                response.raise_for_status()  # Raise an error for bad status codes

                # Parse the JSON response
                data = await response.json()

                # Transform the data (example: extract specific fields)
                transformed_data = [
                    {
                        "id": item.get("id"),
                        "name": item.get("name"),
                        "value": item.get("value")
                    }
                    for item in data if isinstance(item, dict)
                ]

                return transformed_data

    except aiohttp.ClientError as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    async def main():
        api_url = "https://api.example.com/data"
        result = await fetch_and_transform_data_async(api_url)
        if result:
            print("Transformed Data:")
            print(result)

    asyncio.run(main())