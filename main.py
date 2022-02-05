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
    step_print = 100000
    for number in range(11111111111111, 99999999999999):
        number_str = str(number)
        if number_str.find("0") == -1:
            alu.set_number(number_str)
            alu.load_instruction('MONAD')
            step_print -= 1
            if step_print == 0:
                print(number_str)
                step_print = 100000
            if alu.getZ() == 0:
                print("number: {0}".format(number_str))
                print("z:{0}".format(alu.getZ()))


if __name__ == '__main__':
    arithmetic_logic_unit = ALU()
    MONAD(arithmetic_logic_unit)
