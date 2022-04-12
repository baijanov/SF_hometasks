""" Игра угадай число.
Компьютер сам загадывает и угадывает число менее чем за 20 раз
"""
import numpy as np

def random_predict(number:int=1)->int:
    """Рандомно угадываем число
    
    Args:
    number(int, optional): Загадываем чиcло. Defaults to 1.
    
    Returns:
    int:число попыток
    """
    min = 1
    max = 101

    number = np.random.randint(min, max)

    count = 0

    while True:
        count+=1
        mid = (min+max) // 2
        
        if mid > number:
            max = mid
            
        elif mid < number:
            min = mid
            
        else:
            break #конец игры выход из цикла
    return count

def score_game(random_predict)->int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls)) # находим среднее количество попыток
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)


# RUN
if __name__ == '__main__':
    score_game(random_predict)