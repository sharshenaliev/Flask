def macro(crontab):
    if crontab == "@monthly":
        message = [0, 0, 1, ' '.join([str(i) for i in range(1, 13)]), ' '.join([str(i) for i in range(1, 8)])]
    elif crontab == "@weekly":
        message = [0, 0, ' '.join([str(i) for i in range(1, 32)]), ' '.join([str(i) for i in range(1, 13)]), 0]
    elif crontab == "@daily" or crontab == "@midnight":
        message = [0, 0, ' '.join([str(i) for i in range(1, 32)]), ' '.join([str(i) for i in range(1, 13)]),
                   ' '.join([str(i) for i in range(1, 8)])]
    elif crontab == "@hourly":
        message = [0, ' '.join([str(i) for i in range(24)]), ' '.join([str(i) for i in range(1, 32)]),
                   ' '.join([str(i)for i in range(1, 13)]), ' '.join([str(i) for i in range(1, 8)])]
    elif crontab == "@yearly" or crontab == "@annually":
        message = [0, 0, 1, 1, ' '.join([str(i) for i in range(1, 8)])]
    elif crontab == "@reboot":
        message = "after rebooting"
    else:
        message = "wrong input of non-standard macro"
    return message
