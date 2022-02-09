from ArithmeticLogicUnit import ALU


def cv1(alu):
    alu.load_instruction('input_pt1')
    print(alu.getX())


def cv2(alu):
    alu.load_instruction('input_pt2')
    print(alu.getZ())


def cv3(alu):
    alu.load_instruction('input_pt3')
    print("{0} {1} {2} {3}".format(alu.getW(), alu.getX(), alu.getY(), alu.getZ()))


def MONAD(alu):
    alu.disable_manual_input()
    #"29989297949519"
    for number in ["29989297949519"]:
        number_str = str(number)
        if number_str.find("0") == -1:
            alu.set_number(number_str)
            alu.load_instruction('MONAD')
            if alu.getZ() == 0:
                print("number: {0}".format(number_str))
                print("z:{0}".format(alu.getZ()))
    print("{0} {1} {2} {3}".format(alu.getW(), alu.getX(), alu.getY(), alu.getZ()))


if __name__ == '__main__':
    arithmetic_logic_unit = ALU()
    MONAD(arithmetic_logic_unit)
