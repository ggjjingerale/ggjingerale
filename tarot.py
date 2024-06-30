import random
# 定义所有的塔罗牌
tarot_deck = [
    "愚者", "魔术师", "女祭司", "皇后", "皇帝", "教皇", "恋人", "战车", "力量", "隐士",
    "命运之轮", "正义", "倒吊人", "死神", "节制", "恶魔", "塔", "星星", "月亮", "太阳",
    "审判", "世界", "权杖国王", "权杖王后", "权杖骑士", "权杖随从", "权杖十", "权杖九", "权杖八",
    "权杖七", "权杖六", "权杖五", "权仗四", "权杖三", "权杖二", "权杖ACE", "星币国王",
    "星币王后", "星币骑士", "星币随从", "星币十", "星币九", "星币八", "星币七", "星币六", "星币五", "星币四", "星币三", "星币二", "星币ACE"
    "圣杯国王", "圣杯王后", "圣杯骑士", "圣杯随从", "圣杯十", "圣杯九", "圣杯八", "圣杯七", "圣杯六", "圣杯五", "圣杯四", "圣杯三", "圣杯二", "圣杯ACE"
    "宝剑国王", "宝剑王后", "宝剑骑士", "宝剑随从", "宝剑十", "宝剑九", "宝剑八", "宝剑七", "宝剑六", "宝剑五", "宝剑四", "宝剑三", "宝剑二", "宝剑ACE"
]
 
tarot_abbr = ["yz","msh","njs","hh","hd","jh","lr","zc","ll","ys",
        "myzl","zy","ddr","ss","jz","em","t","xx","yl","ty",
       "sp","sj","qzgw","qzwh","qzqs","qzsc","qz10","qz9","qz8",
        "qz7","qz6","qz5","qz4","qz3","qz2","qz1","xbgw",
        "xbwh","xbqs","xbsc","xb10","xb9","xb8","xb7","xb6","xb5","xb4","xb3","xb2","xb1",
        "sbgw","sbwh","sbqs","sbsc","sb10","sb9","sb7","sb8","sb6","sb5","sb4","sb3","sb2","sb1",
       "bjgw","bjwh","bjqs","bjsc","bj10","bj9","bj7","bj8","bj6","bj5","bj4","bj3","bj2","bj1"]

pos = ["正位","逆位"]

pos_abbr = ["z","n"]

def draw_tarot_card():
    """从塔罗牌堆中随机抽取一张牌"""
    return random.choice(tarot_deck)
 
def main():
    """主程序"""
    print("欢迎使用塔罗占卜工具！")
    while True:
        input("请输入你的问题：") #并按下Enter键进行抽牌..
        card = draw_tarot_card()
        tarot_idx = tarot_deck.index(card) # 找到对应缩写
        card_pos = random.choice(pos)
        pos_idx = pos.index(card_pos)
        print("你抽到的塔罗牌是：", card, random.choice(pos))
        if tarot_abbr[tarot_idx][0:2]=="bj":
            str = "https://w.taluo.com/bj/"+ tarot_abbr[tarot_idx] + pos_abbr[1] + ".php"
        elif tarot_abbr[tarot_idx][0:2]=="sb":
            str = "https://w.taluo.com/sb/"+ tarot_abbr[tarot_idx] + pos_abbr[1] + ".php"
        elif tarot_abbr[tarot_idx][0:2]=="xb":
            str = "https://w.taluo.com/xb/"+ tarot_abbr[tarot_idx] + pos_abbr[1] + ".php"
        elif tarot_abbr[tarot_idx][0:2]=="qz":
            str = "https://w.taluo.com/qz/"+ tarot_abbr[tarot_idx] + pos_abbr[1] + ".php"
        else:
            str = "https://w.taluo.com/da/"+ tarot_abbr[tarot_idx] + pos_abbr[1] + ".php"
        print("详情请见：", str)
        cont = input("是否继续抽牌？(yes/no): ")
        if cont.lower() != "yes":
            print("再见！")
            break
            
 
if __name__ == "__main__":
    main()
    
