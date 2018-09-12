from random import randint
def calculate_crit(player):
    has_crit = False
    dice = randint(0, 100)
    chance = player["Luck"]+player["AGI"]
    if chance > dice:
        has_crit = True

    return has_crit

def combat_round(attacker, defender):
    print(attacker["NAME"], "is beating", defender["NAME"])
    has_crit = calculate_crit(attacker)
    if has_crit:
        print("Đòn chí mạng")
        damage = attacker["STR"]*2 - defender["DEF"]
    else:
        damage = attacker["STR"] - defender["DEF"]
    if damage > 0:
        defender["HP"] -= damage
        print(defender["NAME"], "lost", damage, "HP")
        print(defender)
    else:
        attacker["HP"] -= abs(damage)
        print(attacker["NAME"], "lost", abs(damage), "HP")
        print(attacker)

def combat_full(player, opponent):
    auto_combat = True
    while True:
        combat_round(player, opponent)
        if opponent["HP"] <= 0 or player["HP"] <= 0:
            break
        combat_round(opponent, player)
        if opponent["HP"] <= 0 or player["HP"] <= 0:
            break

        print("Bạn muốn:")
        print("1. Đánh tiếp")
        print("2. Chạy")
        print("3. Tự động đánh")
        option = input(">>>")
        if option == "1":
            pass
        elif option == "2":
            dice = randint(0, 100)
            if player["Luck"] > dice:
                print("Bạn đã chạy thoát")
                break
            else:
                print("Chạy trốn không thành công, bạn quay trở lại cuộc chiến")
        elif option == "3":
            auto_combat = False


# player = {
#     "NAME":"Tokuda",
#     "CLASS":"JAV",
#     "HP": 60,
#     "STR": 7,
#     "DEF": 10,
#     "LVL": 1,
#
# }
# Orc ={
#     "NAME":" Orc",
#     "HP": 7,
#     "STR": 1,
#     "DEF": 2,
#
# }
#
#
# while True:
#     combat(player, Orc)
#
#     if Orc["HP"] <= 0 or player["HP"] <= 0:
#         break
#
#     combat(Orc, player)
#     if Orc["HP"] <= 0 or player["HP"] <= 0:
#         break
