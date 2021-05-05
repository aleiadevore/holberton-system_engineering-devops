#!/usr/bin/python3
""" Returns info about employee todo status """


if __name__ == "__main__":
        import csv
        import requests
        from sys import argv

        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
        info = requests.get(url).json()
        name = info.get('username')

        all_tasks = requests.get('{}/todos'.format(url)).json()

        file_name = '{}.csv'.format(argv[1])

        with open(file_name, mode='w') as f:
                csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)
                for task in all_tasks:
                        csv_writer.writerow([argv[1], name, task.get(
                                'completed'), task.get('title')])
