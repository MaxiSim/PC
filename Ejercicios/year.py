
def main ():
    month = int(input('En que mes naciste?: '))
   
    if 1<= month <= 3:
        print('Sos del Q1')
    elif 4<= month <=6:
        print('Sos del Q2')
    elif 7<= month <= 9:
        print('Sos del Q3')
    elif 10<= month <= 12:
        print('Sos del Q4')
    else:
        print('Ese mes no existe')
        
if __name__ == '__main__':
    main()

        
    