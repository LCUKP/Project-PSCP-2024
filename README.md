# Project-PSCP-2024
#วิธีการใช้งาน (ไม่ได้ Deploy ขึ้น host)
1. pull code ทั้งโปรเจคลงเครื่องของผู้ใช้
2. เช็คในแน่ใจว่าติดตั้ง python และ Django เรียบร้อยแล้ว หากไม่ติดตั้งจะทำงานไม่ได้
3. เปิดโปรเจคขึ้นมาพร้อมเปิด Terminal หรือ CMD
4. ตรวจให้แน่ใจว่าอยู่ใน path ../Project-PSCP-2024/oursite หากไม่อยู่ใน path นี้ ให้ cd เข้ามาให้ถูกต้อง
5. เรียก python manage.py runserver ถ้าใช้ Mac ให้เรียก python3 manage.py runserver

path ที่ใช้งาน และ รหัสที่ใช้สำหรับ login <br>
http://localhost:port/admin/    user : adminsite / password : 12345 <br>
http://localhost:port/          user : testuser / password : 12345 <br>
http://localhost:port/adminis/  user : admin / password : Admin12345 (ระบบฐานข้อมูลสามารถแก้ไขได้ทุก Models) <br>


