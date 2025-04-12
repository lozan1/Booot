from telegram import Update, Video
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from collections import defaultdict

TOKEN = "7445462452:AAEAIilss5VMEmKYoF1rtlZ7QdyADqwsmro"
GROUP_ID = -1001951482804

video_stats = defaultdict(lambda: {"views": 0})

async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != GROUP_ID:
        return
    
    video: Video = update.message.video
    file_id = video.file_id
    
    video_stats[file_id]["views"] += 1
    views = video_stats[file_id]["views"]
    
    await update.message.reply_text(
        f"تمت مشاهدة هذا الفيديو {views} مرة داخل المجموعة.",
        reply_to_message_id=update.message.message_id
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.VIDEO, handle_video))
    app.run_polling()

if __name__ == "__main__":
    main()
