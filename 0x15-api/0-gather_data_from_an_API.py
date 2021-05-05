#!/usr/bin/python3
""" Returns info about employee todo status """


if __name__ == "__main__":
        import requests
        from sys import argv

        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
        info = requests.get(url).json()
        name = info.get('name')

        params = {'completed': 'true'}
        completed = requests.get('{}/todos'.format(url), params=params).json()
        all_tasks = requests.get('{}/todos'.format(url)).json()

        print('Employee {} is done with tasks({}/{}):'.format(
                name, len(completed), len(all_tasks)))
        for item in completed:
                print('\t {}'.format(item.get('title')))
