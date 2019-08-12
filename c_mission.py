import pickle

def save_file(boy,girl,count):
    file_boy_name = 'boy_' + str(count) + '.txt'
    file_girl_name = 'girl_' + str(count) + '.txt'

    boy_file = open(file_boy_name,'wb')
    girl_file = open(file_girl_name,'wb')

    pickle.dump(boy,boy_file)
    pickle.dump(girl,girl_file)

    boy_file.close()
    girl_file.close()

def split_file(filename):
    f = open(filename)
    boy = []
    girl = []
    count = 1

    for each in f:
        if each[:6] != '======':
            (role,line_spoken) = each.split(':',1)
            if role == '小甲鱼':
                boy.append(line_spoken)
            if role == '小客服':
                girl.append(line_spoken)
        else:
            save_file(boy,girl,count)

            boy = []
            girl = []
            count += 1
    save_file(boy,girl,count)
    f.close()

split_file('record.txt')
    
