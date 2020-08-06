import argparse
import codecs
import json

import pandas as pd


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--ideology', nargs='+', type=str,
                        help='set <input.csv> (required) and <output.js> (optional, \"ideologies.js\" by default)',
                        metavar=('input.csv', 'output.js'))
    parser.add_argument('-q', '--question', nargs='+', type=str,
                        help='set <input.csv> (required) and <output.js> (optional, \"questions.js\" by default)',
                        metavar=('input.csv', 'output.js'))
    parser.add_argument('-s', '--special', nargs='+', type=str,
                        help='set <input.csv> (required) and <output.js> (optional, \"special.js\" by default)',
                        metavar=('input.csv', 'output.js'))
    return parser


def convert_ideology(input: str, output: str = 'ideologies.js'):
    ideo_name = '意识形态'
    econ_name = '经济'
    govt_name = '政治'
    scty_name = '社会'
    desc_name = '描述'
    link_name = '链接'
    df = pd.read_csv(input)
    print(df)
    ideologies = []
    for _, row in df.iterrows():
        if pd.isna(row[ideo_name]):
            continue
        item = {
            "name": row[ideo_name],
            "stats": {
                "econ": int(row[econ_name]),
                "govt": int(row[govt_name]),
                "scty": int(row[scty_name]),
            },
            "desc": row[desc_name],
            "link": row[link_name]
        }
        ideologies.append(item)
    json_str = json.dumps(ideologies, ensure_ascii=False, indent=4)
    with codecs.open(output, 'w', encoding='utf-8') as f:
        f.write('ideologies = ' + json_str + ';')


def convert_question(input: str, output: str = 'questions.js'):
    ques_name = '内容'
    econ_name = '平等'
    govt_name = '自由'
    scty_name = '进步'
    envo_name = '生态'
    spec_name = '特殊'
    df = pd.read_csv(input)
    print(df)
    questions = []
    for _, row in df.iterrows():
        if pd.isna(row[ques_name]):
            continue
        item = {
            "question": row[ques_name],
            "effect": {
                "econ": 0 if pd.isna(row[econ_name]) else int(row[econ_name]),
                "govt": 0 if pd.isna(row[govt_name]) else int(row[govt_name]),
                "scty": 0 if pd.isna(row[scty_name]) else int(row[scty_name]),
                "envo": 0 if pd.isna(row[envo_name]) else int(row[envo_name]),
            }
        }
        if not pd.isna(row[spec_name]):
            item.update({'special': row[spec_name]})
        questions.append(item)
    json_str = json.dumps(questions, ensure_ascii=False, indent=4)
    with codecs.open(output, 'w', encoding='utf-8') as f:
        f.write('questions = ' + json_str + ';')


def convert_special(input: str, output: str = 'special.js'):
    raise NotImplementedError()


if __name__ == '__main__':
    parser = get_parser()
    args = vars(parser.parse_args())
    if args['ideology'] is not None:
        ideology = args['ideology']
        if len(ideology) <= 2:
            convert_ideology(*ideology)
        else:
            parser.error('argument -i/--ideology: expected 1 or 2 arguments')
    if args['question'] is not None:
        question = args['question']
        if len(question) <= 2:
            convert_question(*question)
        else:
            parser.error('argument -q/--question: expected 1 or 2 arguments')
    if args['special'] is not None:
        special = args['special']
        if len(special) <= 2:
            convert_special(*special)
        else:
            parser.error('argument -s/--special: expected 1 or 2 arguments')
