import asyncio
from ruuvi_gateway_client import gateway
from ruuvi_gateway_client.types import ParsedDatas

STATION_IP = "10.0.0.21"
# Set either USERNAME and PASSWORD, or TOKEN
# Here is docs how to configure access settings from LAN using username/password or token:
# https://docs.ruuvi.com/ruuvi-gateway-firmware/gateway-html-pages/access-settings-from-lan
# Here is example how to configure polling mode using token access:
# https://docs.ruuvi.com/ruuvi-gateway-firmware/examples/polling-mode
USERNAME = "username"
PASSWORD = "password"
TOKEN = "bXRhN6p8bhedOSRayTlfOo7PAxMobAy9H9vRHtbjMww="


def print_data(data: ParsedDatas):
    for mac, sensor_data in data.items():
        print(f'{mac}: {sensor_data}')


async def main():
    if USERNAME is not None and PASSWORD is not None:
        fetch_result = await gateway.fetch_data(STATION_IP, USERNAME, PASSWORD)
        if fetch_result.is_ok():
            print_data(fetch_result.ok_value)
        else:
            print(f'Fetch with username/password failed: {fetch_result.err_value}')
    if TOKEN is not None:
        fetch_result = await gateway.fetch_data_with_token(STATION_IP, TOKEN)
        if fetch_result.is_ok():
            print_data(fetch_result.ok_value)
        else:
            print(f'Fetch with token failed: {fetch_result.err_value}')

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
