# สร้าง function แบบไม่มี return
def hello(name):
    print("Hello %s" %name)


# การเรียกใช้งาน function
hello("Tipiwat Sanpiboon")

# สร้าง function แบบมี return value
def area(width, height):
    total = width * height
    return total


# เรียกใช้งาน function
print(area(10, 20))

# function แบบมีการกำหนดค่าเริ่มต้นไว้
def show_info(name, salary = 15000, lang = "not define"):
    print("Name: %s" % name)
    print("Saraly: %s" %salary)
    print("lang: %s" %lang)


show_info("Tipiwat Sanpiboon")
print()
show_info("Tipiwat Sanpiboon", 90000)
print()
show_info("Tipiwat Sanpiboon", 90000, "C++")
print()