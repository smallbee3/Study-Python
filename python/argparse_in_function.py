import argparse

MODES = ['base', 'local', 'dev', 'prod']


def get_mode():
    """
    Get the mode in which you want to build docker images
    :return:
    """

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-m', '--mode',
        help=f"Docker build mode({','.join(MODES)})"
    )
    args = parser.parse_args()

    print(args)
    # print(args.accumulate(args.integers))

    # print(args.mdoe)

    # 1) 모듈 호출 시 옵션으로 mode를 전달한 경우

    # build.py --mode <mode>
    # build.py --mode=<mode>
    # build.py -m <mode>
    # build.py -m=<mode>

    if args.mode:
        mode = args.mode.strip().lower()

    # 2) 사용자 입력으로 mode를 선택한 경우

    # build.py --mode
    # build.py -m

    else:
        while True:
            print('Select the mode you want to build')
            for index, mode_name in enumerate(MODES, start=1):
                print(f'{index}. {mode_name}')

            selected_mode = input('Choice mode: ')
            try:
                mode_index = int(selected_mode) - 1
                mode = MODES[mode_index]
                break
            except IndexError:
                print('Please input correct index number')

    return mode


if __name__ == '__main__':
    mode = get_mode()
    print(mode)
    # mode_function(mode)
