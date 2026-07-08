# นักเรียนต้องเลือกใช้ asyncio.wait() พร้อมออปชัน return_when=asyncio.FIRST_COMPLETED เท่านั้น (หากใครใช้ gather หรือ wait_for จะไม่ตรงสเปกเงื่อนไขการแข่งส่งข้อมูล)
import asyncio
from time import ctime
 
# จำลองข้อมูลราคาหุ้นของแต่ละสาขา พร้อม Latency (ความหน่วง) ที่ต่างกัน
SERVERS = {
    "Alpha": {"delay": 3.0, "price": 152},
    "Beta": {"delay": 0.8, "price": 150},   # เร็วที่สุด!
    "Gamma": {"delay": 1.5, "price": 150},
}
 
 
async def fetch_stock_price(server_name):
    info = SERVERS[server_name]
    await asyncio.sleep(info["delay"])
    return server_name, info["price"]
 
 
async def main():
    # สร้าง task สำหรับดึงราคาจากทุกสาขาพร้อมกัน (racing)
    tasks = {
        asyncio.create_task(fetch_stock_price(name), name=name)
        for name in SERVERS
    }
 
    # หยุดทันทีเมื่อมีสาขาแรกตอบกลับ (FIRST_COMPLETED)
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
 
    winner_task = done.pop()
    name, price = winner_task.result()
    print(f"{ctime()} Winner Result: [{name}] Price: {price} USD")
 
    # ยกเลิก task ที่ยังค้างอยู่ (ผู้แพ้ในการแข่งขัน) ทิ้งทันที
    print(f"{ctime()} Cleaning up {len(pending)} pending tasks...")
    for task in pending:
        task.cancel()
 
    # กันไว้ไม่ให้ CancelledError ของ pending task หลุดออกมาโดยไม่มีใครจัดการ
    await asyncio.gather(*pending, return_exceptions=True)
 
 
if __name__ == "__main__":
    asyncio.run(main())
 