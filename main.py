from random import randint

# Глобальные константы
DEFAULT_ATTACK = 5  # базовый урон
DEFAULT_DEFENCE = 10  # базовая защита
DEFAULT_STAMINA = 80  # базовая выносливость


class Character:
    """
    Базовый класс для всех персонажей.
    """

    RANGE_VALUE_ATTACK = (1, 3)  # константа для определения диапазона урона
    RANGE_VALUE_DEFENCE = (1, 5)  # константа для определения диапазона защиты
    SPECIAL_SKILL = "Удача"  # особое умение
    SPECIAL_BUFF = 15  # значение для особого умения
    BRIEF_DESC_CHAR_CLASS = "отважный любитель приключений"  # базовое описание класса

    def __init__(self, name: str) -> None:
        """
        :param name: имя персонажа
        """
        self.name = name

    def attack(self) -> str:
        """
        Вычисляет и возвращает строку с нанесённым уроном.
        Returns:
            str: Сообщение о нанесённом уроне.
        """
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return f"{self.name} нанёс противнику урон, равный {value_attack}. "

    def defence(self) -> str:
        """
        Вычисляет и возвращает строку с заблокированным уроном.
        Returns:
            str: Сообщение о заблокированном уроне.
        """
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return f"{self.name} блокировал {value_defence} урона. "

    def special(self) -> str:
        """
        Возвращает строку о применении специального умения.
        Returns:
            str: Сообщение о применении специального умения
        """
        return f"{self.name} применил {self.SPECIAL_SKILL} - {self.SPECIAL_BUFF} . "

    def __str__(self) -> str:
        """
        Метод для вывода базового описания класса
        Returns:
            str: Сообщение с базовым описанием класса.
        """
        return f"{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}. "


class Warrior(Character):
    """
    Класс персонажа воин. Имеет усиленные значения урона и защиты.
    """

    RANGE_VALUE_ATTACK = (3, 5)  # диапазон урона воина
    RANGE_VALUE_DEFENCE = (5, 10)  # диапазон защиты воина
    SPECIAL_SKILL = "Выносливость"  # особое умение воина
    SPECIAL_BUFF = DEFAULT_STAMINA + 25  # значение для особого умения
    BRIEF_DESC_CHAR_CLASS = " дерзкий воин ближнего боя. Сильный, выносливый и отважный"  # описание для воина


class Mage(Character):
    """
    Класс персонажа маг. Имеет высокий уровень урона и низкую защиту.
    """

    RANGE_VALUE_ATTACK = (5, 10)  # диапазон урона мага
    RANGE_VALUE_DEFENCE = (-2, 2)  # диапазон защиты мага
    SPECIAL_SKILL = "Атака"  # особое умение мага
    SPECIAL_BUFF = DEFAULT_ATTACK + 40  # значение для особого умения
    BRIEF_DESC_CHAR_CLASS = " находчивый воин дальнего боя. Обладает высоким интеллектом"  # описание для мага


class Healer(Character):
    """
    Класс персонажа лекарь. Имеет среднюю защиту, низкий урон.
    """

    RANGE_VALUE_ATTACK = (-3, -1)  # диапазон урона лекаря
    RANGE_VALUE_DEFENCE = (3, 5)  # диапазон защиты лекаря
    SPECIAL_SKILL = "Защита"  # особое умение лекаря
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30  # значение для особого умения лекаря
    BRIEF_DESC_CHAR_CLASS = " могущественный заклинатель. Черпает силы из природы, веры и духов"  # описание для лекаря


# warrior = Warrior("Кодослав")
# print(warrior)
# print(warrior.attack())


def choice_char_class(char_name: str) -> Character:
    """
    Метод для выбора персонажа.
    Args:
        char_name (str): Имя персонажа.
    Returns:
        Character: Выбранный персонаж.
    """
    game_classes = {
        "warrior": Warrior,
        "mage": Mage,
        "healer": Healer,
    }  # словарь для соотнесения ввода пользователя и класса персонажа
    approve_choice: str = None
    while approve_choice != "y":
        selected_class = input(
            "Введи название персонажа, "
            "за которого хочешь играть: \nВоитель — warrior, \nМаг — mage, \nЛекарь — healer: "
        )
        char_class: Character = game_classes[selected_class](char_name)
        print(char_class)
        approve_choice = input(
            "Нажми (Y), чтобы подтвердить выбор, "
            "или любую другую кнопку, "
            "чтобы выбрать другого персонажа "
        ).lower()
    return char_class


def start_training(character) -> None:
    """
    Метод для тренировки персонажа
    Args:
        character (Character): Экземпляр выбранного персонажа.
    """
    print("Потренируйся управлять своими навыками.")
    print(
        "Введи одну из команд:\nattack — чтобы атаковать противника, "
        "\ndefence — чтобы блокировать атаку противника или "
        "\nspecial — чтобы использовать свою суперсилу."
    )
    print("Если не хочешь тренироваться, введи команду skip.")

    commands = {
        "attack": character.attack,
        "defence": character.defence,
        "special": character.special,
    }  # словарь команд для тренировки персонажа

    cmd = None
    while cmd != "skip":
        cmd = input("Введи команду: ")
        if cmd in commands:
            print(commands[cmd]())
        else:
            print("Неверная команда.")
    return print("Тренировка окончена")


char_name = input("Введи имя персонажа: ")
char = choice_char_class(char_name)
start_training(char)
