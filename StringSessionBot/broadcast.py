from pyrogram import Client, filters
from StringSessionBot.database.broadcast_db import Users  # Ganti sesuai struktur project lo
from StringSessionBot.database import SESSION
import asyncio

OWNER_ID = 1234567890  # Ganti dengan ID Telegram lo

@Client.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
async def broadcast(client, message):
    if len(message.command) < 2:
        return await message.reply("❌ Contoh: /broadcast Halo semua!")

    text = message.text.split(None, 1)[1]
    sukses, gagal = 0, 0

    try:
        users = SESSION.query(Users).all()
    except Exception as e:
        SESSION.close()
        return await message.reply(f"⚠️ Gagal ambil user dari database:\n`{e}`")

    await message.reply(f"🔁 Mulai broadcast ke {len(users)} user...")

    for user in users:
        try:
            await client.send_message(user.user_id, text)
            sukses += 1
        except Exception:
            gagal += 1
        await asyncio.sleep(0.1)  # delay 100ms untuk hindari rate limit

    SESSION.close()

    await message.reply(
        f"📢 Broadcast selesai!\n\n"
        f"👥 Total user: {len(users)}\n"
        f"✅ Terkirim: {sukses}\n"
        f"❌ Gagal: {gagal}"
    )
