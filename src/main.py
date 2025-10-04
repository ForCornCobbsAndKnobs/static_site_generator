import os
from static_to_public import static_to_public
from gen_content import generate_page
from pathlib import Path

def src_to_dst(src: Path, dest_root: Path) -> Path:
    rel = src.relative_to("content")
    dst = dest_root / rel
    return dst.with_suffix(".html")

def generate_page_recursive(dir_path_content:str, template_path: str, dest_dir_path: str) -> None:
    content_root = Path(dir_path_content)
    dest_root = Path(dest_dir_path)

    for md in content_root.rglob("index.md"):
        dst = src_to_dst(md, dest_root)
        dst.parent.mkdir(parents=True, exist_ok=True)
        generate_page(str(md), template_path, str(dst))


    

def main():
    here = os.path.dirname(__file__)
    static_dir = os.path.join(here, '..', 'static')
    public_dir = os.path.join(here, '..', 'public')
    static_to_public(static_dir, public_dir)

    generate_page_recursive("./content", './template.html', './public')

if __name__ == "__main__":
    main()
