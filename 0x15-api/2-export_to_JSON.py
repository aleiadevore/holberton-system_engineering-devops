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
        json_str = ''
        for task in all_tasks:
                json_str += json.dumps(
                        {argv[1]: [{'task': task.get(
                                'title'), 'completed': task.get(
                                'completed'), 'username': usrname}]})

        file_name = '{}.json'.format(argv[1])

        with open(file_name, mode='w') as f:
                f.write(json_str)
