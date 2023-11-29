import subprocess

HJ_file_path = 'HyeanJi/main.py'
HW_file_path = 'HyoWoo/main.py'
TH_file_path = 'TaeHoon/main.py'


def main():
    number = int(input('현지의 게임은 1, 효우의 게임은 2, 태훈이의 게임은 3을  입력해 주세요 : '))

    if number == 1:
        subprocess.run(['python', HJ_file_path])
    elif number == 2:
        subprocess.run(['python', HW_file_path])
    elif number == 3:
        subprocess.run(['python', TH_file_path])
    else:
        print("숫자를 다시 입력해 주세요.")

if __name__ == "__main__":
    main()
