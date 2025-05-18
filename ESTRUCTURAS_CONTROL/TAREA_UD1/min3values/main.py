def run(value1: int | float, value2: int | float, value3: int | float) -> int | float:
    print("Ejecutando función con:", value1, value2, value3)

    result = min(value1, value2, value3)
    print("El valor mínimo es:", result)
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
