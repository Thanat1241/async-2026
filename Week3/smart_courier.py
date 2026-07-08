# Delivery System): นักศึกษาต้องเขียน try...except CancelledError ได้ถูกต้อง 
# และใช้ .get_name(), .cancel(), และ .cancelled() ได้

import asyncio
from time import ctime

async def courier_delivery(package_id):

    print(f"{ctime()} Courier started delivering {package_id}...")
    try:
        await asyncio.sleep(10)  # จำลองงานส่งของที่ใช้เวลานานมาก
        return f"{package_id} delivered!"
    except asyncio.CancelledError:
        # Injected exactly at the current await checkpoint when .cancel() is called
        print(f"{ctime()} Delivery Canceled! Returning package to warehouse.")
        raise  # Re-raise the exception to propagate cancellation
 
        

async def main():

    task = asyncio.create_task(courier_delivery("P001"), name="Express-Courier")
 
    # ให้ไรเดอร์ทำงานไปก่อน 2 วิ แล้วมาเช็คสถานะ
    await asyncio.sleep(2)
    print(f"{ctime()} Checking task '{task.get_name()}'. Is it done? {task.done()}")
 
    # ตัดสินใจว่าใช้เวลานานเกินไป สั่งยกเลิก
    print(f"{ctime()} Taking too long! Canceling the task...")
    task.cancel()
 
    try:
        await task  # รอให้ CancelledError วิ่งผ่านและ task จบสถานะจริง ๆ
    except asyncio.CancelledError:
        pass
 
    print(f"{ctime()} Final verify: Is task officially canceled? {task.cancelled()}")
 


if __name__ == "__main__":
    asyncio.run(main())