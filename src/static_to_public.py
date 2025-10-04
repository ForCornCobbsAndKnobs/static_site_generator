import os
import shutil


def static_to_public(static_dir, public_dir):
    if not os.path.isdir(static_dir):
        raise Exception("static path must be dir")
    if os.path.exists(public_dir):
        if os.path.isfile(public_dir):
            raise Exception("public path must be dir")
        else:
            shutil.rmtree(public_dir)
    os.mkdir(public_dir)
    _copy_dir(static_dir, public_dir)

def _copy_dir(src, dest):
    for entry in os.listdir(src):
        src_path = os.path.join(src, entry)
        dst_path = os.path.join(dest, entry)
        if os.path.isdir(src_path):
            os.mkdir(dst_path)
            _copy_dir(src_path, dst_path)
        else:
            shutil.copy(src_path, dst_path)
