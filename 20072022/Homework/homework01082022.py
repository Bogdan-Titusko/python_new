
while True:
    try:
        isikukood = input('Enter your ID: or type exit!:  ')
        if isikukood.lower() == 'exit':
            break
        int(isikukood)
        if len(isikukood) != 11:
            raise UserWarning
    except UserWarning:
        if len(isikukood) > 11:
            print('Code is long')
        else:
            print('Code is short')
            continue
    except ValueError:
        print('Code is not numeric!')
        continue
    else:
        while True:
            user_choice = input('Please choose:\n1.Get gender\n'
                                '2.Get date of birth\n3.Get region of birth\n'
                                '4.Valuidate\n5.Change ID\n'
                                '0.Exit\n--> ')
            if user_choice == '1':
                if isikukood[0] not in ['9', '0']:
                    if int(isikukood[0]) % 2 == 0:
                        gender = 'female'
                    else:
                        gender = 'male'
                    print('You are ' + gender)
                else:
                    print('Unable to determine gender!')
            elif user_choice == '2':
                if isikukood[0] not in ['9', '0']:
                    if isikukood[0] in ['1', '2']:
                        bcent = '18'
                    elif isikukood[0] in ['3', '4']:
                        bcent = '19'
                    elif isikukood[0] in ['5', '6']:
                        bcent = '20'
                    elif isikukood[0] in ['7', '8']:
                        bcent = '21'  # 39710173734
                    print(f'Your date of birth is {isikukood[5:7]}.{isikukood[3:5]}.{bcent}{isikukood[1:3]}.')
                else:
                    print('Can\' determine date of birth! ')
            elif user_choice == '3':
                if int(isikukood[7:10]) in range(0, 11):
                    haigla = 'Kuressaare haigla'
                elif int(isikukood[7:10]) in range(10, 20):
                    haigla = 'Tartu Ülikooli Naistekliinik'
                elif int(isikukood[7:10]) in range(20, 151):
                    haigla = ' Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)'
                elif int(isikukood[7:10]) in range(150, 161):
                    haigla = ' Keila haigla'
                elif int(isikukood[7:10]) in range(160, 221):
                    haigla = 'Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)'
                elif int(isikukood[7:10]) in range(220, 271):
                    haigla = 'Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)'
                elif int(isikukood[7:10]) in range(270, 371):
                    haigla = 'Maarjamõisa kliinikum (Tartu), Jõgeva haigla'
                elif int(isikukood[7:10]) in range(370, 421):
                    haigla = 'Narva haigla'
                elif int(isikukood[7:10]) in range(420, 471):
                    haigla = 'Pärnu haigla'
                elif int(isikukood[7:10]) in range(470, 491):
                    haigla = 'Haapsalu haigla'
                elif int(isikukood[7:10]) in range(490, 521):
                    haigla = 'Järvamaa haigla (Paide)'
                elif int(isikukood[7:10]) in range(520, 571):
                    haigla = 'Rakvere haigla, Tapa haigla'
                elif int(isikukood[7:10]) in range(570, 601):
                    haigla = 'Valga haigla'
                elif int(isikukood[7:10]) in range(600, 651):
                    haigla = ' Viljandi haigla'
                elif int(isikukood[7:10]) in range(650, 701):
                    haigla = ' Lõuna-Eesti haigla (Võru), Põlva haigla'
                print(f'Your region is {isikukood[7:10]}.{haigla}')
                continue
            if user_choice == '4':
                if int(isikukood[0]):
                    validate = int(isikukood[0]) * 1 + int(isikukood[1]) * 2 + int(isikukood[2]) * 3 + int(
                        isikukood[3]) * 4 + int(isikukood[4]) * 5 + int(isikukood[5]) * 6 + int(isikukood[6]) * 7 + int(
                        isikukood[7]) * 8 + int(isikukood[8]) * 9 + int(isikukood[9]) * 1
                    validate2 = (validate / int(11))
                    validate3 = (int(validate2) * 11)
                    validate4 = (validate - validate3)
                    print(f'Your validate number is :' + str(validate4))
                else:
                    print('Erorr')
            if user_choice == '5':
                break
            if user_choice == '0':
                print('Good bye')
                quit()
