import json
import os
import re
import sys
import argparse
from collections import Counter


class Log:
    """Класс парсера логов"""
    report = {}

    def __init__(self, file_name):
        """Определение файла"""
        self.log_name = file_name
        try:
            with open(self.log_name) as f:
                self.log_file = f.read()
        except IOError:
            print(" ".join(["File error", self.log_name]))
            sys.exit(1)

    def set_value(self, key, value):
        self.report[key] = value

    def all_requests(self):
        """Вычисление всех запросов"""
        regexp = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
        ips_list = re.findall(regexp, self.log_file)
        self.set_value("All requests", len(ips_list))

    def requests_type(self):
        """Типы запросов"""
        regexp = r"GET|POST|PUT|DELETE"
        requests = re.findall(regexp, self.log_file)
        self.set_value("Requests type", dict(Counter(requests)))

    def top_ip(self):
        """Топ 10 ip-адрессов"""
        regexp = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
        ip_list = re.findall(regexp, self.log_file)
        sorted_ip = map(lambda x: x[0], sorted(Counter(ip_list).items())[:10])
        self.set_value("Top 10 of IP", list(sorted_ip))

    def longest_requests(self):
        """Топ 10 долгих запросов"""
        regexp = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(.*)(POST|GET)(.*?)( 2\d\d )(\d*)(.*?)'
        longest_logs = re.findall(regexp, self.log_file)
        longest_logs_info = list(map(lambda x: (x[2], x[0], x[5]), longest_logs))
        sorted_list = sorted(Counter(longest_logs_info).items())[:10]
        self.set_value("Top 10 of long requests", list(map(lambda x: x[0], sorted_list)))

    def client_errors(self):
        """Топ 10 клиентских ошибок"""
        regexp = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(.*)(POST|GET)(.*?)( 4\d\d )(.*?)'
        client_error_logs = re.findall(regexp, self.log_file)
        client_error_logs_info = list(map(lambda x: (x[0], x[2], x[4]), client_error_logs))
        sorted_list = sorted(Counter(client_error_logs_info).items())[:10]
        self.set_value("Top 10 of client errors", list(map(lambda x: x[0], sorted_list)))

    def server_errors(self):
        """Топ 10 серверных ошибок"""
        regexp = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(.*)(POST|GET)(.*?)( 5\d\d )(.*?)'
        client_error_logs = re.findall(regexp, self.log_file)
        client_error_logs_info = list(map(lambda x: (x[0], x[2], x[4]), client_error_logs))
        sorted_list = sorted(Counter(client_error_logs_info).items())[:10]
        self.set_value("Top 10 of server errors", list(map(lambda x: x[0], sorted_list)))

    def save_to_json(self):
        """Сохранение в json"""
        name = "".join(['parser', '.json'])
        with open(name, 'w') as json_file:
            json.dump(self.report, json_file)

    def analyze_all(self):
        self.all_requests()
        self.requests_type()
        self.top_ip()
        self.longest_requests()
        self.client_errors()
        self.server_errors()
        self.save_to_json()


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir', default="",
                        help="Указать путь директории или файл")

    return parser


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    apache_log = ""
    if os.path.exists(namespace.dir):
        if os.path.isfile(namespace.dir):
            apache_log = Log(namespace.dir)
        elif os.path.isdir(namespace.dir):
            files = os.listdir(namespace.dir)
            for file in files:
                if os.path.splitext(os.path.basename(file))[1] == '.log':
                    apache_log = Log("".join([namespace.dir, file]))
        if apache_log:
            apache_log.analyze_all()
    else:
        print("Error")
