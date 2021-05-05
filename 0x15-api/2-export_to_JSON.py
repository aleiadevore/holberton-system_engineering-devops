#!/usr/bin/python3
""" Returns info about employee todo status in json file """


if __name__ == "__main__":
        import json
        import requests
        from sys import argv

        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
        info = requests.get(url).json()
        usrname = info.get('username')

        all_tasks = requests.get('{}/todos'.format(url)).json()

        json_list = []
        new_dict = {}

        for task in all_tasks:
                json_list.append(
                        {'task': task.get(
                                'title'), 'completed': task.get(
                                'completed'), 'username': usrname})
        new_dict[argv[1]] = json_list

        file_name = '{}.json'.format(argv[1])

        with open(file_name, mode='w') as f:
                json.dump(new_dict, f)
