import asyncio


async def async_result_checker(task):
    while not task.state == 'SUCCESS':
        await asyncio.sleep(1)
        if task.state == 'FAILURE':
            return "FAILED"
    return "DONE"
