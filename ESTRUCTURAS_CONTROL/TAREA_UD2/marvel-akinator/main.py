def run(can_fly: bool, is_human: bool, has_mask: bool) -> str:
    if can_fly:
        if is_human:
            if has_mask:
                hero = "Ironman"
            else:
                hero = "Captain Marvel"
        else:
            if has_mask:
                hero = "Ronan Accuser"
            else:
                hero = "Vision"
    else:
        if is_human:
            if has_mask:
                hero = "Spiderman"
            else:
                hero = "Hulk"
        else:
            if has_mask:
                hero = "Black Bolt"
            else:
                hero = "Thanos"

    print(f"El personaje de Marvel es: {hero}")
    return hero



# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
