player = {
    "NAME":"Jacky",
    "CLASS":"Human",
    "HP": 100,
    "STR": 10,
    "DEF": 15,
    "LVL": 1,
}
print("Chào mừng đến với game Escape the house")
print("Bạn là jacky, một thanh niên 18+")
print("Một hôm, sau khi đi mây mưa với bạn, bạn đang trên đường về gặp 1 thanh niên nhìn chằm chằm vào bạn")
print("Bạn chưa kịp làm gì thì đã bị thanh niên đó HIẾP DÂM ")
print("Bạn kêu to lên 1 tiếng xong ngất")
print("Khi bạn tỉnh dậy bạn thấy mình bị đưa vào một căn nhà hoang")
print("Nhiệm vụ của bạn là giải đố các câu hỏi và đánh bại thanh niên đấy")
print("Đây là game giải đố nên người chơi ko nên xem code")
print("Ai win game trong 15 phút sẽ bị thanh niên kia hiếp dâm. CÁC BẠN ĐÃ HIỂU CHƯA!!!!!")

cmd = input("Bạn muốn xem bạn còn bao nhiêu HP thì bạn bấm stats!")
if cmd == "stats":
    print("NAME:", player["NAME"])
    print("CLASS:", player["CLASS"])
    print("HP:", player["HP"])
    print("STRENGHT:", player["STR"])
    print("DEFENSE:", player["DEF"])
    print("LEVEL:", player["LVL"])

print("Bạn nhìn thấy một cánh cửa")
print("Bạn có 2 lựa chọn")
print("1. Không mở")
print("2. Mở cửa")
option = input("Lựa chọn của bạn?")
if option == "1":
    print("Bạn không mở cửa là 1 SAI LẦM LỚN")
    print("Bạn sẽ chọn lại chứ?")
elif option == "2":
    print("Bạn đi vào căn phòng thứ 2")
    print("Bạn nhìn thấy một tờ giấy, trong đấy ghi:")
    print("Mày đang bị tao giam giữ ở 1 nơi hoang vắng. Nếu mày muốn sống sót thì hãy trả lời câu hỏi này của tao rồi mày sẽ thoát")
    print("Câu hỏi của tao là:")
    print("Cái gì trên lông dưới lông, tối hòa làm một?")
    Q1 = input("Câu trả lời của bạn:")
    if Q1 == "Đôi mắt":
        print("Bạn đã đúng")
        print("Bạn đã vượt qua phòng 2")
        print("Bạn được tặng một chìa khóa mở cửa và một con dao")
        print("Xin chúc mừng ")
        print("Lúc này bạn nghe thấy tiếng của một thanh niên")
        print("Mày được lắm, đã vượt qua được phòng 2 à")
        print("Mày hãy giải câu hỏi tiếp theo của tao:")
        print("Chấm chấm mút mút, đút vào lỗ trôn. Hai sợi lông ***, cái dài cái ngắn")
        Q2 = input("Câu trả lời của bạn:")
        if Q2 == ("Xâu kim"):
            print("Bạn đã đúng")
            print("Bạn đã vượt qua phòng 3")
            print("Bạn nhặt được chìa khóa dẫn tới phòng 4")
            print("Bạn đi tới phòng tiếp theo")
            print("Ở đó có một con chó to lớn, hung dữ")
            print("Bên cạnh đó có cánh cửa")
            print("Bạn có 3 lựa chọn")
            print("1. Chạy về phòng cũ đóng cửa")
            print("2. Chạy tới cái cửa và mở chạy thoát")
            print("3.  Đánh nhau với con chó")
            cmd = input("Lựa chọn của bạn?")
            if cmd == "1":
                print("Bạn bị NGU à. Bạn sẽ chọn lại chứ?")
            elif cmd =="2":
                print("Bạn bị con chó đợp chết. Bạn sẽ chọn lại chứ?")
            elif cmd == "3":
                Dog = {
                    "NAME":"DOG",
                    "CLASS":"DOG",
                    "HP":13,
                    "STR":25,
                    "DEF":2,
                    "LVL":1,
                }
                print("NAME:", Dog["NAME"])
                print("CLASS:", Dog["CLASS"])
                print("HP:", Dog["HP"])
                print("STRENGHT:", Dog["STR"])
                print("DEFENSE:", Dog["DEF"])
                print("LEVEL:", Dog["LVL"])

                print("Bạn được đánh trước")
                damage = player["STR"] - Dog["DEF"]
                if damage > 0:
                    Dog["HP"] -= damage
                    print("Con chó vừa mất", damage, "HP")
                    print("Con chó còn", Dog["HP"], "HP")

                print("Lượt con chó")
                damage = Dog["STR"] - player["DEF"]
                if damage > 0:
                    player["HP"] -= damage
                    print("Bạn vừa mất", damage, "HP")
                    print("Bạn còn", player["HP"], "HP")
                else:
                    print("Bạn không bị làm sao")

                print("Đến lượt bạn")
                damage = player["STR"] - Dog["DEF"]
                if damage > 0:
                    Dog["HP"] -= damage
                    print("Con chó vừa mất", damage, "HP")
                    print("Con chó còn", 0, "HP")
                    print("Bạn đã tiêu diệt được con chó")
                    print("Xin chúc mừng bạn được thăng cấp và được hồi lại máu")

                    player["HP"] = 120
                    player["STR"]= 20
                    player["DEF"] = 25
                    player["LVL"] = 2
                    print("HP:", player["HP"])
                    print("STRENGHT:", player["STR"])
                    print("DEFENSE:", player["DEF"])
                    print("LEVEL:", player["LVL"])

                print("Bạn đi tiếp vào căn phòng thứ 5")
                print("Ở đó được chia làm ba phòng")
                print("Bên ngoài cửa có ghi")
                print("Phòng 1: có lửa cháy dữ dội")
                print("phòng 2: chứa toàn khí độc")
                print("Phòng 3: Có một bầy hổ nhịn đói 2 năm")
                Q3 = input("Lựa chọn của bạn")
                if Q3 == "1":
                    print("Bạn đã bị chết cháy. Thật đáng tiếc!!!")
                elif Q3 == "2":
                    print("Bạn đã chết sau 1 giây hít phải khí độc. Bạn sẽ chọn lại chứ?")
                elif Q3 == "3":
                    print("Bạn đã vượt qua được phòng thứ 5")
                    print("Tại căn phòng này vì câu hỏi quá dễ nên không được thưởng!!!")
                    print("Bạn bước vào căn phòng tiếp theo")
                    print("Nơi đó có ghi chữ exit")
                    print("Nhưng trước mặt bạn xuất hiện một người thanh niên có một bộ óc to, đeo kính nhìn giống hệt giáo sư tiến sĩ ")
                    print("Anh ta nói:")
                    print("Mày thật may mắn khi đã đến được căn phòng cuối cùng. Nếu muốn thoát ra khỏi đây hãy đánh bại ta đã")
                    print("Bạn sẽ đánh bại được hắn bằng cách trả lời những câu hỏi sau")
                    print("Nếu muốn thoát nhanh hãy chọn Very hard")
                    print("1. Hard")
                    print("2. Very hard")
                    option = input("Lựa chọn của bạn?")
                    if option == "1":
                        print("Đố mày khi cầu thủ thực hiện quả đá phạt đền, anh ta sẽ sút vào đâu?")
                        Q4 = input("Câu trả lời của bạn:")
                        if Q4 == "Quả bóng":
                            print("Xin chúc mừng bạn đã giải được câu hỏi ")
                            print("Phần thưởng của bạn là một câu hỏi thú vị nữa")
                            print("Đây là câu hỏi ngoài lề nên không quan tâm gì đến trò chơi")
                            print("Cầm trên tay một cây thước và một cây bút , làm thế nào để bạn vẽ được một vòng tròn thật chính xác?")
                            Q5 = input("Câu trả lời của bạn:")
                            if Q5 == "Cầm compa lên vẽ":
                                print("Chúc mừng bạn đã win game")
                                print("Bạn đã thoát nhưng thanh niên kia đã chạy trốn")
                                print("To be continue!!")
                            else:
                                print("Bạn không giải được nhưng vẫn win game")
                                print("Bạn đã thoát nhưng thanh niên kia đã chạy trốn")
                                print("To be continue!!")
                        else:
                            print("Ha ha ha mày thua rồi con ạ!!")
                            print("GAME OVER")
                    elif option == "2":
                        print("Đố mày biết A gọi B bằng bác, B gọi C là ông nội , C kêu D là cậu, D kêu E là dì, E kêu F là chú, F gọi Z là con.Vậy A gọi Z bằng gì?")
                        Q6 = input("Câu trả lời của bạn:")
                        if Q6 == ("Mồm"):
                            print("Xin chúc mừng bạn đã giải được câu hỏi")
                            print("Đây là câu hỏi cuối cùng nên bạn đã win game")
                            print("Bạn đã thoát nhưng thanh niên kia đã chạy trốn")
                            print("To be continue!!")
                        else:
                            print("GAME OVER")
        else:
            print("Mày còn non lắm con ạ. HA HA HA HA !!!")
            print("GAME OVER")

    else:
        print("Ha ha mày đã sai. Mày đã thuộc về tao!!!")
        print("GAME OVER!!")






