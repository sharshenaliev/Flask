from nums import numbers

def parse(crontab):
    minute, hour, dayofmonth, month, dayofweek = crontab.split()

    def calculate(input, min, max):
        error = "Sorry, incorrect argument!"
        chain = "Sorry, argument is out of range!"
        zero = "Sorry, step cannot be zero!"

        for i in numbers:
            input = input.replace(i['name'], i['number'])
        if input == "*":
            value = ' '.join(str(i) for i in range(min, max))
        elif input.find(",") != -1:
            options = input.split(",")
            result = []
            for item in options:
                if item.isnumeric():
                    result.append(int(item))
                elif item.find("-") != -1 and item.find("/") == -1:
                    sq = item.split("-")
                    for i in range(int(sq[0]), int(sq[1]) + 1):
                        result.append(i)
                elif item.find("/") != -1 and item.find("-") == -1:
                    it = item.split("/")
                    if it[0] == "*":
                        if int(it[1]) != 0:
                            for i in range(min, max, int(it[1])):
                                result.append(i)
                        else:
                            return zero
                    elif it[0].isnumeric() and it[1].isnumeric():
                        if int(it[1]) != 0:
                            for i in range(min, int(it[0]) + 1, int(it[1])):
                                result.append(i)
                        else:
                            return zero
                    else:
                        return error
                elif item.find("/") != -1 and item.find("-") != -1:
                    try:
                        it = item.split("/")
                        sq = it[0].split("-")
                        if int(it[1]) != 0:
                            for i in range(int(sq[0]), int(sq[1]) + 1, int(it[1])):
                                result.append(i)
                        else:
                            return zero
                    except:
                        return error
                else:
                    return error
            result.sort()
            if result[0] >= min and result[-1] < max:
                value = ' '.join(str(i) for i in result)
            else:
                value = chain
        elif input.find("-") != -1 and input.find("/") == -1 and input.find(",") == -1:
            sq = input.split("-")
            if all(item.isnumeric() for item in sq):
                if min <= int(sq[0]) < max and min <= int(sq[1]) < max:
                    value = ' '.join(str(i) for i in range(int(sq[0]), int(sq[1]) + 1))
                else:
                    value = chain
            else:
                value = error
        elif input.find("/") != -1 and input.find("-") == -1 and input.find(",") == -1:
            options = input.split("/")
            if options[0] == "*":
                value = ' '.join(str(i) for i in range(min, max, int(options[1])))
            elif options[0].isnumeric() and options[1].isnumeric():
                if int(options[1]) != 0:
                    if min <= int(options[0]) < max and min <= int(options[1]) < max:
                        value = ' '.join(str(i) for i in range(min, int(options[0]) + 1, int(options[1])))
                    else:
                        value = chain
                else:
                    value = zero
            else:
                value = error
        elif input.find("-") != -1 and input.find("/") != -1 and input.find(",") == -1:
            try:
                options = input.split("/")
                sq = options[0].split("-")
                if min <= int(sq[0]) < max and min <= int(sq[1]) < max:
                    if int(options[1]) != 0:
                        value = ' '.join(str(i) for i in range(int(sq[0]), int(sq[1]) + 1, int(options[1])))
                    else:
                        value = zero
                else:
                    value = chain
            except:
                value = error
        elif input.isnumeric():
            if min <= int(input) < max:
                value = input
            else:
                value = chain
        else:
            value = error
        return value

    message = [calculate(minute, min=0, max=60),
               calculate(hour, min=0, max=24),
               calculate(dayofmonth, min=1, max=32),
               calculate(month, min=1, max=13),
               calculate(dayofweek, min=1, max=8)]
    return message
