import os
from static_to_public import static_to_public
from gen_content import generate_page
from pathlib import Path


def get_index_md():
    base = Path("./content")
    return list(base.rglob("index.md"))

def src_to_dst(src: Path) -> Path:
    rel = src.relative_to("content")
    dst = Path("public") / rel
    return dst.with_suffix(".html")

    

def main():
    here = os.path.dirname(__file__)
    static_dir = os.path.join(here, '..', 'static')
    public_dir = os.path.join(here, '..', 'public')
    static_to_public(static_dir, public_dir)

    index_mds = get_index_md()
    for index_md in index_mds:
        dst = src_to_dst(index_md)
        dst.parent.mkdir(parents=True, exist_ok=True)
        generate_page(str(index_md), './template.html', str(dst) )

if __name__ == "__main__":
    main()
