# Validation of phone number
# length of no less than 11 digits
# China Mobile, China Union and China Telecom version
# only integers can be input

def phone_detect():
    phone_number = str(input('Enter Your Number: '))
    CN_mobile = [134, 135, 136, 137, 138, 139, 150, 151, 152, 157, 158, 159, 182, 183, 184, 187, 188, 147, 178, 1705]
    CN_union = [130, 131, 132, 155, 156, 185, 186, 145, 176, 1709]
    CN_telecom = [133, 153, 180, 181, 189, 177, 1700]
    if len(phone_number) != 11:
        print('Invalid length, your number should be in 11 digits')
    elif int(phone_number[0:3]) in CN_mobile:
        print('Operator: China Mobile')
        print("We're sending verification code via text to your phone: {}".format(phone_number))
    elif int(phone_number[0:3]) in CN_union:
        print('Operator: China Union')
        print("We're sending verification code via text to your phone: {}".format(phone_number))
    elif int(phone_number[0:3]) in CN_telecom:
        print('Operator: China Telecom')
        print("We're sending verification code via text to your phone: {}".format(phone_number))
    else:
        print('No such an operator')

phone_detect()

# there will be some vulnerabilities in the above code, a better version would include 4 digits check
def number_test():

    while True:
        number = input('Enter Your Number: ')
        CN_mobile = [134, 135, 136, 137, 138, 139, 150, 151, 152, 157, 158, 159, 182, 183, 184, 187, 188, 147, 178, 1705]
        CN_union = [130, 131, 132, 155, 156, 185, 186, 145, 176, 1709]
        CN_telecom = [133, 153, 180, 181, 189, 177, 1700]
        first_three = int(number[0:3])
        first_four = int(number[0:4])

        if len(number) == 11:

            if first_three in CN_mobile or first_four in CN_mobile:
                print('Operator: China Mobile')
                print('We\'re sending verificaiton code via text to your phone: ', number)
                break
            elif first_three in CN_union or first_four in CN_union:
                print('Operator: China Union')
                print('We\'re sending verificaiton code via text to your phone: ', number)
                break
            elif first_three in CN_telecom or first_four in CN_telecom:
                print('Operator: China Telecom')
                print('We\'re sending verificaiton code via text to your phone: ', number)
                break
            else:
                print('No such a operator')
        else:
            print('Invalid length, your number should be in 11 digits')

number_test()