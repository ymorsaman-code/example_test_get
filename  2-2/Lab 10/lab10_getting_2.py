import yt_dlp

# ระบุ URL ของวิดีโอที่ต้องการ (รองรับ YouTube, Facebook, และอื่นๆ อีกมากมาย)
url = "https://www.youtube.com/shorts/ydDowjc4yak"

# กำหนดการตั้งค่า (Options) แบบง่ายที่สุด
ydl_opts = {
    'format': 'best',              # เลือกคุณภาพที่ดีที่สุดที่มี
    'outtmpl': '%(title)s.%(ext)s' # ตั้งชื่อไฟล์ตามชื่อคลิปวิดีโอ
}

# สั่งดาวน์โหลด
print(f"Downloading video from: {url}")
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Download completed!")

#--------------------

