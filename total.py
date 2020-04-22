import cv


def results(font):

    # 1. Create root list from results.txt
    arr = []
    for line in open('results.txt'):
        arr.append(line)

    # 2. Create list all values (rec_all) and clean list for ranged (rec)

    rec_all = []
    rec = []

    # 3. Output dictionaries from root list and input them in new list

    for i in range(len(arr)):
        try:
            eval(arr[i])
        except NameError:
            pass
        except SyntaxError:
            pass
        else:
            rec_all.append(eval(arr[i]))

    # 4. Check the list
    for line in range(len(rec_all)):
        try:
            rec_all[line]['name'] and rec_all[line]['score']
        except KeyError:
            pass
        else:
            rec.append(rec_all[line])

    # 4. Draw list of best results from new list

    for j in range(len(rec)):
        rank = font.render(str(j + 1), 1, cv.BLACK)
        name = font.render(rec[j]['name'], 1, cv.BLACK)
        score = font.render(str(rec[j]['score']), 1, cv.BLACK)
        cv.SURFACE.blit(rank, (int(cv.SIDE_MARGIN * 1.3), int(cv.TOP_MARGIN * (2 + 0.4 * j))))
        cv.SURFACE.blit(name, (int(cv.SIDE_MARGIN * 1.55), int(cv.TOP_MARGIN * (2 + 0.4 * j))))
        cv.SURFACE.blit(score, (int(cv.SIDE_MARGIN * 2.7), int(cv.TOP_MARGIN * (2 + 0.4 * j))))


def best_record(score):
    arr = []
    for line in open('results.txt'):
        arr.append(line)

    rec_all = []
    rec = []
    rec_val = []

    for i in range(len(arr)):
        try:
            eval(arr[i])
        except NameError:
            pass
        except SyntaxError:
            pass
        else:
            rec_all.append(eval(arr[i]))

    for line in range(len(rec_all)):
        try:
            rec_all[line]['name'] and rec_all[line]['score']
        except KeyError:
            pass
        else:
            rec.append(rec_all[line])

    for j in range(len(rec)):
        value = rec[j]['score']
        rec_val.append(value)

    if len(rec_val) == 12:
        if score > rec_val[11]:
            return True
        else:
            return False
    else:
        return True


def add_record(name, score):
    arr = []
    for line in open('results.txt'):
        arr.append(line)

    rec_all = []
    rec = []

    for i in range(len(arr)):
        try:
            eval(arr[i])
        except NameError:
            pass
        except SyntaxError:
            pass
        else:
            rec_all.append(eval(arr[i]))

    for line in range(len(rec_all)):
        try:
            rec_all[line]['name'] and rec_all[line]['score']
        except KeyError:
            pass
        else:
            rec.append(rec_all[line])

    rec.append({'name': name, 'score': score})

    # 4. Bubble sort new list

    for x in range(len(rec)):
        for y in range(len(rec) - x - 1):
            if rec[y]['score'] < rec[y + 1]['score']:
                rec[y]['score'], rec[y + 1]['score'] = rec[y + 1]['score'], rec[y]['score']
                rec[y]['name'], rec[y + 1]['name'] = rec[y + 1]['name'], rec[y]['name']

    write_r = open('results.txt', 'w')
    for line in range(len(rec)):
        write_r.write(str(rec[line]) + '\n')
    write_r.close()


def delete_list():
    write_r = open('results.txt', 'w')
    write_r.write('')
    write_r.close()
