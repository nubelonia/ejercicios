def run(age: int, weight: int, heartbeat: int, platelets: int) -> bool:
    
    if 18 <= age <= 65 and weight >= 50 and 50 <= heartbeat <= 100 and 150000 <= platelets <= 450000:
        print("El donante es apto para donar sangre")
        return True
    else:
        print("El donante no es apto para donar sangre")
        return False


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
