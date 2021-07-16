def vhod(arg):
    with open('users_data.txt', 'r') as d:
        s = d.read()
        s = s.split(';')
    t = [i.split(',') for i in s]
    index = -1
    shetchik = 1
    shetchik1 = 1
    shetchik2 = 1
    name = 0
    vost1 = 0
    if arg == 0:
            while index == -1:
                  otvet = input('Введи логин ')
                  if otvet == '':
                      print('Вы ничего не ввели')
                      vhod(0)
                  for i in t:
                      for j in i[:1]:
                          if j == otvet:
                              index = t.index(i)
                              name = otvet
                              break
                  if index == -1:
                      print(
                          'Такого логина не зарегистрировано \n Если хотите зарегестрироваться, напишите - регистрация \n Если вас интересует главное меню, напишите - меню \n В ином случае, вы останетесь в этом окне   ')
                      otvet1 = input().lower()
                      if otvet1 == 'регистрация':
                          registration('registration')
                          break
                      elif otvet1 == 'меню':
                          gen_menu(0)
                          break
                      else:

                          shetchik += 1
                          if shetchik == 4:
                              print('закончились попытки, подвердите, что вы не робот ')
                              robot()

    else:
        print(
            'Что-то пошло не так=) \n Если хотите войти, напишите - вход \n Если зарегистрироваться, напишите - регистрация \n Чтобы попасть в главное меню, напишите - меню ')
        otvet2 = input().lower()
        if otvet2 == 'вход':
            vhod(0)
        elif otvet2 == 'регистрация':
            registration('registration')
        else:
            gen_menu(0)

    if index >= 0:
        pass1 = 0
        while pass1 == 0:
            password = input('Введи пароль ')
            if password == t[index][1]:
                pass1 += 10
                print('Вы вошли, добро пожаловать ')
                gen_menu(name)
                break
            else:
                print(
                    'Неправильный пароль  \n Для того чтобы восстановить пароль, напишите - восстановить \n Если хотите попасть в главное меню, напишите - меню \n В ином случае, вы останетесь в этом окне ')
                otvet3 = input().lower()
                if otvet3 == 'восстановить':
                    while vost1 == 0:
                        vost = input(t[index][3]).lower()
                        if vost == t[index][4]:
                            vost1 += 10
                            print('Вот ваш пароль: ', t[index][1])
                            pass1 += 10
                            vhod(0)
                            break
                        else:
                            print(
                                'Неправильный ответ \n Для того чтобы попасть в главное меню, напишите - меню \n Если хотите вернутся в меню входа, напишите - вход \n В ином случае, вы останетесь в этом окне')
                            otvet4 = input().lower()
                            if otvet4 == 'меню':
                                pass1 += 10
                                vost1 += 10
                                gen_menu(0)
                                break
                            elif otvet4 == 'вход':
                                pass1 += 10
                                vost1 += 10
                                vhod(0)
                                break
                            else:
                                shetchik2 += 1
                                if shetchik2 == 4:
                                    robot()


                elif otvet3 == 'меню':
                    pass1 += 10
                    gen_menu(0)
                else:

                        shetchik1 += 1
                        if shetchik1 == 4:
                              robot()



