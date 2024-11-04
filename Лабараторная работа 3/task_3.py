from itertools import count


def count_letters(text):
    count = {}
    for letters in text:
        small_letters = letters.lower()
        if small_letters.isalpha():
            if small_letters in count:
                count[small_letters] += 1
            else:
                count[small_letters] = 1
    return count

def calculate_frequency(count):
    all_count = sum(count.values())
    dict_final = {}
    for symbol, kol_vo in count.items():
        dict_final[symbol] = round(kol_vo / all_count, 2)
    return dict_final

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

count = count_letters(main_str)
dict_final = calculate_frequency(count)

for symbol, numb in dict_final.items():
    print(f"{symbol}: {numb}")