#!/usr/local/python
"""
generate-bes-from-template.py

Created by James Stewart (@JGStew) on 2020-03-03.
"""

from __future__ import absolute_import

import pystache

def generate_bes_from_template(template_dict):
    """Generate BES XML file from info in template_dict hash table"""
    #renderer = pystache.Renderer()
    return pystache.Renderer().render_path(template_dict['template_file_path'], template_dict)


def main():
    """Only called if this script is run directly"""
    # get python dictionary with example config items (only works for python3?)
    #from examples.task_example_data import template_dict
    #print(template_dict)
    template_dict = {
                'template_file_path': 'examples/TEMPLATE_TASK.bes',
                'title': 'Example Generated From Template!',
                'download_size': 9999,
                'prefetch': 'prefetch file.txt',
                'action_script':
                """
delete /tmp/file.txt
copy __Download/file.txt /tmp/file.txt
"""
                }
    print(template_dict)
    print(generate_bes_from_template(template_dict))

# if called directly, then run this example:
if __name__ == '__main__':
    main()