import asyncio
import server_config
import const
async def handle_client(reader, writer):
    data = await reader.read(const.DATA_DIR)
    print(data)
async def main():
    server = await asyncio.start_server(handle_client, server_config.HOST, server_config.PORT)
    print(f'服务器启动成功，监听端口：{server_config.PORT}')
    async with server:
        await server.serve_forever()


asyncio.run(main())