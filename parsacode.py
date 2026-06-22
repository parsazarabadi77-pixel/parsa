"""
╔══════════════════════════════════════════╗
║       TERMINAL SHOOTER - main.py         ║
║  نقطه شروع بازی - اینجا بازی اجرا میشه  ║
╚══════════════════════════════════════════╝

برای اجرا:
    python main.py

نیازمندی‌ها:
    - Python 3.8+
    - کتابخانه‌های استاندارد (هیچ نصب اضافه‌ای لازم نیست)
"""

import sys
import os

# اضافه کردن مسیر پروژه به sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.game import Game
from utils.terminal import clear_screen, set_terminal_title


def main():
    """تابع اصلی - بازی را راه‌اندازی می‌کند"""
    set_terminal_title("🔫 Terminal Shooter")
    clear_screen()

    game = Game()
    game.run()


if __name__ == "__main__":
    main()