from datetime import datetime

# Predefined descriptions for Life Path Numbers (1-9 + Master Numbers)
life_path_descriptions = {
    1: "You're a natural leader with strong independence. Future looks bright for new beginnings, entrepreneurship, and achieving big goals. Embrace your originality!",
    2: "You're diplomatic, intuitive, and great at partnerships. Your future holds harmony, meaningful relationships, and success through cooperation.",
    3: "Creative, social, and expressive! Expect joy, artistic opportunities, and fun adventures. Share your optimism with the world.",
    4: "Reliable and hardworking builder. Your future brings stability, strong foundations, and long-term success through discipline.",
    5: "Adventurous freedom-seeker! Big changes, travel, and exciting experiences await. Stay flexible and enjoy the ride.",
    6: "Caring, responsible, and family-oriented. Future highlights love, home, community, and nurturing others.",
    7: "Deep thinker and seeker of truth. Spiritual growth, research, or inner wisdom will guide your successful path.",
    8: "Ambitious and powerful! Wealth, achievement, and leadership in business or career are in your stars.",
    9: "Compassionate humanitarian. Your future involves giving back, global impact, and completing important life cycles.",
    11: "Master Intuitive! Highly spiritual and inspirational. Your path involves enlightenment, innovation, and guiding others.",
    22: "Master Builder! You have huge potential to create lasting impact on the world through big projects and vision."
}

# Zodiac signs with date ranges and fun future vibes
zodiac_data = {
    "Aries": {"dates": ((3, 21), (4, 19)), "vibe": "Bold and energetic! Your future is full of action, courage, and pioneering new paths."},
    "Taurus": {"dates": ((4, 20), (5, 20)), "vibe": "Steady and sensual. Expect growth in comfort, finances, and building lasting value."},
    "Gemini": {"dates": ((5, 21), (6, 20)), "vibe": "Curious and adaptable. Communication, learning, and exciting connections ahead!"},
    "Cancer": {"dates": ((6, 21), (7, 22)), "vibe": "Nurturing and intuitive. Home, family, and emotional fulfillment will shine."},
    "Leo": {"dates": ((7, 23), (8, 22)), "vibe": "Charismatic leader! Creativity, recognition, and joyful spotlight moments coming."},
    "Virgo": {"dates": ((8, 23), (9, 22)), "vibe": "Analytical and helpful. Success through skill-building, service, and perfection."},
    "Libra": {"dates": ((9, 23), (10, 22)), "vibe": "Balanced and charming. Relationships, beauty, and harmony will flourish."},
    "Scorpio": {"dates": ((10, 23), (11, 21)), "vibe": "Intense and transformative. Deep growth, passion, and powerful rebirths await."},
    "Sagittarius": {"dates": ((11, 22), (12, 21)), "vibe": "Adventurous philosopher. Travel, learning, and freedom will expand your world."},
    "Capricorn": {"dates": ((12, 22), (1, 19)), "vibe": "Ambitious and disciplined. Career achievements and long-term goals will pay off."},
    "Aquarius": {"dates": ((1, 20), (2, 18)), "vibe": "Innovative and humanitarian. Future brings unique ideas and positive change for many."},
    "Pisces": {"dates": ((2, 19), (3, 20)), "vibe": "Dreamy and compassionate. Creativity, intuition, and spiritual connections will guide you."}
}

def calculate_life_path(dob):
    """Calculate Life Path Number from YYYY-MM-DD"""
    try:
        date = datetime.strptime(dob, "%Y-%m-%d")
    except ValueError:
        return None, "Invalid date format! Use YYYY-MM-DD (e.g., 1995-07-15)"
    
    year = date.year
    month = date.month
    day = date.day
    
    # Sum all digits
    total = 0
    for num in [year, month, day]:
        while num > 0:
            total += num % 10
            num //= 10
    
    # Reduce to single digit or master number (11, 22, 33)
    while total > 9 and total not in [11, 22, 33]:
        temp = 0
        while total > 0:
            temp += total % 10
            total //= 10
        total = temp
    
    return total, life_path_descriptions.get(total, "A unique path awaits you!")

def get_zodiac(dob):
    """Get zodiac sign from date"""
    try:
        date = datetime.strptime(dob, "%Y-%m-%d")
    except ValueError:
        return None, None
    
    month, day = date.month, date.day
    
    for sign, data in zodiac_data.items():
        (start_m, start_d), (end_m, end_d) = data["dates"]
        if (month == start_m and day >= start_d) or (month == end_m and day <= end_d) or \
           (start_m < end_m and start_m <= month <= end_m) or \
           (start_m > end_m and (month >= start_m or month <= end_m)):
            return sign, data["vibe"]
    return None, None

# === Main App ===
print("🌟 Welcome to Your Personal Future Teller App 🌟")
print("Enter your date of birth (YYYY-MM-DD)")

dob = input("→ ").strip()

life_path_num, life_path_msg = calculate_life_path(dob)
zodiac_sign, zodiac_vibe = get_zodiac(dob)

if life_path_num is None or zodiac_sign is None:
    print("Oops! Please check your date format.")
else:
    print("\n" + "="*50)
    print(f"📅 Your Birth Date: {dob}")
    print(f"♾️  Life Path Number: {life_path_num}")
    print(f"🌌 Zodiac Sign: {zodiac_sign}")
    print("="*50)
    print("\n🔮 Your Future Insight:")
    print(f"→ Based on your Life Path: {life_path_msg}")
    print(f"→ Based on your Zodiac: {zodiac_vibe}")
    print("\nRemember: The future is shaped by your choices! Make it awesome. ✨")
