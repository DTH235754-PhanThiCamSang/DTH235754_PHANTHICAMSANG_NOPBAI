# GitHub Copilot
def is_leap(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def days_in_month(month, year):
    if month == 2:
        return 29 if is_leap(year) else 28
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    if month in (4, 6, 9, 11):
        return 30
    return 0  # invalid month

def next_day(day, month, year):
    dim = days_in_month(month, year)
    if dim == 0 or day < 1 or day > dim or year < 1:
        raise ValueError("Ngày không hợp lệ")
    if day < dim:
        return day + 1, month, year
    # last day of month
    if month < 12:
        return 1, month + 1, year
    return 1, 1, year + 1

if __name__ == "__main__":
    try:
        d, m, y = map(int, input("Nhập ngày tháng năm (vd: 31 12 2023): ").split())
        nd, nm, ny = next_day(d, m, y)
        print(f"Ngày kế tiếp là: {nd:02d}/{nm:02d}/{ny}")
    except ValueError as e:
        print(e)
    except Exception:
        print("Dữ liệu nhập không hợp lệ. Vui lòng nhập 3 số nguyên.")