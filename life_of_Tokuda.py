player = {
    "NAME":"Tokuda",
    "CLASS":"JAV",
    "HP": 60,
    "STR": 7,
    "DEF": 10,
    "LVL": 1,

}
cmd = input("Your command?")

if cmd == "stats":
    print("NAME:", player["NAME"])
    print("CLASS:", player["CLASS"])
    print("HP:", player["HP"])
    print("STRENGHT:", player["STR"])
    print("DEFENSE:", player["DEF"])
    print("LEVEL:", player["LVL"])
elif cmd == "here":
    print("Bạn đang ở trước cửa Techkids")
    print("Bạn có 2 lựa chọn")
    print("1. Quay trở về Techkids")
    print("2. Đi vào cánh rừng đối diện")
    option = input("Lựa chọn của bạn?")
    if option == "1":
        print("Xin lỗi, đã hết giờ làm việc")
        print("Nhập lại đê!!")
    elif option == "2":
        print("Bạn đã bước vào rừng")
        print("Bạn thấy một bình thủy dịch ở trên mặt đất")
        print("1. Bỏ qua")
        print("2. Nhặt lên uống")
        option = input("Lựa chọn của bạn?")
        if option == "1":
            print("Tiếc quá")
        elif option == "2":
            player["HP"] = 100
            print ("Bạn đã hồi phục hoàn toàn HP")
            print("NAME:", player["NAME"])
            print("CLASS:", player["CLASS"])
            print("HP:", player["HP"])
            print("STRENGHT:", player["STR"])
            print("DEFENSE:", player["DEF"])
            print("LEVEL:", player["LVL"])
        print("Bạn gặp 1 con Orc chưa trưởng thành")
        print("Bạn sẽ:")
        print("1. Chạy trốn")
        print("2. Nấp vào hang đá bên cạnh")
        print("3. ĐÁNH!!!")
        option = input("lựa chọn của bạn?")
        if option == "1":
            print("Do bạn chạy quá chậm bạn bị bắt đi")
        elif option == "2":
            print("Orc không nhìn thấy bạn và bỏ đi")
            print("Tuy nhiên khi bạn quay lại nhìn vào hang, bạn thấy 1 đàn sói")

        elif option == "3":
            Orc ={
                "NAME":" Orc",
                "HP": 7,
                "STR": 1,
                "DEF": 2,

            }
            print("OPPONENT:", Orc["NAME"])
            print("HP:", Orc["HP"])
            print("STENGHT:", Orc["STR"])
            print("DEFENSE:", Orc["DEF"])

            print("Bạn được đánh đầu tiên")
            damage = player["STR"]-Orc["DEF"]
            if damage > 0:
                Orc["HP"] -= damage
                print("Orc vừa mất", damage, "HP")
                print("Orc còn ", Orc["HP"], "HP")

            print("Orc đánh bạn")
            damage = Orc["STR"] - player["DEF"]
            if damage > 0:
                player["HP"] -= damage
                print("Player vừa mất ", damage, "HP")
            else:
                print("Bạn không làm sao cả")

            print("Bạn đánh Orc lượt 2")

            damage = player["STR"] - Orc["DEF"]
            if damage > 0:
                Orc["HP"] -= damage
                print("Orc còn ", Orc["HP"], "HP")
            print("Orc đã bị tiêu diệt")
            print("Bạn đã thắng")
            print("Phần thưởng của bạn là một chuyến đi Nhật Bản miễn phí!!")
            print("Xin chúc mừng!!!")
            print("Vì bạn đã được chuyến đi nên trò chơi kết thúc")
            print(" END GAME")
    else:
        print("Bạn sẽ không được chơi!!!")

else:
    print("Bạn đã chết")

