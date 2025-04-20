import datetime as dt


class Quest:
    def __init__(self, name, description, goal="У самурая нет цели"):
        self.name = name
        self.description = description
        self.goal = goal
        self.start_time = None
        self.end_time = None
        print(f"Получен новый квест! Цель: {goal}.")

    def accept_quest(self):
        if self.end_time is not None:
            return "С этим испытанием вы уже справились."
        else:
            self.start_time = dt.datetime.now()
            return f"Начало {self.name} положено в {self.start_time}"

    def pass_quest(self):
        if self.start_time is None:
            return "Нельзя завершить то, что не имеет начала!"
        else:
            self.end_time = dt.datetime.now()
            completion_time = self.end_time - self.start_time
            return f"Квест {self.name} окончен. Время выполнения квеста: {completion_time}."

    def __str__(self):
        if self.start_time is not None:
            actual_time = dt - self.start_time
            return f"Цель квеста {self.name} — {self.goal}. Квест выполняется напротяжении {actual_time}."
        else:
            return f" Цель квеста {self.name} — {self.goal}."


new_quest = Quest(
    "Спасти пирожочек",
    "Потерялся пирожочек на кухне. Кажется, он упал за холодильник.",
    "Найти пирожочек",
)

print(new_quest.accept_quest())
print(new_quest.pass_quest())
print(new_quest.accept_quest())
