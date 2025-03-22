# Python网课学习
def menu():
    print('-' * 40)
    print('学生管理系统 V1.0')
    print('[1] 添加学生信息')
    print('[2] 删除学生信息')
    print('[3] 修改学生信息')
    print('[4] 查询学生信息')
    print('[5] 遍历所有学生信息')
    print('[6] 保存数据到文件')
    print('[6] 退出系统')
    print('-' * 40)


students = []


def add_student():
    name = input("请输入要添加学生的姓名: ")
    age = int(input("请输入要添加学生的年龄："))
    address = input("请输入要添加学生的电话：")
    student = {}
    student["name"] = name
    student["age"] = age
    student["address"] = address
    global students
    students.append(student)
    print(f"学生{name}添加成功")


def get_all_students():
    global students
    for i in students:
        print(i)


def del_student():
    name = input("请输入要删除学生的姓名：")
    global students
    for i in students:
        if i["name"] == name:
            students.remove(i)
            print(f"学生{name}信息删除成功")
            break
    else:
        print("您要删除的信息不存在")


def exit_student():
    name = input("请输入要编辑学生的姓名：")
    global students
    for i in students:
        if i["name"] == name:
            i["name"] = input("请输入修改后的学生姓名：")
            i["age"] = int(input("请输入修改后的学生年龄："))
            i["mobile"] = input("请输入修改后的学生电话：")
            print(f"学生{name}修改成功")
            break
    else:
        print("您要修改的学员未找到")


def get_student():
    name = input("请输入要查询学生的姓名：")
    global students
    for i in students:
        if i["name"] == name:
            print(i)
            break
    else:
        print("您要查询的学生信息暂未找到")


def save_data_to_file():
    global students
    if not len(students) == 0:
        f = open("data.txt", "w", encoding="utf-8")
        f.write(str(students))
        f.close()
        print("信息保存成功!")


def load_data():
    global students
    f = open("data.txt", "r", encoding="utf-8")
    students = eval(f.read())
    f.close()


load_data()
while True:
    menu()
    user_num = int(input('请输入您要操作的功能编号：'))
    if user_num == 1:
        add_student()
    elif user_num == 2:
        del_student()
    elif user_num == 3:
        exit_student()
    elif user_num == 4:
        get_student()
    elif user_num == 5:
        get_all_students()
    elif user_num == 6:
        save_data_to_file()
    elif user_num == 7:
        print('退出系统成功，感谢您使用学生管理系统V1.0')
        break
    else:
        print('您输入的功能编号不正确，请重新输入')
