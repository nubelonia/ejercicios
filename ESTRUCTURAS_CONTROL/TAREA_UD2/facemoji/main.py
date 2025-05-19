def run(feeling: str) -> str:
    emojis = {
        'happy': chr(0x1F600),      
        'sad': chr(0x1F614),        
        'angry': chr(0x1F621),      
        'pensive': chr(0x1F914),    
        'surprised': chr(0x1F62E),  
        'rocket': chr(0x1F680)      
    }

    key = feeling.lower()
    emoji = emojis.get(key, None)

    print(f"Sentimiento: {feeling} → Emoji: {emoji}")
    return emoji


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
