# Напишите однострочный генератор словаря, который
# принимает на вход три списка одинаковой длины: имена str,
# ставка int, премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа
# и суммой премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии

names = ("Олег", "Алексей", "Ольга", "Ева")

bet = (2, 5, 6, 8)

percent = ("10.25%", "12.50%", "0.5%", "2.0%")


def get_dictcomp(names:list[str], bet:list[int],percent:list[str]) -> dict[str:int]:
    return {names: round(bet+(bet/100*float(percent)), 2) for names, bet, percent in
            zip(names, bet, map(lambda x: x[:-1], percent))}

print(get_dictcomp(names,bet, percent))