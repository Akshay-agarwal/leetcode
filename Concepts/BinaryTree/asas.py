# Complete the function below.


def css_string_to_color(colorString):
    # creating dictionary for hex values
    css_dict = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    new = []
    # check valid input through ASCII Value
    for i in range(len(colorString) - 1):
        print(ord(colorString[i + 1].upper()))
        if 48 <= ord(colorString[i + 1].upper()) <= 57 or 65 <= ord(colorString[i + 1].upper()) <= 70:
            continue
        else:
            return "Error"
    # check for valid length of input
    if len(colorString) == 4 or len(colorString) == 7:

        # if length is 4, make it to length 7 by adding it two times
        if len(colorString) == 4:
            print("here")
            colorString = list(colorString[1:])
            for i in colorString:
                new.append(i)
                new.append(i)
        if len(colorString) == 7:
            new = list(colorString[1:])

        res = 0
        j = 0
        new_rgb = []

        # create one rgb list by adding 2 elements from list at a time
        rgb = [new[0] + new[1], new[2] + new[3], new[4] + new[5]]

        # from rgb list, create rgb value by multiplying 16 to digit at one's place and adding it to digit at oth place
        for i in range(len(rgb)):
            if rgb[i][0].upper() in css_dict:
                res += css_dict[rgb[i][0].upper()] * 16
            else:
                res += int(rgb[i][0]) * 16

            if rgb[i][1].upper() in css_dict:
                res += css_dict[rgb[i][1].upper()]
            else:
                res += int(rgb[i][1])

            # append result for each iteration to new_rgb
            new_rgb.append(res)
            res = 0

        # now the new_rgb has all the values of rgb and multiply 65536 to 2nd place(blue color), 256 to one's place(green color) and 1 to 0th place(red color) i.e convert to OLE
        res += new_rgb[0] + new_rgb[1] * 256 + new_rgb[2] * 65536

        return res

    else:
        return "Error"

