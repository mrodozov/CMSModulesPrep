import json
import os
import sys

def rewrite_vfs_file(vfs_file, root_path=None, local_module_map_file=None):

    with open(vfs_file, 'r') as vfsfile:
        data = json.load(vfsfile)
    l_root_path = os.path.abspath(root_path)
    l_local_module_map_file = os.path.abspath(local_module_map_file)
    data['roots'].append({"type": "directory",
                          "name":l_root_path,
                          "contents":[ {"type": "file",
                          "name": "module.modulemap", "external-contents" : l_local_module_map_file
                                        }]})

    print json.dumps(data, indent=1)
    with open(vfs_file, 'w') as vfsfile:
        vfsfile.write(json.dumps(data, indent=1))

if __name__ == "__main__":

    rewrite_vfs_file(sys.argv[1], sys.argv[2], sys.argv[3])
