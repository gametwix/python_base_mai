def get_drone_list_by_vendor(vendor, drones_names):
    vendor = vendor.lower()
    res = list()
    for drone in drones_names:
        words = drone.split()
        if words[0].lower() == vendor:
            if vendor == "dji":
                words[0] = words[0].upper()
            else:
                words[0] = words[0].title()
            res.append(" ".join(words))
    return res


def count_vendor_drones(drones_names):
    res = dict()
    for drone in drones_names:
        vendor = drone.split()[0].lower()
        if res.get(vendor) is None:
            res[vendor] = 1
        else:
            res[vendor] += 1
    return res


def count_number_two(drones_names):
    res = 0
    for drone in drones_names:
        if "2" in drone or "II" in drone:
            res += 1
    return res


def split_drones_by_register(drones_names, drones_weights):
    need_register = list()
    not_need_register = list()
    for drone, weight in zip(drones_names, drones_weights):
        if weight > 150:
            need_register.append(drone)
        else:
            not_need_register.append(drone)
    return (need_register, not_need_register)


def need_agree_for_fly(weight, height, close_zone, in_city, direct_visibility):
    return (
        not direct_visibility
        or close_zone
        or height > 150
        or (in_city and weight >= 150)
    )


if __name__ == "__main__":
    drone_list = [
        "DJI Mavic 2 Pro",
        "DJI Mavic 2 Zoom",
        "DJI Mavic 2 Enterprise Advanced",
        "AUTEL Evo II Pro",
        "DJI Mini 2",
        "Autel Evo Nano",
        "Autel Evo Lite Plus",
        "Parrot Anafi",
        "Dji Inspire 2",
        "DJI Mavic 3",
        "DJI Mavic Air2s",
        "Ryze Tello",
        "Eachine Trashcan",
    ]

    drone_weight_list = [
        903,
        900,
        920,
        980,
        249,
        249,
        600,
        540,
        1500,
        1000,
        570,
        130,
        110,
    ]

    # TODO1
    # выведите все дроны производителя, название которого введет пользователь через input, и подсчитайте их количество.
    # учтите, что:
    # 1) DJI и Dji - это один и тот же производитель! такие случаи тоже должны обрабатываться
    # 2) при выводе исправьте название производителя, если допущена ошибка. как правильно писать производителей: DJI, Autel

    vendor = input("Enter vendor name: ")
    vendor_drones = get_drone_list_by_vendor(vendor, drone_list)
    print(f"Vendor have {len(vendor_drones)} drones:")

    for drone in vendor_drones:
        print(drone)

    print("\n")

    # TODO2
    # 1) подсчитайте количество моделей дронов каждого производителя из списка drone_list. производители: DJI, Autel, Parrot, Ryze, Eachine
    # 2) подсчитайте количество моделей дронов второй версии (содержащих в названии "2" или "II") - ответ 7

    print("Count drones by vendor:")

    count_vendors = count_vendor_drones(drone_list)
    for vendor, count in count_vendors.items():
        if vendor == "dji":
            print(f"{vendor.upper()}\t{count}")
        else:
            print(f"{vendor.title()}\t{count}")

    print(f"Drones with number two: {count_number_two(drone_list)}\n")

    # TODO3
    # выведите все дроны из списка, которые нужно регистрировать, и подсчитайте их количество.
    # напоминание: регистрировать нужно все дроны массой более 150 г
    # сделайте то же самое для всех дронов, которые не нужно регистрировать
    # для этого вам нужно параллельно обрабатывать два списка: drone_list и drone_weight_list:
    # как работает zip, мы разберем на лекции про списки. пока что просто пользуйтесь (в drone будет модель, в weight - ее вес)

    need_reg, not_need_reg = split_drones_by_register(drone_list, drone_weight_list)

    print(f"{len(need_reg)} drones need to be registered:")
    for drone in need_reg:
        print(drone)

    print(f"\nNo need to be registered {len(not_need_reg)} drones:")
    for drone in not_need_reg:
        print(drone)

    # TODO4
    # для каждого дрона из списка выведите, нужно ли согласовывать полет при следующих условиях:
    # высота 155 м, полет вне населенного пункта, вне закрытых зон, в прямой видимости
    # помните, что для дронов тяжелее 150 г согласовывать полет над населенным пунктом - обязательно!

    print("\nNeed or no need agree for fly drones: ")
    for drone, weight in zip(drone_list, drone_weight_list):
        need = need_agree_for_fly(weight, 155, False, False, True)
        if need:
            print(f"{drone} - need")
        else:
            print(f"{drone} - no need")

    # TODO5
    # модифицируйте решение задания TODO1:
    # теперь для введенного пользователем производителя вы должны вывести строку, содержащую перечисление моделей и БЕЗ названия производителя.
    # например, пользователь ввел "Autel". ваша программа должна вывести вот такой результат: "Evo II Pro, Evo Nano, Evo Lite Plus". для этого вам понадобится несколько функций работы со строками. решить эту задачу можно несколькими разными способами
    # производители те же: DJI, Autel, Parrot, Ryze, Eachine

    vendor = input("\nEnter vendor name: ")
    vendor_drones = get_drone_list_by_vendor(vendor, drone_list)
    models = [" ".join(drone.split()[1:]) for drone in vendor_drones]
    print(*models, sep=", ")
