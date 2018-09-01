#-*- coding: utf-8 -*-

import mysql.connector
import config

from utils.helpers import *
from utils.singleton import Singleton


class SqlHelper(Singleton):
    def __init__(self):
        self.database_name = config.database_name
        self.init()

    def init(self):
        self.database = mysql.connector.connect(**config.database_config)
        self.cursor = self.database.cursor()

        self.create_database()
        self.database.database = self.database_name

    def create_database(self):
        try:
            command = 'CREATE DATABASE IF NOT EXISTS %s DEFAULT CHARACTER SET \'utf8\' ' % self.database_name
            log('sql helper create_database command:%s' % command)
            self.cursor.execute(command)
        except Exception as e:
            log('SqlHelper create_database exception:%s' % str(e))

    def create_table(self, command):
        try:
            log('sql helper create_table command:%s' % command)
            self.cursor.execute(command)
            self.database.commit()
        except Exception as e:
            log('sql helper create_table exception:%s' % str(e))

    def insert_data(self, command, data):
        try:
            #log('insert_data command:%s, data:%s' % (command, data))

            self.cursor.execute(command, data)
            self.database.commit()
        except Exception as e:
            log('sql helper insert_data exception msg:%s' % str(e))

    def execute(self, command):
        try:
            log('sql helper execute command:%s' % command)
            data = self.cursor.execute(command)
            self.database.commit()
            return data
        except Exception as e:
            log('sql helper execute exception msg:%s' % str(e))
            return None

    def query(self, command):
        try:
            #log('sql helper execute command:%s' % command)

            self.cursor.execute(command)
            data = self.cursor.fetchall()

            return data
        except Exception as e:
            log('sql helper execute exception msg:%s' % str(e))
            return None

    def query_one(self, command):
        try:
            log('sql helper execute command:%s' % command)

            self.cursor.execute(command)
            data = self.cursor.fetchone()

            return data
        except Exception as e:
            log('sql helper execute exception msg:%s' % str(e))
            return None
