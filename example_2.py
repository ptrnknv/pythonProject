import xlrd

wb = xlrd.open_workbook('trekking3.xlsx')
sh = wb.sheet_by_index(0)
ss = wb.sheet_by_index(1)
common_dt = {}
for rx in range(1, sh.nrows):
    dd = sh.row(rx)
    added_list = []
    for el in dd[1:]:
        el = el.value
        if el== '':
            el = 0
        added_list.append(el)
    common_dt[dd[0].value] = common_dt.get(dd[0].value, []) + added_list
raskl = {}
days = []
for el in range(1, ss.nrows):
    data = ss.row(el)
    day = int(data[0].value)
    name = data[1].value
    gr = int(data[2].value)
    days.append((day, name, gr))
res = {}
for k, *v in days:
    if v[0] in common_dt:
        temp = []
        for el in common_dt[v[0]]:
            temp.append(el * (v[1] / 100))
        res[k] = res.get(k, []) + [temp]
for el in res.values():
    print(*map(int, map(sum, zip(*el))))


