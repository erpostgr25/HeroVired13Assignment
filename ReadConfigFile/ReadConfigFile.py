import configparser
import pymysql
import json, yaml
import os
from flask import Flask, Response

'''Pre-requisite on MySQL:
CREATE DATABASE configdb;

USE configdb;

CREATE TABLE configuration (
    id INT AUTO_INCREMENT PRIMARY KEY,
    config_json JSON NOT NULL
);
'''
def check_config(file_path):
    if not os.path.exists(file_path):
        print("Config file not found.")
        return None

    config = configparser.ConfigParser()
    config.read(file_path)

    result = {}
    for section in config.sections():
        result[section] = dict(config[section])
    return result

mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Blapk6020j',  # replace with your MySQL password
    'database': 'configdb',
    'cursorclass': pymysql.cursors.DictCursor
}

def save_mysql(config_data):
    
    conn = pymysql.connect(**mysql_config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM configuration")
    config_json = json.dumps(config_data)
    cursor.execute("INSERT INTO configuration (config_json) VALUES (%s)", (config_json,))
    conn.commit()
    print("Configuration saved to MySQL.")
    conn.close()

app = Flask(__name__)
@app.route('/getconfig', methods=['GET'])
def get_config():
    conn = pymysql.connect(**mysql_config)
    cursor = conn.cursor()
    cursor.execute("SELECT config_json FROM configuration")
    result = cursor.fetchone()
    conn.close()
    config_dict = json.loads(result['config_json'])
    safe_dict = json.loads(json.dumps(config_dict))
    yaml_data = yaml.dump(safe_dict, sort_keys=False)
    return Response(yaml_data, mimetype='text/yaml')

config_path = r"C:\Users\Shashi\OneDrive\Documents\Shashi_HeroVired13\HeroVired13Assignment\ReadConfigFile\config.ini"
config_data = check_config(config_path)

if config_data:
    save_mysql(config_data)
    app.run(debug=True)
