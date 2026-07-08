# Delivery System): นักศึกษาต้องเขียน try...except CancelledError ได้ถูกต้อง 
# และใช้ .get_name(), .cancel(), และ .cancelled() ได้

import asyncio
from time import ctime


# 1: Coroutine จำลองการส่งพัสดุ
async def delivery_task(package_id, duration):
    try:
        print(f"{ctime()} Courier started delivering {package_id}...")
        await asyncio.sleep(duration)  # จำลองเวลาเดินทางส่งของ
        return f"Package {package_id} Delivered!"
    except asyncio.CancelledError:
        # ถูก inject เมื่อ main สั่ง .cancel() ที่จุด await
        print(f"{ctime()} Delivery Canceled! Returning package to warehouse.")
        raise  # re-raise เพื่อให้สถานะ task เป็น cancelled จริง


async def main():
    # 2: สร้าง Task ชื่อ "Express-Courier" (P001, 5 วินาที)
    task = asyncio.create_task(
        delivery_task(package_id="P001", duration=5.0),
        name="Express-Courier"
    )

    # 3: ผ่านไป 2 วินาที ตรวจสอบสถานะด้วย .done() และพิมพ์ชื่อด้วย .get_name()
    await asyncio.sleep(2.0)
    print(f"{ctime()} Checking task '{task.get_name()}'. Is it done? {task.done()}")

    # 4: ยังไม่เสร็จ -> ยกเลิกทันทีด้วย .cancel()
    if not task.done():
        print(f"{ctime()} Taking too long! Canceling the task...")
        task.cancel()

    # เปิดช่องให้ event loop ไปรัน except block ของคูรูทีน
    await asyncio.sleep(0.1)

    # 5: ตรวจสอบจากภายนอกว่า .cancelled() เป็น True
    print(f"{ctime()} Final verify: Is task officially canceled? {task.cancelled()}")


if __name__ == "__main__":
    asyncio.run(main())