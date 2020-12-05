string1 = "\t{0[0]:^10}\t{0[1]:^10}\t{0[2]:^10}\t{0[3]:^10}\t{0[4]:^10}\t{0[5]:^10}\t{0[6]:^10}\t{0[7]:^10}"
string2 = ["姓名", "年龄", "性别", "学号", "数学", "英语", "语文", "总分"]
string3 = "\t{:^10}\t{:^10}\t{:^10}\t{:^10}\t{:^10}\t{:^10}\t{:^10}\t{:^10}"


class Student(object):
    def __init__(self):
        self.students = []

    @staticmethod
    def choice_menu():
        print("-" * 50 + "\n\t\t学生成绩管理系统" + "\n\t\t1、添加学生信息" +
              "\n\t\t2、删除学生信息" + "\n\t\t3、修改学生信息" + "\n\t\t4、查找学生信息" +
              "\n\t\t5、显示学生信息" + "\n\t\t6、科目成绩信息" + "\n\t\t7、排序学生成绩" +
              "\n\t\t8、退出程序\n" + "-" * 50
              )

    def add_student(self):
        student = {}
        name = input("请输入学生姓名：")
        student['姓名'] = name
        age = int(input("请输入学生年龄："))
        student['年龄'] = age
        sex = input("请输入学生性别：")
        student['性别'] = sex
        num = int(input("请输入学生学号："))
        for stu in self.students:
            while num == stu.get("学号"):
                print("已有该学号!")
                num = int(input("请输入学生学号："))
        student['学号'] = num
        math = float(input("请输入学生数学成绩："))
        student['数学'] = math
        english = float(input("请输入学生英语成绩："))
        student['英语'] = english
        chinese = float(input("请输入学生语文成绩："))
        student['语文'] = chinese
        student['总分'] = math + english + chinese
        self.students.append(student)

    def delete_student(self):
        flag = False
        name = input("请输入要删除的学生姓名：")
        for student in self.students:
            if name == student.get("姓名"):
                self.students.remove(student)
                print("删除成功！")
                flag = True
        if flag is False:
            print("没有该学生信息！")

    def modify_student(self):
        flag = False
        name = input("请输入要修改的学生姓名：")
        for student in self.students:
            if name == student.get('姓名'):
                command = input("请输入要修改的信息（如姓名、年龄、学号、数学、英语、语文）：")
                if command == '姓名':
                    new_name = input("请输入新的姓名：")
                    student['姓名'] = new_name
                elif command == '年龄':
                    new_age = int(input("请输入新的年龄："))
                    student['年龄'] = new_age
                elif command == '学号':
                    new_num = int(input("请输入新的学号："))
                    student['学号'] = new_num
                elif command == '数学':
                    new_math = float(input("请输入新的数学成绩："))
                    student['数学'] = new_math
                elif command == '英语':
                    new_english = float(input("请输入新的英语成绩："))
                    student['英语'] = new_english
                elif command == '语文':
                    new_chinese = float(input("请输入新的语文成绩："))
                    student['语文'] = new_chinese
                else:
                    print("请输入正确的信息！")
                student['总分'] = student['语文'] + student['数学'] + student['英语']
                flag = True
        if flag is False:
            print("没有该学生信息！")

    def find_student(self):
        name = input("请输入要查找的学生姓名：")
        flag = False
        for student in self.students:
            if name == student.get("姓名"):
                print("-" * 130 + "\n" + string1.format(string2))
                print(string3.format(student['姓名'], student['年龄'], student['性别'], student['学号'],
                                     student['数学'], student['英语'], student['语文'], student['总分'])
                      )
                print("-" * 130)
                flag = True
        if flag is False:
            print("没有该学生信息！")

    def show_student(self):
        print("-" * 130 + "\n" + string1.format(string2))
        for student in self.students:
            print(string3.format(student['姓名'], student['年龄'], student['性别'], student['学号'],
                                 student['数学'], student['英语'], student['语文'], student['总分'])
                  )
        print("-" * 130)

    def calculate_student(self):
        list1 = []
        command = input("请选择查看哪门科目（如语文、数学、英语）：")
        if command == '语文':
            for i in range(len(self.students)):
                list1.append(self.students[i][command])
            print("语文总分为：%.2f" % (sum(list1)))
            print("语文平均分为：%.2f" % (sum(list1) / len(self.students)))
        elif command == '数学':
            for i in range(len(self.students)):
                list1.append(self.students[i][command])
            print("数学总分为：%.2f" % (sum(list1)))
            print("数学平均分为：%.2f" % (sum(list1) / len(self.students)))
        elif command == '英语':
            for i in range(len(self.students)):
                list1.append(self.students[i][command])
            print("英语总分为：%.2f" % (sum(list1)))
            print("英语平均分为：%.2f" % (sum(list1) / len(self.students)))
        else:
            print("请输入正确的文字！")

    def sort_student(self):
        list1 = []
        for student in self.students:
            list1.append(student)
        list2 = sorted(list1, key=lambda x: x['总分'], reverse=True)
        print("-" * 130 + "\n" + string1.format(string2))
        for i in range(len(list2)):
            print(string3.format(list2[i]['姓名'], list2[i]['年龄'], list2[i]['性别'], list2[i]['学号'],
                                 list2[i]['数学'], list2[i]['英语'], list2[i]['语文'], list2[i]['总分'])
                  )
        print("-" * 130)

    def main(self):
        self.choice_menu()
        while True:
            command = input("请输入选择：")
            if command == '1':
                self.add_student()
            elif command == '2':
                self.delete_student()
            elif command == '3':
                self.modify_student()
            elif command == '4':
                self.find_student()
            elif command == '5':
                self.show_student()
            elif command == '6':
                self.calculate_student()
            elif command == '7':
                self.sort_student()
            elif command == '8':
                break


if __name__ == "__main__":
    Student().main()
