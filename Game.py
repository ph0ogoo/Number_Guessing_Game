import random
import time
import ConstantGame as CG

def GameLoop(count_chances: int) -> None:

    # начало отсчета времени
    start = time.time()

    hidden_number = GetRandomValue()
    choise = 0

    while (choise < count_chances):

        choise += 1

        while(True):
            try:
                person_input = int(input(CG._MESSAGE_ENTER_GUESS.format(current_choise = choise)))
                if person_input in range(CG._range_min, CG._range_max + 1):
                    break
                else:
                    print(f"THE VALUE SHOULD BE IN THE RANGE FROM {CG._range_min} TO {CG._range_max}")

            except ValueError:
                print("ERROR, ENTER A VALID VALUE")

        win_lose = CheckWinOrLose(person_input, hidden_number)[0]
        _less_or_greater = CheckWinOrLose(person_input, hidden_number)[1]

        if win_lose:
            print(CG._MESSAGE_WIN.format(choise = choise, your_time = round(time.time() - start)))
            return 
        else:
            print(CG._MESSAGE_INCORRECT.format(less_or_greater = _less_or_greater, input = person_input))

    else:
        print(CG._MESSAGE_LOSE.format(hidden = hidden_number))


def CheckWinOrLose(current_choise: int, hidden_number: int) -> tuple:
    
    if current_choise < hidden_number:
        _less_or_greater = "greater"
    else:
        _less_or_greater = "less"

    if current_choise == hidden_number:
        return [True, _less_or_greater]

    return [False, _less_or_greater]


def GetRandomValue() -> int:
    return random.randint(CG._range_min, CG._range_max)


def main():

    try:
        # Строка приглащения
        print(CG._MESSAGE_WELCOME)
        
        # реализацию возможности играть много раз
        while(True):
            # Прошу пользователя выбрать уровень сложности
            while (True):
                try:
                    _input_difficulty_level = int(input(CG._MESSAGE_DIFFICULTY_LEVEL))
                    if _input_difficulty_level in range(1, 4):
                        break   
                    else:
                        raise ValueError
                except ValueError:
                    print("NO, ENTER 1, 2 OR 3")

            # Устанавливаю количество попыток
            match(_input_difficulty_level):
                case 1:
                    difficulty_level = "Easy"
                    count_chances = 10
                case 2:
                    difficulty_level = "Medium"
                    count_chances = 5
                case 3:
                    difficulty_level = "Hard"
                    count_chances = 3

            # вывод правил игры
            print(CG._MESSAGE_START_GAME.format(difficulty_level = difficulty_level))
            print(CG._MESSAGE_TASK.format(count_chances = count_chances))

            # начало игрового цикла
            GameLoop(count_chances)

            # предложение сыграть еще раз
            while(True):
                try:
                    person_input = input(CG._MESSAGE_GAME_AGAIN)
                    
                    if (person_input == 'n'):
                        exit()
                    elif (person_input == 'y'):
                        break
                    else: raise ValueError
                
                except ValueError:
                    print("choose 'y' or 'n'")

    except KeyboardInterrupt:                       # возможность выйти из игры комбинацией ctrl+c
        print("\nYOU HAVE AUTOMATICALLY LOST\n")
        exit()
        


if __name__ == '__main__':
    main()  




