plugboard = []

class EnigmaI:

    entry = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    rolls = [
        "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
        "AJDKSIRUXBLHWTMCQGZNPYFVOE",
        "BDFHJLCPRTXVZNYEIWGAKMUSQO",
        "ESOVPZJAYQUIRHXLNFTGKDCMWB",
        "VZBRGITYUPSDNHLXAWMJQOFECK"
    ]
    turn_over_notches = "YMDRH"
    visible_letters_in_window_at_turnover = "QEVJZ"
    reflectors = [
        "EJMZALYXVBWFCRQUONTSPIKHGD",
        "YRUHQSLDPXNGOKMIEBFZCWVJAT",
        "FVPJIAOYEDRZXWGCTKUQSBNMHL"
    ]

class EnigmaD:
    entry = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rolls = [
        "LPGSZMHAEOQKVXRFYBUTNICJDW",
        "SLVGBTFXJQOHEWIRZYAMKPCNDU",
        "CJGDPSHKTURAWZXFMYNQOBVLIE"
    ]
    turn_over_notches = "GMV"
    visible_letter_in_window_at_turnover = "YEN"
    reflectors = [
        "IMETCGFRAYSQBZXWLHKDVUPOJN"
    ]

class NorwayEnigma:
    entry="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rolls=[
        "WTOKASUYVRBXJHQCPZEFMDINLG",
        "GJLPUBSWEMCTQVHXAOFZDRKYNI",
        "JWFMHNBPUSDYTIXVZGRQLAOEKC",
        "FGZJMVXEPBWSHQTLIUDYKCNRAO",
        "HEJXQOTZBVFDASCILWPGYNMURK"
    ]
    turn_over_notches = "YMDRH"
    visible_letters_in_window_at_turnover = "QEVJZ"
    reflectors = [
        "MOWJYPUXNDSRAIBFVLKZGQCHET"
    ]

class SonderEnigma:
    entry="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rolls=[
        "VEOSIRZUJDQCKGWYPNXAFLTHMB",
        "UEMOATQLSHPKCYFWJZBGVXIDNR",
        "TZHXMBSIPNURJFDKEQVCWGLAOY"
    ]
    turn_over_notches="YMD"
    visible_letters_in_window_at_turnover = "QEV"
    reflectors=["CIAGSNDRBYTPZFULVHEKOQXWJM"]

class EnigmaM3:
    entry="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rolls=[
        "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
        "AJDKSIRUXBLHWTMCQGZNPYFVOE",
        "BDFHJLCPRTXVZNYEIWGAKMUSQO",
        "ESOVPZJAYQUIRHXLNFTGKDCMWB",
        "VZBRGITYUPSDNHLXAWMJQOFECK",
        "JPGVOUMFYQBENHZRDKASXLICTW",
        "NZJHGRCXMYSWBOUFAIVLPEKQDT",
        "FKQHTLXOCBJSPDZRAMEWNIUYGV",
    ]
    turn_over_notches=[
        "Y",
        "M",
        "D",
        "R",
        "H",
        "HU",
        "HU",
        "HU"
    ]
    visible_letters_in_window_at_turnover = [
        "Q",
        "E",
        "V",
        "J",
        "Z",
        "ZM",
        "ZM",
        "ZM"
    ]
    reflectors=[
        "YRUHQSLDPXNGOKMIEBFZCWVJAT",
        "FVPJIAOYEDRZXWGCTKUQSBNMHL"
    ]

class EnigmaM4:
    entry="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rolls=[
        "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
        "AJDKSIRUXBLHWTMCQGZNPYFVOE",
        "BDFHJLCPRTXVZNYEIWGAKMUSQO",
        "ESOVPZJAYQUIRHXLNFTGKDCMWB",
        "VZBRGITYUPSDNHLXAWMJQOFECK",
        "JPGVOUMFYQBENHZRDKASXLICTW",
        "NZJHGRCXMYSWBOUFAIVLPEKQDT",
        "FKQHTLXOCBJSPDZRAMEWNIUYGV",
        "LEYJVCNIXWPBQMDRTAKZGFUHOS",
        "FSOKANUERHMBTIYCWLQPZXVGJD"
    ]
    turn_over_notches=[
        "Y",
        "M",
        "D",
        "R",
        "H",
        "HU",
        "HU",
        "HU",
        "",
        ""
    ]
    visible_letters_in_window_at_turnover = [
        "Q",
        "E",
        "V",
        "J",
        "Z",
        "ZM",
        "ZM",
        "ZM"
    ]
    reflectors=[
        "ENKQAUYWJICOPBLMDXZVFTHRGS",
        "RDOBJNTKVEHMLFCWZAXGYIPSUQ"
    ]

class EnigmaG:
    entry="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rolls=[
        "LPGSZMHAEOQKVXRFYBUTNICJDW",
        "SLVGBTFXJQOHEWIRZYAMKPCNDU",
        "CJGDPSHKTURAWZXFMYNQOBVLIE"
    ]
    turn_over_notches=[
        "ACDEHIJKMNOQSTWXY",
        "ABDGHIKLNOPSUVY",
        "CEFIMNPSUVZ"
    ]
    visible_letters_in_window_at_turnover = [
        "SUVWZABCEFGIKLOPQ",
        "STVYZACDFGHKMNQ",
        "UWXAEFHKMNR",
    ]
    reflectors=[
        "IMETCGFRAYSQBZXWLHKDVUPOJN"
    ]


def enigma(word, settings=(0,0,0), plugboard=[], wheel_selection=(0, 1, 2), reflector_selection=0, model=EnigmaI()):
    new_word = ""
    rolls = []
    reflector = model.reflectors[reflector_selection]
    for roll in wheel_selection:
        rolls.append(model.rolls[roll])
    for i in word.upper():
        if i in model.entry:
            index = model.entry.index(plugboard_find(i, plugboard))
            for roll in range(len(rolls)):
                letter = rolls[roll][(index + settings[roll]) % len(model.entry)]
                index = model.entry.index(letter)
            letter = reflector[index]
            index = model.entry.index(letter)
            for roll in range(len(rolls)).__reversed__():
                letter = model.entry[index]
                index = rolls[roll].index(letter) - settings[roll]
            new_word += plugboard_find(model.entry[index], plugboard)
        else:
            new_word += i
        settings[0] = (settings[0] + 1) % len(model.entry)
        for roll in range(len(rolls)):
            if roll != len(wheel_selection)-1:
                if rolls[roll][settings[roll]] in model.turn_over_notches[wheel_selection[roll]]:
                    settings[roll + 1] += 1

            else:
                if rolls[roll][settings[roll]] in model.turn_over_notches[wheel_selection[roll]]:
                    settings[roll] = 0
    return new_word

def plugboard_find(letter, plugboard):
    for l in plugboard:
        if l[0].upper() == letter:
            return l[1].upper()
        if l[1].upper() == letter:
            return l[0].upper()
    return letter