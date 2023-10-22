import sys
import pickle
import random

def main():
    # выполняем POST-запрос на сервер по эндпоинту add с параметром json
    with open('model/regions_classifier.pkl', 'rb') as pkl_file:
        reg_class = pickle.load(pkl_file)
        regions = list(reg_class.keys())
    while True:
        rand_regs = []
        for i in range(3):
            rand = random.randint(0, len(regions))
            rand_regs.append(regions[rand])
        print(f'Введите название региона (например, {rand_regs}) либо Выход:')
        phrase = str(input())
        phrase = phrase.replace('обл-ть', 'область').replace('республика', 'Республика')
        if phrase in reg_class.keys():
            print(reg_class[phrase])
        elif phrase == 'Выход':
            sys.exit()
        else:
            print('Некорректное название региона')
    
if __name__ == '__main__':
    main()